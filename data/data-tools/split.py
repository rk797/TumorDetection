import os
import shutil


os.chdir(r'train folder path here')

#moves 1/5 of data to the validation folder for training
for i,f in enumerate(os.listdir()):
    print(f)

    if i%5 == 0:
        shutil.move(f, r"put val folder path here"+"\\"+f)