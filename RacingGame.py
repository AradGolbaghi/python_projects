import random

play = True
temp = -1

while play:
    first_car = int(input("What's the speed of the first car? the rout 100km: "))
    print("\n The speed of the first car is " + str(first_car))
    while first_car > 100:
        first_car = int(input("\n What's the speed of the first car? the rout is 100km: "))
        print("\n The speed of the first car is " + str(first_car))
        print("\n Your car's speed needs to be less then a 100")

    while temp == first_car:
        print("You can't use a number more then once")
        first_car = int(input("\n What's the speed of the first car? the rout is 100km: "))
        print("\n The speed of the first car is " + str(first_car))

    temp = first_car
    second_car = random.randint(0, 100)
    print("\n The speed of the second car is " + str(second_car))

    if first_car > second_car:
        again = input("\n Well Done! You have won this RACE :) (y/n) \n")
        if again == "n":
            play = False
            print("Have Fun with your day ;) ")
    elif second_car > first_car:
        again = input("\n Oh No! You have lost try again to WIN :(  (y/n) \n")
        if again == "n":
            play = False

            print("Have Fun with your day ;) ")
    else:
        again = input("\n Draw! Do you want to play again (y/n) \n")
        if again == "n":
            play = False
            print("Have Fun with your day ;) ")
