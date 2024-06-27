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

player_choice = input("Choose your fighter: type R for Rock, P for Paper or S for Scissors. ")

R = rock
S = scissors
P = paper

print(player_choice)

import random
choices = [R, S, P]
num_choices = len(choices)
random_choice = random.randint(0, num_choices - 1)

computer_choice = choices[random_choice]    

print(computer_choice)
