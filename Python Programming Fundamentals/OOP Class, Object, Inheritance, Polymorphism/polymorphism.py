# class Hewan:
#     def __init__(self, nama):
#         self.nama = nama

#     def suara(self):
#         return "Hewan bersuara"

# class Anjing(Hewan):
#     def suara(self):
#         return "Guk guk!"

# class Kucing(Hewan):
#     def suara(self):
#         return "Meow!"

# class Sapi(Hewan):
#     def suara(self):
#         return "Moo!"

# Polymorphism in action
# hewan_list = [
#     Anjing("Buddy"),
#     Kucing("Kiri"),
#     Sapi("Bussie")
# ]

# Method yang sama, behavior berbeda
# for hewan in hewan_list:
#     print(hewan.suara())

# Duck Typing
# class Mobil:
#     def start(self):
#         return "mesin mobil menyala"

# class Motor:
#     def start(self):
#         return "mesin motor menyala"

# class Perahu:
#     def start(self):
#         return "mesin perahu menyala"

# Function yang polymorphic
# def operasikan_kendaraan(kendaraan):
#     print(kendaraan.start())

# Polymorphism dengan duck typing
# kendaraan_list = [
#     Mobil(),
#     Motor(),
#     Perahu()
# ]

# for kendaraan in kendaraan_list:
#     operasikan_kendaraan(kendaraan)

# Operator Overloading
# class Apple:
#     def __init__(self, jumlah):
#         self.jumlah = jumlah

#     def __add__(self, other):
#         return Apple(self.jumlah + other.jumlah)

#     def __str__(self):
#         return f"Apple: {self.jumlah}"

# apple1 = Apple(5)
# apple2 = Apple(3)
# apple3 = apple1 + apple2
# print(apple3)

# Abstract Base Class
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

shape = [
    Rectangle(5, 3),
    Circle(2)
]

for s in shape:
    print(f"Area is {s.area()}")