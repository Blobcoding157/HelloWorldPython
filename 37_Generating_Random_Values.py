import random

for i in range(2):
    print(random.random())  # 2 zufällige zahlen

for i in range(3):
    print(random.randint(10, 20)) # zischen 10 und 20

members = ["John", "Daniel", "damn", "Bob"]
leader = random.choice(members)
print(leader)

#implementiere eine Klasse DICE() mit einer methode ROLL() die zwei würfel wirft und das ergebnis wiedergibt


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y



dice = Dice()
print(dice.roll())

