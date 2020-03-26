print('this is an investment calculator')

initial_investment = float(input('how much do you want to invest: '))
interest_rate = float(input('how much is the interest_rate: '))
years = int(input('how many years are we investing in?: '))

# NPV = (Cash flows)/( 1+r)i

net_present_value_today = initial_investment / (1+ interest_rate)**years


print(net_present_value_today)  