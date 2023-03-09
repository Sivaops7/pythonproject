#love calculator
print("Welcome to the Love calculator!")
name = input("what is your name? \n")
name1 = input("what is their name? \n")
com_string = name + name1
lower_string = com_string.lower()
t = lower_string.count('t')
r = lower_string.count('r')
u = lower_string.count('u')
e = lower_string.count('e')
true = t + r + u + e
l = lower_string.count('l')
o = lower_string.count('o')
v = lower_string.count('v')
e = lower_string.count('e')
love = l + o + v + e
love_score = str(true) + str(love)
l = int(love_score)
print(f"Your love score is {love_score},")
if l < 10 or l > 90:
    print("you go together like coke and sentos.")
elif l > 40 or l > 50:
    print("your are alright together.")
else:
    print("love you.")
