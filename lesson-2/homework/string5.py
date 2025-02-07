str = input("Write some sentence: ")

strlow = str.lower()
vowels = {'a','e','i', 'o', 'u'}
consonants = {'w', 'm', 'j', 'r', 'z', 'c', 'h', 'l', 'p', 'k', 's', 'b', 'y', 'n', 'f', 'q', 't', 'd', 'x', 'g',
                  'v'}
num_vow=0
num_con=0
i=0

while i < len(str):
    if strlow[i] in vowels:
        num_vow +=1
    elif strlow[i] in consonants:
        num_con +=1
    i +=1

print(f"The number of vowels is {num_vow} and the number of consonants is {num_con}.")
