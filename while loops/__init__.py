homme = ""

while True:
    homme = input("> ").lower()
    if homme == "start":
        print("Car started, Go Go Go! ")
    elif homme == "stop":
        print("Car stopped oh no!")
    elif homme == "help":
        print("""
Start = Car started, Go Go Go!
Stop = Car stopped oh no!
Quit = Exiting the game
""")
    elif homme == "quit":
        break
    else:
        print("Sorry, My programmer didn't tell me what do those words mean :( ")
