password = str(input("Create a password: "))
if len(password) < 8:
    print("Password is too short.")
else:
    for x in password:
        if x.isupper():
            print("Password is strong.")
            break
        else:
            print("Password must contain an uppercase letter.")
            break


