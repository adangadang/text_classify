import os
import math

ROOTDIR = "./after_modify/train/"
DESTDIR = "./after_modify/tf_idf/"
total_words = {}
single_file_words_list = []
single_file_words_dict = {}
write_list = []
total_files = 0

for parent, dirnames, filenames in os.walk(ROOTDIR):
    for filename in filenames:
        train_file = open(ROOTDIR + filename, "rb")
        content = train_file.read()
        content_list = content.split("/")

        for i in content_list:
            if i in total_words:
                total_words[i] += 1
            else:
                total_words[i] = 1

        train_file.close()

total_files = len(total_words)

for parent, dirnames, filenames in os.walk(ROOTDIR):
    for filename in filenames:
        train_file = open(ROOTDIR + filename, "rb")
        content = train_file.read()
        content_list = content.split("/")

        length = len(content_list)
        content_set = list(set(content_list))

        dest_file = open(DESTDIR + filename[:-4] + ".sort","wb")
        single_file_words_dict.clear()
        write_list[:] = []
        for i in content_set:
            num = content_list.count(i)
            tf = float(num)/length
            idf = math.log(float(total_files)/total_words[i])
            tf_idf = tf*idf
            single_file_words_dict[i] = tf_idf

        single_file_words_list = single_file_words_dict.items()
        tmp_list = sorted(single_file_words_list,  key = lambda x: x[1])
        tmp_list = list(reversed(tmp_list))
        for i in xrange(len(tmp_list)):
            write_list.append(tmp_list[i][0] + ":" + str(tmp_list[i][1]))

        write_content = "\n".join(write_list)
        dest_file.write(write_content)

        train_file.close()
        dest_file.close()
