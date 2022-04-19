birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)

#int()
#float()
#bool()

#übung: ask a user their weight (in pounds), convert it to kilograms and print on the terminal

weight = input('what is your weight(in pounds)? ')
kilo = float(weight) * 0.45
print(f'your weight is {kilo} kg')