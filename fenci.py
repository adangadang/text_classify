import jieba
import os

ROOTDIR = "./ClassFile/C000007/"
DESTDIR = "./after_modify/fenci/"
changepath = ["07", "08", "10", "13", "14", "16", "20", "22", "23", "24"]

for i in changepath:
    rootdir = ROOTDIR.replace("07", i)
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if filename.endswith("txt"):
                txt_file = open(rootdir + filename , "rb")
                txt_content = txt_file.read()
                txt_seg_list = jieba.cut(txt_content)
                txt_write_log = "/".join(txt_seg_list)
                log_file = open(DESTDIR + i + "_" + filename[:-4] + ".log", "w")
                log_file.write(txt_write_log.encode('utf-8'))
                txt_file.close()
                log_file.close()


