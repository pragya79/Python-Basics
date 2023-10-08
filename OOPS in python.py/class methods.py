class Person:
    count_instance=0#this is a class variable
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name=last_name
        self.age=age
    @classmethod
    def count_instances(cls):#here count_instances is a class method hence we'll give class as an argument just  like we passed self in instance methods
        return f"You have created {cls.count_instance} no. of instances of {cls.__name__} class"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def above_18(self):
        return self.age>18
p1=Person("Pragya","Sharma",18)
p2=Person("Prateek","Sharma",22)
print(p1.count_instances())#called using instance
print(Person.count_instances())#called using class

