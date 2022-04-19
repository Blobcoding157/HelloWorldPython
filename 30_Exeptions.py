try:
    age = int(input("age: "))
    income = 2000
    rist = income / age
    print(age)
except ValueError:
    print("gib eine nummer ein du dummer dödel")
except ZeroDivisionError:
    print("age can not be 0")