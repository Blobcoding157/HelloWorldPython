import random
#   rename all variables= variable makieren und shift F6
snumber = random.randrange(0, 10)
#print(snumber)
counter = 0
counter_Limit = 3
while counter < counter_Limit:
    number = int(input("Guess (0-10): "))
    counter += 1
    if number == snumber:
        print("you won!")
        break
if counter == counter_Limit:
    print(f"dödel es war {snumber}")