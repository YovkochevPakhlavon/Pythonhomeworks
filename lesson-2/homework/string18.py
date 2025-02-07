sentence = input("Write a sentence: ").split()

if sentence[0] == sentence[-1]:
    print(f"True, it starts and ends with the same word which is \'{sentence[0]}\' ")
else:
    print(f"False, it starts with the word \'{sentence[0]}\' and ends with the word \'{sentence[-1]}\'. ")
