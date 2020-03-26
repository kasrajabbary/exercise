#name = 'hithere' 

#print(name.split(" "))
#nomo = name.replace('i','o')
#print(nomo)
frOm = []
fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for file in fileList:
    print(file.split())
    #print(file[0])

    for f in file.split():
        print(f[:4])
        frOm.append(f[:4])
print(frOm)



f = open("integers.txt")
theSum = 0
for line in f:
    line = line.strip()
    number = int(line)
    theSum += number
    print("The sum is", theSum)
