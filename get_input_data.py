import os
ROOTDIR = "./after_modify/tf_idf/"
DESTDIR = "./after_modify/input_data/"
words_num = 4
tmp_list = []
write_list = []
class_index = ["07", "08", "10", "13", "14", "16", "20", "22", "23", "24"]

for parent, dirnames, filenames in os.walk(ROOTDIR):
    for filename in filenames:
        tf_idf_file = open(ROOTDIR + filename, "rb")
        content = tf_idf_file.read()
        content_list = content.split("\n")

        tmp_list[:] = [(x.split(":"))[0] for x in content_list]
        write_list[:] = []

        if len(content_list) < words_num:
            write_list[:] = tmp_list
        else:
            write_list[:] = tmp_list[0:words_num]

        write_content = "/".join(write_list)
        dest_file = open(DESTDIR + filename[:-5] + ".input", "wb")
        dest_file.write(write_content)
        tf_idf_file.close()
        dest_file.close()



