#day 4 rock paper scissor game
import random
select = int(input("what do you choose> type 0 for ROCK, 1 for PAPER or 2 for SCISSOR."))
rock = (r'''rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
paper = (r'''paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) ''')
scissors = (r'''scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
num = [rock,paper,scissors]
ra_num = random.randint(0, 2)
if select >=3 or select < 0:
    print("You typed the Invaild No")
else:
    print(f"you choose {num[select]}")

    choice = num[ra_num]
    print(f"computer choose {choice}")
    if select == 0 and ra_num == 2:
        print(f"you win")
    elif ra_num == 0 and select == 2:
        print(f"you loose")
    elif ra_num > select:
        print(f"you loose")
    elif select > ra_num:
        print("you win")
    elif select == ra_num:
        print(f"It's draw ")