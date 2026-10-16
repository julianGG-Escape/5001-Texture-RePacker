from os import path
from PIL import Image

# locate folder
AFolder = "X:/Level 5/5001/Lessons/Misc/Assets/"
BFolder =  "E:/Escape studios/CT5001/Scripts/Misc/Assets/"
if path.isdir(AFolder):
    Folder = AFolder
else:
    Folder = BFolder


#implement numpy, check what channels are occupied

# onen all images as RGBA
img = Image.open(f"{Folder}Apples.webp").convert("RGBA")

print(img.mode)

#print(img.getbands())
#print(img.info)


R_chan = img.getchannel("R")
G_chan = img.getchannel("G")
B_chan = img.getchannel("B")

pack = Image.merge("RGB",(R_chan,G_chan,B_chan))

pack.show()