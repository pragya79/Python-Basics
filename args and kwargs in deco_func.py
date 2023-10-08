# def deco_func(any_func):
#     def wrap_func():
#         print("this is awesome func")
#         any_func()
#     return wrap_func
# @deco_func
# def func1(a):
#     print(f"this is func1 with argument {a}")
# func1(9)#it will show error

def deco_func(any_func):
    def wrap_func(*args,**kwargs):
        print("this is awesome func")
        return any_func(*args,**kwargs)#***
    return wrap_func
@deco_func
def func1(a):
    print(f"this is func1 with argument {a}")
func1(9)

@deco_func
def add(a,b):
   return a+b
print(add(2,3))#without dec_func this line will give 5 but with it it gives none
'''for that we have to write return before ***any_func in deco_func'''
