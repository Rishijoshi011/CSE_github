
class Vehicle(object):
    tiers = ''

    @classmethod
    def show(cls):
        print("Vehicle class")
    
class Car(Vehicle):
    tiers = 4
    
    @classmethod
    def show(cls):
        super().show()
        print("Car class: " , cls.tiers)
        
class Manual(Car):
    Engine = "V12 Twin Turbo"
    
    @classmethod
    def show(cls):
        super().show()
        print(f"Manual class: {cls.Engine}")
        
m = Manual()

m.show()