#try "git add ." for pushing

from PIL import Image
import logging  # not showing currently
#import numpy

#print(img.getdata)
#print(img.mode)

input_chan_lst = {
    }


def updateOutput(): # update the output image placeholder
    logging.info("output updated")

def mergeForOutput(image,active_channel):
    input_chan_lst[active_channel] = image


def combineChannels(col_space = "RGB"):
    merge_chans = tuple(input_chan_lst.values())
    print(f"channels to be merged: {merge_chans}")
    pack = Image.merge("RGB",merge_chans) ## error here
    pack.show()

def lockChannels(channels, active_channel):
    logging.info(f'Primary channel: "{active_channel}"')
    newchan = channels.replace(active_channel,"")
    if "B" in newchan:
        logging.info(f'Locked channels: "{newchan}"')

def separateChannels(image,col_space):
    # this one splits image into channels
    for chan in col_space:
        col = chan
        chan = image.getchannel(chan)
        print (col,chan)
        #print(chan_lst(col))
        #chan.save(f"./Assets/{col}.jpg")

    return chan

def handler(image, active_channel = "R"): # channel defaulted to "R"
    # detect of image is RGB(A) or Greyscale
    col_space = image.mode
    #print(f"image mode is working: {img.mode}")
    match col_space:
        case "L":
            print("this image is greyscale")
            mergeForOutput(image, active_channel)

        case "RGB":
            print("this image is RBG")
            lockChannels(col_space,active_channel)
            separateChannels(image,col_space)
        case "RGBA":
            print("this image is RGBA")
            lockChannels(col_space,active_channel)
            separateChannels(image, col_space)

        case _:
            print(f"other image mode: {col_space}")

    updateOutput()



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

