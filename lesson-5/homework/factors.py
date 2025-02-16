def factors():
    integer = int(input('Enter a positive integer: '))
    i=1
    while i <=integer:
        if integer % i == 0:
            print(f'{i} is a factor of {integer}')
        i +=1

factors()