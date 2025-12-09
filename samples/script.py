# script/create_sample

input_file = r"C:\Users\User\Documents\germany\thesis\semantic change\database\MIZAN-FA\mizan_words and sentences.xml"
output_file = r"C:\Users\User\Documents\germany\thesis\semantic change\database\github_corpora\samples\mizan_sample.xml"

num_lines = 50   # size of sample

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:
    for i in range(num_lines):
        line = fin.readline()
        if not line:
            break
        fout.write(line)
