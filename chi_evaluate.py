import os
ROOTDIR = "./after_modify/train/"
DESTDIR = "./after_modify/chi/"

total_doc_num = 0
total_vocabulary = {}
each_class_words = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
each_class_words_list = [[], [], [], [], [], [], [], [], [], []]
each_class_doc_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
class_index = ["07", "08", "10", "13", "14", "16", "20", "22", "23", "24"]
single_class_words = {}
write_list = []

for parent, dirnames, filenames in os.walk(ROOTDIR):
    for filename in filenames:
        train_file = open(ROOTDIR + filename, "rb")
        content = train_file.read()
        content_list = list(set(content.split("/")))

        index = class_index.index(filename[0:2])
        each_class_doc_num[index] += 1

        for i in content_list:
            if i in total_vocabulary:
                total_vocabulary[i] += 1
            else:
                total_vocabulary[i] = 1
            if i in each_class_words[index]:
                each_class_words[index][i] += 1
            else:
                each_class_words[index][i] = 1

        train_file.close()

total_doc_num = sum(each_class_doc_num)

for i in xrange(10):
    each_class_words_list[i] = each_class_words[i].keys()
    single_class_words.clear()
    for j in each_class_words_list[i]:
        num_a = each_class_words[i][j]
        num_b = total_vocabulary[j] - num_a
        num_c = each_class_doc_num[i] - num_a
        num_d = total_doc_num - num_a - num_b - num_c

        num_x = total_doc_num*(num_a * num_d - num_b * num_c)**2
        num_y = (num_a + num_c)*(num_a + num_b)*(num_b + num_d)*(num_c + num_d)

        single_class_words[j] = float(num_x)/num_y

    single_class_words_list = single_class_words.items()

    tmp_list = sorted(single_class_words_list, key = lambda x: x[1])
    tmp_list = list(reversed(tmp_list))
    write_list[:] = []
    for k in xrange(len(tmp_list)):
        write_list.append(tmp_list[k][0] + ":" + str(tmp_list[k][1]))

    write_content = "\n".join(write_list)
    dest_file = open(DESTDIR + "class" + str(i) + ".chi", "wb")
    dest_file.write(write_content)
    dest_file.close()



