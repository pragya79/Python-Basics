class circle:
    pi=3.14#class variable
    def __init__(self,radius):
    #as pi is now class variable not instance variable henceno need to write self.pi instead write circle.pi
        # self.pi = pi
        self.radius = radius
    def cal_circum(self):
        return 2*circle.pi*self.radius
    def cal_area(self):
        return circle.pi*self.radius*self.radius
#for every circle value of pi is same i.e 3.14
c=circle(12)
print(c.cal_circum())
print(c.__dict__)