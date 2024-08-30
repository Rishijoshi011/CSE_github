
# ! Single inheritence

from abc import abstractmethod

class Base(object):
    num = 11

    @classmethod
    def greet(cls):
        print("Base class")
    
class Derived(Base): 
    @classmethod
    def greet2(cls):
        print("Derived class", Base.num)
    
    
de = Derived() 
de.greet()

# ! multiple

class Base1(object):
    @classmethod
    def show(cls):
        print("base1 class")
    
class Base2(object):
    @classmethod
    def show(cls):
        print("base2 class")
    
class Derived2(Base1, Base2):
    
    @classmethod
    def show(cls):
        Base1.show()
        Base2.show()

de2 = Derived2()
de2.show()

# ! Multilevel

class Vehicle(object):
    tiers = ''

    @abstractmethod
    def show(self):
        pass
    
class Car(Vehicle):
    tiers = 4
    
    @classmethod
    def show(cls):
        print("Car class: " , cls.tiers)
        
class Manual(Car):
    Engine = "V12 Twin Turbo"
    
    @classmethod
    def show(cls):
        super().show()
        print(f"Manual class: {cls.Engine}")
        
# ! hybrid 

class EV(Car):
    Engine = "Dark matter"

    @classmethod
    def show(cls):
        super().show()
        print(f"EV class: {cls.Engine}")
        
m = Manual()
ev = EV()
m.show()
ev.show()
