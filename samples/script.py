# script/create_sample

input_file = r"C:\Users\User\Documents\germany\thesis\semantic change\database\Matina\Matina-D1403032901_newsKhordad1403_dedup90_P.jsonl"
output_file = r"C:\Users\User\Documents\germany\thesis\semantic change\database\Matina\Matina-newsKhordad1403.jsonl"

num_lines = 50   # size of sample

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:
    for i in range(num_lines):
        line = fin.readline()
        if not line:
            break
        fout.write(line)
