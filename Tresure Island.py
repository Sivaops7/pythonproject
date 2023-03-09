#treasure island
print(r'''\

                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /


            ''')
print("Welcome To Treasure Island.\n your mission is to find the treasure.")
side = input("You're at a cross road. where o you want to go? Type Left or Right  ")
if side == 'left':
    s = input("You come to a lake. There is an island in the middle of the lake. Type WAIT to wait for a boat. Type swim to swim across ")
    if s == 'wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.Which colour do you choose?")
        if door == 'yellow':
            print("Congralution.You Win")
        else:
            print(" You enter a room of beasts.Game Over")
    else:
        print("You are Drowned.Game Over")
else:
    print("You are choosing worng side. Game Over")
