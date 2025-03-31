import random
target_num =  random.randint(1,1000)
attempts=0
print("Welcome to the guess number game!")
print("I have selected a number between 1 to 1000!")
while True:
    guess= int(input("Enter your guess:"))
    attempts+=1
    if guess> target_num:
        print("Too high! Try again.")
    elif guess < target_num:
        print("Too low! Try again.")
    else:
        (print(f"Congratulations! You guessed it in {attempts} attempts."))
        break


 