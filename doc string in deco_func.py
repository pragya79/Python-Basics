from functools import wraps

def deco_func(any_func):
    @wraps(any_func)#wraps is a built-in decorator
    def wrapper_func():
        '''this is wrapper func's doc string'''
        print("this is awesome func")
        any_func()
    return wrapper_func
@deco_func
def func():
    '''this is fun's doc string'''
    print("hi pragya!!")
print(func.__doc__)#here it will print wrapper's func doc string
print(func.__name__)#it will print wrapper func name
#to solve this problem we'll import a module functool
