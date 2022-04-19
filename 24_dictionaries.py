customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True,
}

customer["birthdate"] = "Jan 1 1980" #add
print(customer.get("name", "Default value"))
print(customer.get("non existend value", "Default value"))

customer["name"] = "JacksepticEye" #change

print(customer.get("name", "Default value"))

#make a programm that changes input numbers to words using dictionaries

phone = input("Phonenumber: ")

digits = {
    "0": "ZERO ",
    "1": "ONE ",
    "2": "TWO ",
    "3": "THREE ",
    "4": "FOUR ",
    "5": "FIVE ",
    "6": "SIX ",
    "7": "SEVEN ",
    "8": "EIGHT ",
    "9": "NINE ",

}
output = ""
for dig in phone:
    output += digits.get(dig, "!") + " "

print(output)
