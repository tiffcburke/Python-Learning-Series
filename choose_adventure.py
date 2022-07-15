# Python learning series

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input('''You are on a dirt road, 
it has come to an end and you can go left or right.
Which way would you like to go? ''').lower()

if answer == "left": 
    answer = input(
    '''You have come to a river, 
    you can walk around it or swim across it. 
    Type which path you choose(walk or swim): ''').lower()
   
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")

elif answer == "right":
    answer = input(
        '''You have came to a bridge, it looks wobbly,
         do you want to cross it or head back? (cross / head back) '''
    ).lower()
    if answer == "head back":
        print("You go back to the main road and lose.")
    elif answer == "cross":
        answer = input(print("You crossed the bridge and meet a stranger. Do you talk to them? (Yes/No) "))

        if answer == "yes":
            print("You talk to the stranger and he gives you gold. You won!")

        elif answer == "no":
            print("You ignore the stranger and you lose.")
        
        else:
            print("Not a valid option, you lose.")

else: 
    print("Not a valid option, you are now lost.")

