driving = False

while True:
    inp = input("> ").upper()
    if inp == "HELP":
        print("""
start   -   to start the car
stop    -   to stop the car
quit    -   to exit car game """)

    elif inp == "START":
        if driving:
            print("the car is already driving!")
        else:
            driving = True
            print("Car started... let's go")

    elif inp == "STOP":
        if driving:
            driving = False
            print("the car stopped")
        else:
            print("dödel! the car is already stopped")

    elif inp == "QUIT":
        print("see you next time!")
        break

    else:
        print("I don't understand")