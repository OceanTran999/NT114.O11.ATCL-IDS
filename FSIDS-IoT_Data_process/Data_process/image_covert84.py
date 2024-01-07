from PIL import Image

import os

path = "./UNSW-NB15/"
path1 = "./UNSW-NB15/"


folders = os.listdir(path)
# files = os.listdir(path)
# print(files)
for folder in folders:
    folder_path = os.path.join(path, folder)
    files = os.listdir(folder_path)
    # save_path = path1+folder
    save_path = os.path.join(path1, folder)
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    for pic in files:
        # print(pic)
        img = Image.open(os.path.join(folder_path, pic)).convert('RGB')
        img = img.resize((84, 84), resample=Image.LANCZOS)
        print(img.getbands())  #
        print(img.size)

        # file_name, file_extend = os.path.splitext(pic)
        # print(file_name,file_extend)
        # pic_new = os.path.join(os.path.abspath(save_path), file_name + '.jpg')

        # pic_new = os.path.join(os.path.abspath(save_path), pic)
        pic_new = os.path.join(save_path, pic)

        img.save(pic_new)
