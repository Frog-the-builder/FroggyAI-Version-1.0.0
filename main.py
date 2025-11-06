import random
import time

    #joke function

def Joke():
    return random.choice(jokes)

    #calculator function

def calculator():
    operator = input("Would you like addition, subtraction, multiplication, or division? ")

    #Addition

    if operator == "addition":
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number:"))
        sumA = num1 + num2
        print(f"The answer is {sumA}")

    else:
        print("please put a number")

        #subtraction

    if operator == "subtraction":
        num1sub = float(input("Please enter the first number: "))
        num2sub = float(input("Please enter the second number:"))
        sumS = num1sub - num2sub
        print(f"The answer is {sumS}")

    else:
        print("please put a number")

        #multiplication
    if operator == "multiplication":
        num1mul = float(input("Please enter the first number: "))
        num2mul = float(input("Please enter the second number:"))
        sumM = num1mul * num2mul
        print(f"The answer is {sumM}")

    else:
        print("please put a number")

        #division

    if operator == "division":
        num1div = float(input("Please enter the first number: "))
        num2div = float(input("Please enter the second number:"))
        sumD = num1div / num2div
        print(f"The answer is {sumD}")

    else:
        print("please put a number:")

    #rock paper scissors game

def rpc():
    
    rpc_choices = ["rock", "paper", "scissors"]
    ai_choice = random.choice(rpc_choices)
    user_choice = input("Choose rock, paper, or scissors: ")
    print(f"FroggyAI chose {ai_choice}")

    if user_choice == ai_choice:
        print("It's a tie!")

    if user_choice == "rock" and ai_choice == "paper":
        print("Round lost!")

    if user_choice == "paper" and ai_choice == "rock":
        print("Round won!")

    if user_choice == "scissors" and ai_choice == "rock":
        print("Round lost!")

    if user_choice == "rock" and ai_choice == "scissors":
        print("Round won!")

    if user_choice == "paper" and ai_choice == "scissors":
        print("Round lost!")

    if user_choice == "scissors" and ai_choice == "paper":
        print("Round won!")

    if user_choice not in rpc_choices:
        print("Please choose a valid option.")

Byelist = [
    "until we meet again",
    "see you later alligator",
    "after a while crocodile",
    "stay froggy my friend",
    "until next time, rabbin!",
    "hop you later!"
]


jokes = [
    "Why did the frog take the bus to work today? Because his car got toad!",
    "What do you call a frog with no hind legs? Unhoppy!",
    "Why are frogs so happy? Because they eat whatever bugs them!",
    "What do you get when you cross a frog with a dog? A croaker spaniel!",
    "Why did the frog sit on the lily pad? He wanted to be a little boulder!",
    "What do you call a frog that's illegally parked? Toad!",
    "What do you call a frog that's great at basketball? A jump shot!",
    "Why did the frog go to the library? To check out some hop-eras!",
    "What do you call a frog that loves to eat candy? A sweet-toad!",
    "Why did the frog bring a suitcase to the pond? He was going on a hop-cation!",
    "What do you call a frog that's great at baseball? A home run toad!"
    "and why did the frog cross the road? To get to the hopping mall!"
]



name = input("What should I call you? ")
print(f"hello {name}, I am FroggyAI, the greatest frog ai of all time!")

while True:
    print("What can I do for you today? (1. for math, 2 for a joke, and 3 for rocks, 4 to exit)")
    choice = int(input("Enter your choice "))



    if choice == 1:
        calculator()

    if choice == 2:
        print(Joke())

    if choice == 3:
        rpc()

    if choice == 4:
        print(random.choice(Byelist))
        time.sleep(2)
        break
    
    if choice > 4:
        print("please choose a valid option")

