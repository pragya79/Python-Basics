numbers=[1,2,3,4]
def square(a):
    return a**2
list=[square(1),square(2),square(3)]
print(list)
square=lambda s:s**2

#list comprehension
square_new=[i**2 for i in numbers]
print(square_new)

#only map(func_name,iterable)-----> gives object
squares=list(map(square,numbers))
print(squares)