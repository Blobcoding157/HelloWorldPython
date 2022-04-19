names = ["John" , "Bob" , "Mash" , "Sara" , "Maggy" ]
print(names[:])

names[0] = "Jon"
print(names[:])

numbers = [0,1,2,3,4,5,60,7,8,9,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

