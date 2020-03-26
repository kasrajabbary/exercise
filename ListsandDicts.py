#fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
#for index in range(len(fileList)):
#    print(fileList[index].upper())
#    print(fileList[index][0].upper())

aList = [34, 45, 67]
target = 45
#if target in aList:
#    print(aList.index(target))
#else:
#    print(-1)

#for index in range(len(aList)):
#    if target in aList:
#        print(index, aList[index])
#        print(aList.index(target))

first = [10, 20, 30]

second = first
print(first)
print(second)
print(first[1])
first[1] = 99
print(second)

third = []
for elements in first:

    third.append(elements)

print(third)
print(first)

fourth = list(first)
print(fourth)

