#types of error
'''name error,
identation error(due to spaces),
type error(string+int),
syntax error'''
#RAISE TYPERROR
a=input("enter x: ")
b=input("enter y: ")
def add(a,b):
    if(type(a) is int and type(b) is int):
        return a+b
    else: 
        raise TypeError("you have entered wrong datatype")

print(add(a,b))