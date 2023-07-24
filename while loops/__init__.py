hommee = ""
started = False
while True:
    hommee = input("> ").lower()
    if hommee == "start":
        if started:
           print("Car is already started")
        else:
            started = True
        print("Car started, Go Go Go! ")
    elif hommee == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped oh no!")
    elif hommee == "help":
        print("""
Start = Car started, Go Go Go!
Stop = Car stopped oh no!
Quit = Exiting the game
""")
    elif hommee == "quit":
        break
    else:
        print("Sorry, My programmer didn't tell me what do those words mean :( ")
