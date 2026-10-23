class Mammal:
    def bark(self):
        print('DOG BARKS')
class Dog(Mammal):
    def sys(self):
        print('dog func')
obj1=Mammal()
obj2=Dog()
obj2.sys()
obj2.bark()
obj1.bark()
#inheritance