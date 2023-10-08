class person:
    name=input("enter name: ")
    age=int(input("enter age: "))
    def info(self):
        print(f"{self.name}'s age is {self.age}")

a=person()#"a" is object of class person
# print(a.name)
a.info()