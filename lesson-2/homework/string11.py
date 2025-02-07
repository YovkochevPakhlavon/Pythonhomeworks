str = input("Write a string: ")

if any(char.isdigit() for char in str):
    print("The string contains digits")
else:
    print("The string does not contain digits")