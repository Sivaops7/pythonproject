#day5 practice
#loop concepts
fruits = ["Apple","peach","pear"]
for fruit in fruits:
    print(fruit)
    print(fruit +"pie")
print(fruits)
#average heights
height = input("input a list of students heights : ").split()
for n in range(0,len(height)):
    height[n] = int(str(height[n]))
total1 = 0
no1 = 0
for hei in height:
    total1 += hei
    no1 += 1
average = round(total1/no1)
print(f'your average heights {average}')
