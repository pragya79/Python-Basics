def outer_func():
    def inner_func():
        print("You are in inner_func")
    return inner_func
var=outer_func()
var()

def outer_func2(msg):
    def inner_func2():
        print(f"Pragya says {msg}")
    return inner_func2
var=outer_func2("Hello!")
var()