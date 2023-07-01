import random
play = True

while play:

    box_price = str(input("How much would you want to sell this box of toys for? "))
    if box_price > str(20):
        print("\nSorry but the toys are not worth $" + str(box_price))
        print("How much would you want to sell this box of toys for? ")

    if box_price > str(20):
        print("\nWell let's wait until someone is here for the box of toys :) ")
        print("And then we would be $" + box_price + " richer ")
    else: print("If wanted I can Put a random number in (y/n) ")
    if 'y':
        box_price = random.randint(0, 20)
        
