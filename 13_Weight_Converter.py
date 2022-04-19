# inplement a weight converter from or to Kg <-> Pound

weight = int(input("what is your weight? " ))

a = input("Pound(P) or Kilo (K): " )

if a.upper() == "P":
    print(f'your weight is {weight * 0.45} Kg')
elif a.upper() == "K":
    print(f'your weight is {weight * 2.20} Pound')
else:
    print("write P,p or K,k du dödel")