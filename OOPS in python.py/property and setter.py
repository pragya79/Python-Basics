class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        # if price>0:
        #     self.price=price
        # else:
        #     self.price=0
        #alternate of if-else
        self.price=max(price,0)#so that input price is either positive or zero
        self.details=f"{self.brand} {self.model} is of Rs {self.price}"
    def make_a_call(self,phone_num):
        print(f"calling {phone_num}")
    def full_name(self):
        print(f"{self.brand} {self.model}")
