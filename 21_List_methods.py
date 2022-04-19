numbers = [5,2,1,1,7,4]
numbers.append(20)  #insert at the end
print(numbers)

numbers.insert(2,10) #insert where,what
print(numbers)

numbers.remove(5)   #remove item
print(numbers)

numbers.pop() #deletes last item
print(numbers)

print(numbers.index(7)) #an welcher stelle steht der wert

print(7 in numbers)

print("count ist "+ str(numbers.count(1)))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

numbers.clear() # alles löschen
print(numbers)

print(numbers2)

#übung duplikate entfernen

liste = [4,1,2,5,7,5,5,5,5,5,5,5,5,5]
uniques =[]

print(liste)

for item in liste:
    if item not in uniques:
        uniques.append(item)
print(uniques)