import random

def guess():
    number = random.randrange(0, 100)

    score= 0
    for i in range(1,20):
        try:
            myNumber = int(input("Enter a number: "))

            score += 1
            if number == myNumber:
                print(f"Congratulations! The number is:{number}. Your score: {score} ")
                break
            elif number < myNumber:
                print("Number is too high.Try Again!")
            elif number > myNumber and myNumber > -1:
                print("Number is too low.Try Again!")
            elif myNumber < 0:
                print("The number isn't possible negative! Please write positive number!")

            elif score == 20:
                print("Too many attempts. You lose!")
        except:
            print("Please write a number!")






guess()

