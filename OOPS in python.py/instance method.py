#List is a predefined class in python which has methods like pop(),append() etc
#List is a mutable object, which means that you can change the value of the list
class Person:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
    def full_name(self):
        return f"{self.first} {self.last}"
    def is_above_18(self):
        return self.age>=18
p1=Person("Pragya","Sharma",18)
print(p1.full_name())#---->1
#what actually happens
print(Person.full_name(p1))#----->2
#line 1 and 2 will give same output
print(p1.is_above_18())