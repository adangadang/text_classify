import os
from math import log

os.system("date")

TRAIN_DIR = "./after_modify/train_result/"
TEST_DIR = "./after_modify/test/"
class_num = 10
condprob_dict = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
class_enum = ["07", "08", "10", "13", "14", "16", "20", "22", "23", "24"]
words_list = []

relevant = [0,0,0,0,0,0,0,0,0,0]
detect = [0,0,0,0,0,0,0,0,0,0]
fit = [0,0,0,0,0,0,0,0,0,0]

vocabulary_file = open(TRAIN_DIR + "vocabulary_file.txt", "rb")
vocabulary_content = vocabulary_file.read()
vocabulary_list = vocabulary_content.split("\n")
vocabulary_file.close()

prior_file = open(TRAIN_DIR + "prior.txt", "rb")
prior_content = prior_file.read()
prior_list = [float(x) for x in prior_content.split("/")]
prior_file.close()

for i in xrange(class_num):
    condprob_file = open(TRAIN_DIR + "condprob" + str(i) + ".txt", "rb")
    condprob_content = condprob_file.read()
    condprob_doc_list = condprob_content.split("\n")
    for x in condprob_doc_list:
        tmp_list = x.split(":")
        condprob_dict[i][tmp_list[0]] = float(tmp_list[1])
    condprob_file.close()

for i in xrange(len(class_enum)):
    TARGET_DIR = TEST_DIR + class_enum[i] + "/"
    print TARGET_DIR
    for parent, dirnames, filenames in os.walk(TARGET_DIR):
        for filename in filenames:
            test_file = open(TARGET_DIR + filename, "rb")
            test_content = test_file.read()
            test_list = test_content.split("/")
            test_file.close()

            words_list[:] = []
            for x in test_list:
                if x in vocabulary_list:
                    words_list.append(x)

            score = [log(x) for x in prior_list]

            for index in xrange(class_num):
                t_list = list(condprob_dict[index])
                for t in t_list:
                    if t in words_list:
                        score[index] += log(condprob_dict[index][t])

            class_index = score.index(max(score))

            relevant[i] += 1
            detect[class_index] += 1
            if i == class_index:
                fit[i] +=1

    precision = float(fit[i])/detect[i]
    print "The %d" %i + " class's situation is:"
    print "   Precision rate is %f." %precision

total_fit = sum(fit)
total_doc_num = sum(relevant)
total_precision = float(total_fit)/total_doc_num
print "The total precision is %f!" %total_precision



os.system("date")

