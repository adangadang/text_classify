import os
import jieba.posseg as pseg
ROOTDIR = "./after_modify/fenci/"
DESTDIR = "./after_modify/no_stop_noun/"

for parent, dirnames, filenames in os.walk(ROOTDIR):
    for filename in filenames:
        log_file = open(ROOTDIR + filename, "rb")
        log_content = log_file.read()
        log_list = log_content.split("/")

        stop_file = open("./stop_words.txt", "rb")
        stop_content = stop_file.read()
        stop_list = stop_content.split("\n")

        for i in stop_list:
            num = log_list.count(i)
            for j in xrange(num):
                log_list.remove(i)

        log2_content = "/".join(log_list)

        type_words = pseg.cut(log2_content)
        noun_words = []
        for w in type_words:
            if "n" in w.flag:
                noun_words.append(w.word)
                noun_content = "/".join(noun_words)

        noun_file = open(DESTDIR + filename[0:2] + "/" + filename[3:-4] + ".log", "wb")
        noun_file.write(noun_content.encode('utf-8'))
        noun_file.close()
        log_file.close()
        stop_file.close()
