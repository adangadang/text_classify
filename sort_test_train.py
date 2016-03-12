import os

ROOTDIR = "./after_modify/no_stop_noun/"
TRAIN_DIR = "./after_modify/train/"
TEST_DIR = "./after_modify/test/"

change_path = {"07", "08", "10", "13", "14", "16", "20", "22", "23", "24"}

for i in change_path:
    for parent, dirnames, filenames in os.walk(ROOTDIR + i):
        for filename in filenames:
            if int(filename[:-4]) < 1500:
                os.system("mv " + ROOTDIR+i+"/"+filename +" "+ TRAIN_DIR+i+"_"+filename)
            else :
                os.system("mv " + ROOTDIR+i+"/"+filename +" "+ TEST_DIR+i+"/"+filename)
