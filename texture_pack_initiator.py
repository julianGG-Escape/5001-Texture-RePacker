import texture_packer as tp
from os import path
import imp
imp.reload(tp)

# locate folder
AFolder = "X:/Level 5/5001/Tool Texture RePacker/Assets/"
BFolder =  "E:/Escape studios/CT5001/Scripts/Misc/Assets/" # this is wrong
if path.isdir(AFolder):
    Folder = AFolder
else:
    Folder = BFolder

# 1. User provides image file
openImg = tp.Image.open
img = tp.Image.open(f"{Folder}Apples.webp") #.convert("RGBA")
img_orm = tp.Image.open(f"{Folder}sample_orm_tex.jpg")

R_img = openImg (f"./Assets/R.jpg")
G_img = openImg (f"./Assets/G.jpg")
B_img = openImg (f"./Assets/B.jpg")


#img_orm.show()

tp.handler(R_img,"R")
tp.handler(G_img,"G")
tp.handler(B_img,"B")

tp.combineChannels()