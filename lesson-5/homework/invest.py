def invest(amount, rate, years):
    i=1
    while i <= years:
        value = amount*(1+rate)**i
        print(f'year {i}: {round(value,2)}')
        i+=1

invest(100, .05, 4)

def invest():
    amount = float(input('the principal amount: '))
    rate = float(input('rate: '))
    years = int(input("a number of years: "))
    i=1
    while i <= years:
        value = amount*(1+rate)**i
        print(f'year {i}: {round(value,2)}')
        i+=1

invest()