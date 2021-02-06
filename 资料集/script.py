
data = []
file_handle = open("train_set1.txt", mode ="w", encoding = 'utf-8')
for line in open("train.txt", encoding='utf-8'):
    words = line.strip().split()
    if words[-1] == "1":
       line = " ".join(words[0:-1])
       print(line)
       file_handle.write(line+"\n")
