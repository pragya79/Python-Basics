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

s=Smartphone("OnePlus","5",35000,"500px","64GB")
print(s.full_name())
print(s.make_a_call("8571829300"))