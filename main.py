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


import random

list  = [rock, paper, scissors]

variable = random.randint(0, len(list))

cc = list[variable]

user = int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))

uc = list[user]

print(uc)
print()
print(cc)

if uc == cc:
  print("It's a draw!")
elif uc == rock and cc == scissors:
  print("You win!!")
elif uc == rock and cc == paper:
  print("You lose 😕")
elif uc == scissors and cc == rock:
  print("You lose 😕")
elif uc == scissors and cc == paper:
  print("You win!!")
elif uc == paper and cc == scissors:
  print("You lose 😕")
elif uc == paper and cc == rock:
  print("You win!!")
else:
  print("Game Over!")

