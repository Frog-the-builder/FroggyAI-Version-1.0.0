import random
import time

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

def stop():
    print(random.choice(Byelist))
    time.sleep(2)
    exit()

def calculator(operator, num1, num2):
    try: # Tries to convert the inputs to numbers
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Please input actual numbers")

    if operator == "addition": # Addition
        sumA = num1 + num2
        print(f"The answer is {sumA}")
        return sumA

    if operator == "subtraction": # Subtraction
        sumS = num1 - num2
        print(f"The answer is {sumS}")
        return sumS

    if operator == "multiplication": # Multiplication
        sumM = num1 * num2
        print(f"The answer is {sumM}")
        return sumM

    if operator == "division": # Division
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            sumD = num1 / num2
            print(f"The answer is {sumD}")

    else:
        print("Please select only 'addition', 'subtraction', 'multiplication', or 'division'.")

def rpc(): # Rock Paper Scissors game
    rpc_choices = ["rock", "paper", "scissors"]
    ai_choice = random.choice(rpc_choices)
    user_choice = input("Choose rock, paper, or scissors: ")
    print(f"FroggyAI chose {ai_choice}")

    if user_choice == ai_choice:
        print("It's a tie!")

    elif user_choice == "rock" and ai_choice == "paper":
        print("Round lost!")

    elif user_choice == "paper" and ai_choice == "rock":
        print("Round won!")

    elif user_choice == "scissors" and ai_choice == "rock":
        print("Round lost!")

    elif user_choice == "rock" and ai_choice == "scissors":
        print("Round won!")

    elif user_choice == "paper" and ai_choice == "scissors":
        print("Round lost!")

    elif user_choice == "scissors" and ai_choice == "paper":
        print("Round won!")

    elif user_choice not in rpc_choices:
        print("Please choose a valid option.")


name = input("What should I call you? ")
print(f"hello {name}, I am FroggyAI, the greatest frog ai of all time!")

while True:
    try:
        print("What can I do for you today? (1. for math, 2 for a joke, and 3 for rocks, 4 to exit)")
        choice = int(input("Enter your choice "))

        if choice == 1:
            calculator(input("Which operator do you want to use. 'addition', 'subtraction', 'multiplication', or 'division': "),
                       input("What is the first number: "),
                       input("What is the second number: "))

        elif choice == 2:
            print(random.choice(jokes))

        elif choice == 3:
            rpc()

        elif choice == 4:
            stop()

        else:
            print("please choose a valid option")

    except KeyboardInterrupt: # If you stop the program forcefully then it will also do the fancy stuff. Also removes the keyboard interupt error
        print("")
        stop()
