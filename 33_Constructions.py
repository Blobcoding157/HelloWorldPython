class Point:
    def __init__(self, x, y):   #construct or create an object
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point = Point(10,20)

#define a new type named person, should have a "name" attribute and a talk() methode

class Person:
    def __init__(self, name, speach):
        self.name = name
        self.speech = speach
    def talk(self):
        print(f"{self.name} says {self.speech}")


person1 = Person(input("name: "), input("Talk: "))
bob = Person("Bob Bobbington", "hello my dear")

person1.talk()
bob.talk()