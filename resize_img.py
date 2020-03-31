from PIL import Image, ImageDraw
import os
import shutil
test = os.listdir('Images')
parse = 0
dst = "New_Images" #Vart filerna sparas för 256 bilderna
for x in test: #x = filenamn
    file_path = "Images/"+x
    image = Image.open(file_path)
    new_image = image.resize((256, 256)) #Bestäm hur vilken 
    file_path = str(parse)+x
    new_image.save(file_path)
    parse+=1
    shutil.move(file_path, dst) #Flyttar filen till rätt map genom dst

