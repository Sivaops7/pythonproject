#day 3
#conditional statements, logical operators,code blocks and scope
print("welcome to the roolercoaster!")
height = int(input("what is your height in cm ? "))
if height >= 120:
    print(" you can ride the rollercoaster! ")
else:
    print("Sorry, you have to grow taller before you can rid")
#Odd or even
num=int(input("which number do you want to check the number :"))
if num % 2 == 1:
    print("This is odd number.")
else:
    print("This is an even number. ")
#nested if/else statement
print("Welcome to the rollercoaster !")
height1 = int(input("What is your height in cm? "))
if height1 >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter yor age?"))
    if age < 12:
        print("Please pay $5.")
    elif age<=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
# leap year calculation
year=int(input("Which year u want calculated?"))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year!")
else:
    print("Not leap year!")
#multiple if statements in succession
print("Welcome to the rollercoaster !")
height1 = int(input("What is your height in cm? "))
if height1 >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter yor age?"))
    if age < 12:
        bill = 5
        print("Child ticket are $5.")
    elif age<=18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("adult tickets are $12.")
        wants_ph = input("Do you want a photo taken? Y or N. ")
    if wants_ph == 'y':
        bill += 3
        print(f"your bill is {bill}")
    else:
        print(f"your bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
#pizza deliveries
print("welcome to Python Pizza Deliveries!")
size = input("what size pizza do you want? s, m, l:")
add_pepp = input("Do you want pepperoni? y or n ")
extra_ch = input("Do you want extra chees?y or n ")
if size == 's':
    bill = 15
    if add_pepp == 'y':
        bill +=2
        if extra_ch == 'y':
            bill +=1
            print(f"Your final bill is {bill}")
        else:
            print(f"Your final bill is {bill}")
    else:
        print(f"Your final bill is {bill}")
elif size == 'm':
    bill = 20
    if add_pepp == 'y':
        bill += 3
        if extra_ch == 'y':
            bill += 1
            print(f"Your final bill is {bill}")
        else:
            print(f"Your final bill is {bill}")
    else:
        print(f"Your final bill is {bill}")
else:
    bill = 25
    if add_pepp == 'y':
        bill += 3
        if extra_ch == 'y':
            bill += 1
            print(f"Your final bill is {bill}")
        else:
            print(f"Your final bill is {bill}")
    else:
        print(f"Your final bill is {bill}")