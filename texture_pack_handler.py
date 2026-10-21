#try "git add ." for pushing

from PIL import Image
#import numpy

#print(img.getdata)
#print(img.mode)

input_chan_lst = {
    }


def updateOutput(): # update the output image placeholder
    print("update output function")
    if input_chan_lst:
        combineChannels()

def mergeForOutput(image,active_channel):
    input_chan_lst[active_channel] = image


def combineChannels(col_space = "RGB"):
    #print(input_chan_lst)
    print(list(input_chan_lst.keys()))
    if "A" in input_chan_lst.keys():
        col_space = "RGBA"
        reqChans = 4
    else: 
        col_space = "RGB"
        reqChans = 3

    #print(len(input_chan_lst))
    if len(input_chan_lst) == reqChans:
        merge_chans = tuple(input_chan_lst.values())
        print(f"channels to be merged: {merge_chans}")
        pack = Image.merge(col_space,merge_chans) ## error here
        pack.show()
    else:
        print("missing a few channels")

def lockChannels(col_space, active_channel):
    print(f'Primary channel: "{active_channel}"')
    newchan = col_space.replace(active_channel,"")
    #if "B" in newchan:
    print(f'Locked channels: "{newchan}"')

def separateChannels(image,col_space):
    # this one splits image into channels
    for chan in col_space:
        col = chan
        chan = image.getchannel(chan)
        print (col,chan)
        #print(chan_lst(col))
        #chan.save(f"./Assets/{col}.jpg")

    return chan

def handler(file_path, active_channel = "R"): # channel defaulted to "R"
    image  =  Image.open(file_path)
    # detect of image is RGB(A) or Greyscale
    col_space = image.mode
    L = False
    #print(f"image mode is working: {img.mode}")
    match col_space:
        case "L":
            print("this image is greyscale")
            mergeForOutput(image, active_channel)
            L = True

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
    #updateOutput()
    return L



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

