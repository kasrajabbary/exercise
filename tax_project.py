tax_rate = .2
standard_deduction = 10000
dependent_deduciton = 3000
grossIncome = float(input('salary:' ))
numDependents = int(input('dependents: '))

taxableIncome = grossIncome - standard_deduction - dependent_deduciton * numDependents
incometax = taxableIncome * tax_rate

print('the income tax is:' + str(incometax))