import random as r
target = r.randint(1, 100)
print("I have chosen a number between 1 and 100.")
count = 0
while True:
    guess = eval(input("Enter your guess: "))
    count += 1
    if guess > target:
        print("Too high.")
    elif guess < target:
        print("Too low.")
    else:
        print("Congratulations! You've got it in", count, "tries.")
        break
