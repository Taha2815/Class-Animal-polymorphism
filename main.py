from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can play video games")

class snake(Animal):
    def move(self):
        print("I can slither")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

R = human()
R.move()

K = snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move