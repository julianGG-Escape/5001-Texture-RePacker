from PIL import Image

openImg = Image.open

# 1. User provides image file
openImg = Image.open
img_orm = openImg(f"./Assets/sample_orm_tex.jpg")

R_img = openImg (f"./Assets/R.jpg")
G_img = openImg (f"./Assets/G.jpg")
B_img = openImg (f"./Assets/B.jpg")


channel_lst = { 
    # create empty so not have excessive channels
}
channel_lst.clear()

channel_lst["R"] = R_img
channel_lst["G"] = G_img
channel_lst["B"] = B_img


#pack_data = (R_img, G_img, B_img) # same as below
pack_data = tuple(channel_lst.values())

print(f"Pack data: {pack_data}")

pack = Image.merge("RGB",pack_data)
pack.show()
