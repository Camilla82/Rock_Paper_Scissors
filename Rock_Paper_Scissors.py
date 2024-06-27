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

#Write your code below this line 👇

R = rock
S = scissors
P = paper

player_choice = input("Choose your fighter: type R for Rock, P for Paper or S for Scissors. ")
if player_choice == "R":
  print(rock)
elif player_choice == "P":
    print(paper)
elif player_choice == "S":
    print(scissors)


import random
choices = [R, S, P]
num_choices = len(choices)
random_choice = random.randint(0, num_choices - 1)

computer_choice = choices[random_choice]    

print(computer_choice)

if player_choice == "R" and computer_choice == R:
    print("It's a draw.")
if player_choice == "P" and computer_choice == P:
    print("It's a draw.")
if player_choice == "S" and computer_choice == S:
    print("It's a draw.")
if player_choice == "R" and computer_choice == S:
    print("You win!")
if player_choice == "P" and computer_choice == R:
    print("You win!")
if player_choice == "S" and computer_choice == P:
    print("You win!")
else:
    print("You lose.")

