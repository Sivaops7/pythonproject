#treasure map
row1 = ["\U0001F606","\U0001F606","\U0001F606"]
row2 = ["\U0001F606","\U0001F606","\U0001F606"]
row3 = ["\U0001F606","\U0001F606","\U0001F606"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
num = input("Where do you want to put the treasure?")
horzi = int(num[0])
verti = int(num[1])
selected_row = map[verti-1]
selected_row[horzi-1] = "x"
print(f"{row1}\n{row2}\n{row3}")

