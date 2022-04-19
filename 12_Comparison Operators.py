#if temperature is greater than 30 it's a hot day
# otherwise if it is less than 10, it is a cold day
#otherwise it's neither hot or cold

temperature = int(input("what is your temperature?" ))


if temperature >= 30:
    print("it's a hot day")
elif temperature <= 10:
    print("it's a cold day")
else:
    print("It's nice outside")

#if name is less than 3 caracters long
#   name must be at least 3 caracters
# otherwise if it's more than 50 characters long
# nam can be a maximum of 50 characters
# name looks good

name = input("input your name " )

if len(name) < 3:
    print("your name is too short, like you")
elif len(name) > 50:
    print("your name is too long for our servers to handle")
else:
    print("name safed Mr/Ms. " + name)

