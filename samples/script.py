# script/create_sample

input_file = r"C:\Users\User\Documents\germany\thesis\semantic change\database\Leipzig corpus\fas_news_2016_300K\fas_news_2016_300K-sentences.txt"
output_file = r"C:\Users\User\Documents\germany\thesis\semantic change\database\github_corpora\samples\Leipzig_sample_sentences.xml"

num_lines = 2000   # size of sample

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:
    for i in range(num_lines):
        line = fin.readline()
        if not line:
            break
        fout.write(line)
