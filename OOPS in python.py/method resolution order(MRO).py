class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f"{self.brand} {self.model}"
    def make_a_call(self,phone_num):
        return f"{phone_num} is calling"
#INHERITANCE
class Smartphone(Phone):
    def __init__(self,brand,model,price,rear_camera,RAM):
        #2 ways
        Phone.__init__(self,brand,model,price)
        super().__init__(brand,model,price)
        self.rear_camera=rear_camera
        self.RAM=RAM

#multilevel inheritance:Phone->Smartphone->Flashipphone
class Flashipphone(Smartphone):
    def __init__(self,brand,model,price,rear_camera,RAM,front_camera):
        super().__init__(rear_camera,RAM)
        self.front_camera=front_camera
'''every class has its own method resolution order'''
#MRO
print(help(Smartphone))
#****builtin.ojects is a built-in class which inherites all the other classes in python***
