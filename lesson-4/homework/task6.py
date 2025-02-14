# Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

prime_num=[]
for i in range(1,101):
    if i==2 or i==3 or i==5 or i==7:
        prime_num.append(i)
    elif i!=1 and i % 2!=0 and i%3!=0 and i%4!=0 and i%5!=0 and i%7!=0 and i%8!=0 and i%9!=0 :
        prime_num.append(i)

print(prime_num)