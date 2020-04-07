#------------------------------------------------------------------------------------------------------------------
#För att användas behöver du en Music fil med alla midi filer i form av mid. Du behöver även en map för alla bilder
#------------------------------------------------------------------------------------------------------------------

from music21 import converter, instrument, note, chord
import json
import sys
import numpy as np
from imageio import imwrite
import os
from PIL import Image
import shutil

def extractNote(element):
    return int(element.pitch.ps)

def extractDuration(element):
    return element.duration.quarterLength

def get_notes(notes_to_parse):

    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    durations = []
    notes = []
    start = []

    for element in notes_to_parse:
        if isinstance(element, note.Note):
            if element.isRest:
                continue

            start.append(element.offset)
            notes.append(extractNote(element))
            durations.append(extractDuration(element))
                
        elif isinstance(element, chord.Chord):
            if element.isRest:
                continue
            for chord_note in element.notes:
                start.append(element.offset)
                durations.append(extractDuration(element))
                notes.append(extractNote(chord_note))

    return {"start":start, "pitch":notes, "dur":durations}

def midi2image(midi_path):
    mid = converter.parse(midi_path)

    instruments = instrument.partitionByInstrument(mid)

    data = {}

    try:
        i=0
        for instrument_i in instruments.parts:
            notes_to_parse = instrument_i.recurse()

            if instrument_i.partName is None:
                data["instrument_{}".format(i)] = get_notes(notes_to_parse)
                i+=1
            else:
                data[instrument_i.partName] = get_notes(notes_to_parse)

    except:
        notes_to_parse = mid.flat.notes
        data["instrument_0".format(i)] = get_notes(notes_to_parse)

    resolution = 0.25

    for instrument_name, values in data.items():
        # https://en.wikipedia.org/wiki/Scientific_pitch_notation#Similar_systems
        upperBoundNote = 127
        lowerBoundNote = 21
        maxSongLength = 100

        index = 0
        prev_index = 0
        repetitions = 0
        while repetitions < 70:  #Hur många bilder den sparar utav sången. Om den överskrider sången blir bilden helt svart. Om för liten tar den inte hela sången
            if prev_index >= len(values["pitch"]):
                break

            matrix = np.zeros((upperBoundNote-lowerBoundNote,maxSongLength))

            pitchs = values["pitch"]
            durs = values["dur"]
            starts = values["start"]

            for i in range(prev_index,len(pitchs)):
                pitch = pitchs[i]

                dur = int(durs[i]/resolution)
                start = int(starts[i]/resolution)

                if dur+start - index*maxSongLength < maxSongLength:
                    for j in range(start,start+dur):
                        if j - index*maxSongLength >= 0:
                            matrix[pitch-lowerBoundNote,j - index*maxSongLength] = 255
                else:
                    prev_index = i
                    break

            imwrite(midi_path.split("/")[-1].replace(".mid",f"_{instrument_name}_{index}.png"),matrix)
            index += 1
            repetitions+=1

midi_path = sys.argv[1]
destination = sys.argv[2]
test = os.listdir(midi_path) #Tar fram alla sånger i filen mid och lägger ihop allt i listan test

for songs in test:
    song_path = songs
    midi2image(midi_path+"/"+song_path) 
    os.remove(midi_path+'\\'+song_path) #Tar bort sången 
    
    dst = destination #Vart filerna sparas
    parse = 0
    arr = os.listdir() #Tar alla filer
    ending = ".png" 
    for x in arr:
        png_images = x.endswith(ending) #Tar ut vilka filer som slutar med .png
        if png_images:
            file_name = x
            im = Image.open(file_name, 'r')
            pixel_values = list(im.getdata()) #Alla pixel värden från bilden
            radera = True
            if 255 in pixel_values:
                print("Saved File",parse)
                parse +=1
                radera = False
            if radera:
                os.remove(file_name)    #Tar bort helt svarta bilder
            elif radera == False:
                shutil.move(file_name, dst) #Flyttar filen till rätt map genom dst
    print("Nästa sång!")




