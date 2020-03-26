#name = 'Alan Turing!'

#print(name[0])

#for index in range(len(name)):

#    print(index, name[index])


fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
data = []
for file in fileList:
    if 'program' in file:
        data.append(file)
print(data)
gram = []
for i in data:
    gram.append(i[4:7])

print(gram)

exe = []
for i in data:
    exe.append(i[10:])

print(exe)


    
