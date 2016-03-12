import os

DOCDIR = "./after_modify/input_data/"
CHIDIR = "./after_modify/chi/"
DESTDIR = "./after_modify/train_result/"
chi_list = []
total_doc_num = 0
vocabulary_list = []
each_class_doc_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
class_index = ["07","08", "10", "13", "14", "16", "20", "22", "23", "24"]
class_union_text = [[], [], [], [], [], [], [], [], [], []]
condprob = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

for i in xrange(10):
    chi_file = open(CHIDIR + "class" + str(i) + ".chi", "rb")
    chi_content = chi_file.read()
    chi_total_list = chi_content.split("\n")
    chi_word_list = [(item.split(":"))[0] for item in chi_total_list]
    chi_list.extend(chi_word_list[0:3000])
    chi_file.close()
    echo_file = open(DESTDIR + "tmp.txt", "wb")
    echo_content = "\n".join(chi_list)
    echo_file.write(echo_content)
    echo_file.close()


for parent, dirnames, filenames in os.walk(DOCDIR):
    for filename in filenames:
        index = class_index.index(filename[0:2])
        each_class_doc_num[index] += 1

        docfile = open(DOCDIR + filename, "rb")
        doc_content = docfile.read()
        doc_list = doc_content.split("/")
        for word in doc_list:
            if word in chi_list:
                vocabulary_list.append(word)
                class_union_text[index].append(word)

        docfile.close()


vocabulary_list = list(set(vocabulary_list))
total_doc_num = sum(each_class_doc_num)

prior = [float(x)/total_doc_num for x in each_class_doc_num]

for i in xrange(len(class_union_text)):
    denominator = len(vocabulary_list) + len(class_union_text[i])
    for word in vocabulary_list:
        num = class_union_text[i].count(word)
        condprob[i][word] = "%.20f" %(float(num + 1)/(denominator + 1))

vocabulary_file = open(DESTDIR + "vocabulary_file.txt", "wb")
vocabulary_content = "/".join(vocabulary_list)
vocabulary_file.write(vocabulary_content)
vocabulary_file.close()

prior_file = open(DESTDIR + "prior.txt", "wb")
prior_list = [str(x) for x in prior]
prior_content = "/".join(prior_list)
prior_file.write(prior_content)
prior_file.close()

for i in xrange(len(condprob)):
    cond_file = open(DESTDIR + "condprob" + str(i) + ".txt", "wb")
    cond_list = [(x + ":" + condprob[i][x]) for x in condprob[i]]
    cond_content = "\n".join(cond_list)
    cond_list[:] =[]
    cond_file.write(cond_content)
    cond_file.close()








