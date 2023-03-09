print("! welcome to the tip calculator !")
totalBill = float(input("what was the total bill ?"))
tipPre = int(input("what percentage tip would you like to give ? 10, 12, or 15 ?"))
totalPeople = int(input("how many people to split the bill ?"))
preTot = totalBill*(1+tipPre/100)
bill = preTot/totalPeople
final=round(bill,2)
print("Each person should pay : " + str(final))

