
# if it's hot
#   it's a hot day
#   Drink plenty of water
# otherwise if it's cold
#   it's a cold day
#   wear warm clothes
# otherwise
#   it's a lovely day

is_hot  = False
is_cold = True

if is_hot:
    print("it's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("enjoy your lovely day")

#übung: price of a house  is 1Million €
# if buyer has good credit,
#   they need a put down 10%
# otherwise
#   they need a put down 20%
#Print the down payment

H_price = 1000000
g_credit = False

if g_credit:
    endprice = H_price *1.1
    print(f'your credit is good, so the house will cost {endprice}€ and you pay {abs(H_price - endprice)}€ extra')
else: b_credit:
    endprice = H_price *1.2
    print(f'your credit is bad, so you pay {endprice}€ and you pay {abs(H_price - endprice)}€ extra')

