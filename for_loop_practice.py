lower_bound = int(input('what number is lower_bound :'))
upper_bound = int(input('what number is upper_bound :'))
each_sum = 0
for eachpass in range(lower_bound, upper_bound + 1):
    each_sum = each_sum + eachpass
    print(each_sum)