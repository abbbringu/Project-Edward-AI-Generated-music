
<!-- PROJECT SHIELDS -->
<!--
** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="img/music_notes_PNG64.png" alt="logo" width="100" height="200">
  </a>

  <h3 align="center">Project_Edward</h3>

  <p align="center">
    Ett program som genererar music!




<!-- TABLE OF CONTENTS -->
## Innehållsförteckning

* [Om Projektet](#om-projektet)
  * [Byggd Med](#byggd-med)
* [Börja](#börja)
  * [Förarbete](#förarbete)
  * [Drive](#drive)
  * [Träning](#träning)
  * [Träning från början](#träning-från-början)
  * [Träning från påbörjad träning](#träning-från-påbörjad-träning)
* [Användning](#användning)



<!-- ABOUT THE PROJECT -->
## Om Projektet

Projektet handlar om att skapa music utav ett dataset i form av midi. Filen ska helst vara ett instrument. Jag har gått igenom andra metoder som Lstm för att generera musik. Jag blev missnöjd med resultaten och bestämde att arbeta vidare. Lstm tog in massor med data och kan bestämma vilka noter som ska spelas efter på varandra. Konsekvensen blev att det inte gick att implemeterar durationer och pauser. 

För projektet har jag tänkt använda stylegan för att göra musik. Stylegan är teknisk sätt för bilder. Vilket vi kan använda. Därför använder vi midifiler. Man kan konvertera midifiler till ett kordinat system. X-axeln blir tid och Y axen blir noten. Vi kan spara koriatsystement som en png bild. Varje låt blir ungefär 5-50 bilder långa. Förhoppnings vis får vi ett bra resultat. En risk är att stylegan tar bilder oavsett vart i sången den är. Det vill säga att stylegan kommer inte uppfatta om en början och slut, allt är detsamma. 

<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="img/210appass_1_Piano_6.png" alt="logo" width="256" height="256">
</a>

Överblick av projektet:
* Samla in midi filer i formen (.mid) 
* Konverterar mid filerna till .png
* Gör om bilderna till ett data set (tfrecord) 
* Använd datasetet och börja träna
* Använd bilderna och minimera den till 100x106 res för att senare konvertera den till mid fil igen
Spela midifilerna

### Byggd Med
Här hittar du orginal koder som hjälpte med projektet.
* [Stylegan](https://github.com/t04glovern/stylegan-pokemon)
* [Midi2img and Img2midi](https://github.com/mathigatti/midi2img)
* [Resizing images](https://auth0.com/blog/image-processing-in-python-with-pillow/)
* [Orginala Google Colab](https://colab.research.google.com/drive/1zPmnBwNix4wSARUZ9izE92t6TjzVqN2P#scrollTo=zh3adHVfo7yj)



<!-- GETTING STARTED -->
## Börja

Det här projektet använder [datasetet](https://www.kaggle.com/soumikrakshit/classical-music-midi). Det här datasetet är klassisk musik som bara spelas av ett instrument. 
Här är även min [google-colab](https://colab.research.google.com/drive/1HbpWlQ8gaTG6c4ps7POXD-sSs-6mbWLg#scrollTo=JF1mwki7pjZc) fil som du kan följa.

### Förarbete

Vi börjar med att clona det vi behöver för det här projektet. Vi gör även mappar för vart bilderna kommer hamna. 
Sist använder vi tensorflow 1.
```sh
%cd /content/
!git clone https://github.com/abbbringu/Project_Edward
!mkdir Music
!mkdir Raw
!mkdir Images
%tensorflow_version 1.x
```

### Drive

För att koppla colab med drive använder vi:
```sh
from google.colab import drive
drive.mount('/content/drive')
# drive.mount("/content/drive", force_remount=True)
%cd /content/drive/My Drive/
!mkdir STYLE-GAN
%ls
%cd /content

!ln -s "/content/drive/My Drive/STYLE-GAN" /STYLE-GAN
%cd /STYLE-GAN
%ls
```
Samtidigt skapar vi en mapp "STYLE-GAN" och gör en förkorning från /content/drive/My Drive/STYLE-GAN till /STYLE-GAN

### Eget Dataset

För att göra vårt eget dataset måste vi först ha bilder. Gör en mapp i STYLE-GAN som heter "Music" i google drive. Ta bort filer som slutar på ".MID" eller (".MIDI"). Koden kan endast ta in ".mid" filer. Sedan kör vi koden midi2img-py. Alla bilder borde ligga i /content/Raw. Bilderna i /Raw kommer ut i storlek 100x106 och därför behöver vi resize_img.py vilket gör om de till 256x256. Bilderna hamnar då i Images. 

När vi har bilderna använder vi:
```sh
%cd /content/Project_Edward/Stlye-Gan
!python dataset_tool.py create_from_images (Path till vart datan ska sparas) (/content/Images/)
```
Eftersom stylegan använder sig utav tfrecord måste vi konvertera bilderna. (Startkt rekomenerat att bilderna sparas i driven i en mapp som heter data)

### Träning

Träningen är från början inställd på att träna en ny model i res 256x256. Den är även inställd på att ta ocn spara datan på driven. Det kan anändras beroende på vart du vill ta och spara filerna. Allt finns i /content/Stlye-Gan/config.py
```sh
result_dir = '/STYLE-GAN/results' #Där resultaten sparas
data_dir = '/STYLE-GAN' #Där mappen med tfrecord filerna finns
```
I /content/Stlye-Gan/Train.py Måste det om du inte har en map i drive/STYLE-GAN som heter "data", inte har bilder i 256x256, vill träna med mirror eller vill använda mer än 1 gpu. Om inte kan du ignorera det här stycket.
Du kan hita koden under vid rad 35-36
```sh
35  # Dataset.
36  desc += '-custom';     dataset = EasyDict(tfrecord_dir='data', resolution=256);              train.mirror_augment = False
```
#### Träning från början
Om du vill träna från början kan du lämna content/Style-Gan/training/training_loop.py för det mesta i fred. Men en sak kan som kan ändras är totala träningar. Du hittar det vid rad 129:
```sh
   129    total_kimg = 15000,    # Total length of the training, measured in thousands of real images.
```
Det finns även andra inställningar som kan vara bra att ha på eller av beroende på anvädningen.

#### Träning från påbörjad träning
För att starta en träning från en påbörjad träning behöver du ändra 2 saker i content/Style-Gan/training/training_loop.py Du måste först ange vart din senaste pkl fil är. De lär vara någon stans (driven) STYLE-GAN/results/00009-sgan-custom-1gpu/network-snapshot-003765.pkl
Du lägger pathen i:
```sh
   136    resume_run_id = STYLE-GAN/results/00009-sgan-custom-1gpu/network-snapshot-003765.pkl
```
Och sedan måste du även ändra hur långt den kom (I det här fallet 3765):
```sh
   138    resume_kimg = 3765,      # Assumed training progress at the beginning. Affects reporting and training schedule.
```



<!-- USAGE EXAMPLES -->
## Användning

För att använda ai och för att producera en genererad bild använder vi invoke scriptet från stylegan. Det som behövs är pathen till apk filen.


```sh
%cd /content/Project_Edward/Stlye-Gan
!python invoke.py \
    --model_file '/content/stylegan-pokemon/Weights/MichaelFriese10_pokemon.pkl'
```

Bilderna vi får ut måste vi ändra till 100x106 och sedan köra in den i img2midi sciptet
Och sedan midi till mp3:

```sh
!sudo apt-get install timidity
!timidity test.mid -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k test.mp3
```

