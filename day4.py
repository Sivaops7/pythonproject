#day 4 practice
#Randomisation and Python Lists
import random
ran_num = random.randint(1,10)
print(ran_num)
ran_float = random.random()
print(ran_float)
ran_mul = ran_float * 5
print(ran_mul)
love_score = random.randint(1,100)
print(f"your love score is {love_score}")
#head or tails
rand_coin = random.randint(0,1)
if rand_coin == 0:
    print("Head")
else:
    print("Tails")
#random sellect name paying bill
name_string = input("Give me everybody's names, seperated by a comma.")
name = name_string.split(",")
print(name)
length = len(name)
ran_name = random.randint(0,length-1)
person = name[ran_name]
print(f"{person} is going to buy the meal today !")
person1 = random.choice(name)
print(f"{person1} is going to buy the meal today !")
