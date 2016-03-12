# text_classify

我的代码并不是整一个文件，而且也不是各文件之间相互调用，就只是一个文件一个文件运行，其中运行顺序如下：

1. fenci.py，就是单纯使用结巴分词对全部语料库进行分词。
2. remove_stop_extract_noun.py，就是去除停用词和取名词
3. sort_test_train.py，将测试集和训练集区分开来
4. cal_tf_idf.py，对训练集计算tf_idf值
5. get_input_data.py，对计算好tf_idf值的文件取最大的4个tf_idf值写入新的文件，作为训练材料
6. chi_evaluate.py，使用开放检验生成开放检验值的文件
7. train_classify.py，通过input_data文件和chi文件进行训练，得到训练结果
8. test_doc_precise.py，使用训练结果对测试集进行分类，并输出准确率