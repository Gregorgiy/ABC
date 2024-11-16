# ТЕМА ФУНКЦИИ
# def lol(*args):
#     print(args)

# lol(69,228,288,True,"gef")

# def gun2(**kwargs):
#     strna = kwarks.get('strna')
#     strnis = kwarks['strnnis']

#     print(strna,strnis)


#     gun2(number=12,strna="Hello world")
# class Hero:
#     power = 200
    
#     leon = 2
    
#     her = 3
   
#     hope = 21
#     name = "Hero"
    
#     def walk(self):
#         print("Person walking")
    
#     def info(self):
#         print(self.name)
#         print(" -",self.leon)
#         print("intelligent -",self.hope)
#         print("lovkost -",self.her)
#         print("smart -",self.hor)

# obj = Hero("Michael""Petrovich""1488")
# obj.name = "Hero"
# obj.info()
# class Human: 
#     #Статичесике поля или атрибутами 
#     organizes_count = { 
#         "eyes":2, 
#         "foot":2, 
#         "head":1, 
#         "po4ki":2,
#         "apendix":1
#     } 
#     eyes = 2
#     hromosomERMEK = 1000-7
#     rot = 1
# def __init__(self,name,surname,year_birth,): 
# #динамические атрибуты  
#         self.name = name 
#         self.surname = surname 
#         self.year_birth = year_birth 
     
# #методы класса 
# def say_hello(self): 
#         print(f"Hello {self.name}") 
     
# def age(self): 
#         print(2024 - self.year_birth) 
     
# obj = Human("Jonh","Doe",1989)
# class BankAccount:
#   def check_pass

# class BankAcount: 
#     USD = 1000
#     EU = 889
#     KGS = 89000
#     def __init__(self,privet,id,card): 
#         self.privet = privet
#         self.id = id 
#         self.card = card

 
#     def check_pass(self,passw): 
#         if passw == self.privet: 
#             return True 
#         else: 
#             return False 
#     def info(self):
#         print(self.privet,self.id,self.card) 


# obz = BankAcount(6723,0,20) 
# obz.info()
# class Point:
#     __secret_key = 8968
#     def __init__(self, x,y,res):
#         self.__x = x
#         self.__y = y
#         self.res = res

#     def setX_V(self,sc,x,y):
#         if sc == self.__secret_key:
#             self.__x = x
#             self.__y = y
#             return True
#         else:
#             return False

#     def getX_Y(self):
#         return (self.__x,self.__y)

# alpha = Point(23.22,563.02,["Iron","trees"
# a,b = input().split()
# print(int(a)+int(b))d
# def decorator(func):
#     def wrapper():
#         orig = func()
#         return orig.upper() + "world"
#     return whapper



# @decorator
# def say_hello():
#     return "Hello"

# print(say_hello())
# class Characater:
#     def_init_(self,xp,st,mg) -> None:
# class Character:
#     def __init__(self,xp,st,mg) -> None:
#         self.xp = xp
#         self.st = st
#         self.mg = mg 
 
     
# class Warrior(Character):
#     def attack(self):
#         print("slash sword")
 
# class Mage(Character):
#     def attack(self):
#         print("fireball")
#     from abc import ABC,abstractmethod hod
# class Character(ABC): 
#     @abstractmethod #этот декоратор делает обязательным создание этой функции/метода  
#     def attack(self): 
#         pass 
 
#     @abstractmethod 
#     def walk(self): 
#         pass 
 
 
# class Warrior(Character): 
#     def walk(self): 
#         print("warrior walk") 
     
#     def attack(self): 
#         print("warrior attack") 
 
# class Mage(Character): 
#     def walk(self): 
#         print("Mage walk") 
     
#     def attack(self): 
#         print("Mage attack")

# from abc import ABC,abstractmethod 
 
# class instruments(ABC): 
#     @abstractmethod 
#     def __init__(self,xp,st,mg): 
#         pass 
     
#     @abstractmethod 
#     def attack(self): 
#         pass 
     
# class guitar(Character): 
#     def func(self): 
#         print("slash sword") 
     
# g = Warrior() 
 
# class violin(Character): 
#     def attack(self): 
#         print("fireball")

#         class piano(Character): 
#     def attack(self): 
#         print("fireball")
# from abc import ABC, abstractmethod


# class A(ABC):
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price

#     @abstractmethod
#     def play(self):
#         pass


# class ABM(A):
#     def B(self):
#         return f"{self.title} CGYRUWNKWFHNKDK."

#     def C(self):
#         return f"{self.title} GFBYHNHJBFGN."
    
#     def D(self):
#         return f"{self.title} GYBGVCFGBHVB."

#     def E(self):
#         return f"{self.title} FTUGYHBGJVHF."

    


# class F(A):
#     def G(self):
#         return f"{self.title} ABCDEFG."

#     def H(self):
#         return f"{self.title} HIJKLMNOP."
    
#     def I(self):
#         return f"{self.title} ADFGH."

#     def J(self):
#         return f"{self.title} ASDFGH."



# class K(A):
#     def L(self):
#         return f"{self.title} ASDFGHJL."

#     def M(self):
#         return f"{self.title} ZSDRTYUIOPL."
    
#     def N(self):
#         return f"{self.title} SDFGHJKOJLJHBNMKJH."

#     def O(self):
#         return f"{self.title} HGHIJJLHKGHCFIYUOGHJVGFDRYTIG."

# violin = A("Stradivarius", 15000)
# guitar = F("Fender", 1200)
# piano = K("Yamaha", 5000)
# class Person:
#     population = 0
#     def init(self,name,age):
#         self.name = name
#         self.age = age
#         self.hobbies = []
#         Person.population += 1
#     def str(self):
#         return f"{self.name}"
    
#     def len(self):
#         return len(self.hobbies)
    
#     def add(self,other):
#         self.hobbies.append(other)
#         return self

#     def sub(self,other):
#         if other in self.hobbies:
#             self.hobbies.remove(other)
#             return self
    
# obj = Person("Bob",25)
# print(obj)
# print(len(obj))
# obj = obj + "fikjwjodk" 
# class Point:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    # def __add__(self, other):
    #     if isinstance(other, Point):
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if isinstance(other, Point):

#             return Point(self.x + other.x, self.y + other.y)
#     def __call__(self):
#         print(self.x,self.y)
#     def __bool__(self):
#         if self .x and self.y:
#             return True
#        щ

print("hello grigoriy")












































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































