class Phone:
    #encapsulation meaning saara useful data ek hi capsule mein define kar dena
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self._price=price#here _price represents private name for developers(in python nothing is private)
        self.__price=price
    def make_a_call(self,phone_num):
        print(f"calling {phone_num}")
    def full_name(self):
        print(f"{self.brand} {self.model}")
p1=Phone("Samsung","52A",34000)
print(p1._price)
print(p1.price)#both will give same output

#__price is not a convention--->Name Mangling
# print(p1.__price)#this line will give error='Phone' object has no attribute '__price'
print(p1.__dict__)
#output={'brand': 'Samsung', 'model': '52A', 'price': 34000, '_price': 34000, '_Phone__price': 34000}
'''it implies python compiler changed __price into _Phone__price'''
print(p1._Phone__price)

#ABSTRACTION--->hiding all the complexity of the code
#for ex:
l=[5,9,0,2,3]
l.sort()#here we don't know anything about the algorithm behind the sort method...in python tim sorting is used
print(l)
'''jab tak encapsulation nhi ho sakti tab tk abstraction possible nhi h'''