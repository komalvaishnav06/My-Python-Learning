class dog:
    def bark(self):
        print('barking!')
class animal(dog):
    def eat(self):
        print('eating')

d = animal()
d.eat()
d.bark()
