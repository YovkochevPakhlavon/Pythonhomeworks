str = input("Write a string: ").lower()
vowels={'a','e','i','o','u'}
v=list(vowels)
i=0
new=str
while i<len(v):
    new = new.replace(v[i],'*')
    i +=1

print(new)
