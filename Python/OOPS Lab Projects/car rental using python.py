k=int(input("Total cars initially in stock are: "))
class car:
    def __init__(self,stock):
        self.stock=stock
    def displaystock(self):
        print("Total cars in stock: ",self.stock)
    def rentforcar(self,quantity):
        if(quantity<=0):
            print("Please enter a valid quantity")
        elif(quantity>self.stock):
            print("Sorry!! Out of stock")
        else:
            print("Total Price: ",quantity*k)
            print("Cars remaining in stock: ",self.stock-quantity)
while True:
    
    obj=car(k)
    choise=int(input('''
    1 Total Stock
    2 Enter quantity of cars for rent
    3 Exit
    '''))
    if(choise==1):
        obj.displaystock()
    elif(choise==2):
        n=int(input("Enter quantity of cars for rent: "))
        obj.rentforcar(n)
