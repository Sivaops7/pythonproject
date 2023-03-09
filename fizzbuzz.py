#fizzbuzz exercise
print("welcome to the fizzbuzz exercise")
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("fuzzbuzz")
    elif n % 3 == 0:
        print("Fuzz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)