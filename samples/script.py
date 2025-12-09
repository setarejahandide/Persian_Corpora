# script/create_sample

input_file = r"C:\Users\User\Documents\germany\thesis\semantic change\database\MIZAN-FA\fa (1).txt"
output_file = r"C:\Users\User\Documents\germany\thesis\semantic change\database\github_corpora\samples\mizan_sample_raw.xml"

num_lines = 50   # size of sample

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:
    for i in range(num_lines):
        line = fin.readline()
        if not line:
            break
        fout.write(line)
