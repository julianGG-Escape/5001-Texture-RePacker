from os import path
from PIL import Image
import numpy


# locate folder
AFolder = "X:/Level 5/5001/Tool Texture RePacker/Assets/"
BFolder =  "E:/Escape studios/CT5001/Scripts/Misc/Assets/" # this is wrong
if path.isdir(AFolder):
    Folder = AFolder
else:
    Folder = BFolder


# 1. User provides image file
img = Image.open(f"{Folder}Apples.webp") #.convert("RGBA")


#print(img.getdata)
#print(img.mode)



"""
class InputData(channel = None, data = None):
    def __init__(self, channel, data):
        self.channel = channel
        self.data = data
        pass
"""
def updateOutput(): # update the output image placeholder
    print("output updated")


def lockChannels(channels, active_channel):
    print(active_channel)
    newchan = channels.replace(active_channel,"")
    print(newchan)
    if "B" in newchan:
        print(f"B is in {newchan}")

def separateChannels(image,image_mode):
    # this one splits image into channels
    for chan in image_mode:
        col = chan
        chan = image.getchannel(chan)
        print (col,chan)

    return chan

def handler(image, active_channel = "R"): # channel defaulted to "R"
    # detect of image is RGB(A) or Greyscale
    image_mode = image.mode
    #print(f"image mode is working: {img.mode}")
    match image_mode:
        case "L":
            print("this image is greyscale")

        case "RGB":
            print("this image is RBG")
            lockChannels(image_mode,active_channel)
            separateChannels(image,image_mode)
        case "RGBA":
            print("this image is RGBA")
            lockChannels(image_mode,active_channel)
            separateChannels(image, image_mode)

        case _:
            print(f"other image mode: {image_mode}")

    updateOutput()

handler(img)

for letters in "ABC":
    print(letters)

"""
# this one gets separate files for channels
RED_CHANNEL = InputData("R")
GREEN_INPUT = InputData("G")
BLUE_INPUT = InputData("B")
"""



"""
class OutputData(format = "RGBA", all_channels = None):
    Output = Image.merge(format,(all_channels = None))
    pass
"""




"""
print(f"\nRED CHANNEL: {numpy.array(img.getchannel('R'))}")
print(f"\nALPHA CHANNEL: {numpy.array(img.getchannel('A'))}")

"""
#can implement numpy, check what channels are occupied

#print(img.getbands())
#print(img.info)





#pack = Image.merge("RGB",(R_chan,G_chan,B_chan))

#R_chan.show()
#print(R_chan)
#invertR_chan = R_chan * -1
#pack.show()

