import random

for i in range(10):

    print(random.randint(1,6), end=' ')



smallest = int(input('what is the smallest :'))
largest = int(input('what is the largest :'))

myNumber = random.randint(smallest, largest)

count = 0
while True:
    count +=1
    userNumber = int(input('choose a number :'))
    if userNumber < myNumber:
        print('too small')

    elif userNumber > myNumber:
        print('too big')
    else:
        print('great you got it in' , count, 'tries')
        break
