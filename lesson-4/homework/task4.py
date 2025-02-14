import random
selected_number=random.randint(0, 100)
i=1
while i <= 10:
    guess = int(input("Guess the number: "))
    if guess == selected_number:
        print("You guessed it right!")
        break
    elif i == 10:
        answer = input("You lost. Want to play again?: ")
        answers = ['Y', 'YES', 'y', 'yes', 'ok']
        if answer in answers:
            i=1
    elif guess < selected_number:
        print("Too low!")
    elif guess > selected_number:
        print("Too high!")
    i +=1
    
