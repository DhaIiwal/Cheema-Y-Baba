import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
userChoice = int(input("What do you choose? Type 0 for rock, 1 for Paper, and 2 for Scissors"))
computerChoice = random.randint(0, len(images)-1)
print(computerChoice,userChoice)
print(images[userChoice])
print("Computer chose: ")
print(images[computerChoice])
if userChoice == computerChoice:
    print("draw")
if userChoice == 0:
    if computerChoice == 1:
        print("Loose")
    elif computerChoice == 2:
        print("win")

elif userChoice == 1:
    if computerChoice == 0:
        print("Win")
    elif computerChoice == 2:
        print("loose")

elif userChoice == 2:
    if computerChoice == 0:
        print("loose")
    elif computerChoice == 1:
       print("win")


