#class is a blueprint that decides how our object will look like
class Person:
    #here __init__ is a constructor having arguments self and attributes like first_name etc
    def __init__(self,first_name,last_name,age):#here self refers to object p1
        #instance variables
        print("Constructor is called first")
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
#pehle constructor call hoga then value print hogi
#each time the objectis created constructor will get called
p1=Person("Pragya","Sharma",18)
print(p1.first_name)
p2=Person("Prateek","Sharma",22)
print(p2.first_name)

#EXERCISE-1
class Laptop:
    def __init__(self,brand,windows):
        self.brand=brand
        self.windows=windows
hp=Laptop("HP","Windows 10")
print(hp.brand,hp.windows)