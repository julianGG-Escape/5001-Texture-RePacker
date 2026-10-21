# move up a folder to use

import texture_packer as tp
#from os import path
from importlib import reload

reload(tp)

# depricated
"""
import imp
imp.reload(tp)
"""

"""
# locate folder
AFolder = "X:/Level 5/5001/Tool Texture RePacker/Assets/"
BFolder =  "E:/Escape studios/CT5001/Tool-Texture-RePacker/Assets/" # this is wrong
if path.isdir(AFolder):
    Folder = AFolder
else:
    Folder = BFolder
"""
    
# 1. User provides image file
openImg = tp.Image.open
img = tp.Image.open(f"./Assets/Apples.webp") #.convert("RGBA")
img_orm = tp.Image.open(f"./Assets/sample_orm_tex.jpg")

R_img = openImg (f"./Assets/R.jpg")
G_img = openImg (f"./Assets/G.jpg")
B_img = openImg (f"./Assets/B.jpg")


#img_orm.show()

#tp.handler(img_orm)

tp.handler(R_img,"R")
tp.handler(G_img,"G")
tp.handler(B_img,"B")

tp.combineChannels()