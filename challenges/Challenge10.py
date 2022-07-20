# URL: http://www.pythonchallenge.com/pc/return/bull.html
#region Challenge 10
import os

print("Challenge 10: ")
print("-----------------------------------------------------")

# Create the look and say sequence for the first 30 numbers
seq = []

cur_num = "1X"
cur_symbol = cur_num[0]
cur_sym_cnt = 0
new_seq_entry = ""

for i in range(30):
    for num in cur_num:
        if(num == cur_symbol):
            cur_sym_cnt += 1
        else:
            new_seq_entry += str(cur_sym_cnt) + str(cur_symbol)
            cur_sym_cnt = 1
            cur_symbol = num
    seq.append(new_seq_entry)
    
    cur_num = str(seq[-1]) + "X"
    cur_symbol = cur_num[0]
    cur_sym_cnt = 0
    new_seq_entry = ""

solution = str(len(seq[-1]))
solution_url = "http://www.pythonchallenge.com/pc/return/" + solution + ".html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion