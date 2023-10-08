#Decorators enhances the functionality of other functions
#------>code bina change kare function ki functionalty badha dena
def decorator_func(any_func):
    def wrapper_func():
        print("this is awesome function!")
        any_func()
    return wrapper_func()
def func1():
    print("this is func1")

def func2():
    print("this is func2")
var=decorator_func(func1)
# var()
var=decorator_func(func2)
# var()

#OTHER WAY OF CALLING DECORATOR FUNCTION
@decorator_func
def func3():
    print("this is func3")
func3