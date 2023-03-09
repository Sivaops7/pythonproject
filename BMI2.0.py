#BMI 2.0 CALCULATOR
#BMI CALCULATER
height=float(input("Enter your height in m :"))
weight=float(input("Enter your weight in kg :"))
bmi=(weight)/(height)**2
final=round(bmi,2)
print("Your BMI value : "+str(final))
bm = int(bmi)
if bm <= 18.5:
    print("You are underweight. ")
elif bm <= 25:
    print("You have a normal weight.")
elif bm <= 30:
    print("You are overweight.")
elif bm <= 35:
    print("You are obese")
else:
    print("You are clicically obese.")



