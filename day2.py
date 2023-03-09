#Day 2 practice
#Beginner - Understanding Data Types and How to Manipulate Strings
num_char = len(input("Whats your name ? "))
new_num_char=str(num_char)
print("Your name has "+ new_num_char +" characters.")
print("HELLO"[0])
print(str(40)+str(70))
two_digit_num=input("enter the number :" )
print(type(two_digit_num))
add_num=int(two_digit_num[0])+int(two_digit_num[1])
print(type(add_num))
print("your enter number is "+str(add_num))
print(type(6/3))
print(2**3)
print(3*3+3/3-3)
#BMI CALCULATER
height=input("enter your height in m :")
weight=input("enter your weight in kg :")
bmi=int(weight)/float(height)**2
print("your BMI value : "+str(bmi))
#f-sring
score = 0
height = 1.8
isWinning = True
print(f"your score is {score},your height is {height}, your are Winning is {isWinning}")
age=input("what is your current age ?")
age_as_int = int(age)
year_remaining = 90 - age_as_int
day_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
month_remaining = year_remaining * 12
print (f"you have {day_remaining},{weeks_remaining} weeks,and {month_remaining} month left.")
