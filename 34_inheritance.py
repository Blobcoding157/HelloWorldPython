class Mammal:
    def walks(self):
        print("walks")

class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def meow(self):
        print("meaow")

dog1 = Dog()
dog1.walks()

cat1 = Cat()
cat1.meow()