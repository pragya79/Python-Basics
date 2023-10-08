#statement written under FINALLY keyword will always get executed
#same thing can happen using print
#but when try and except keyword are used under a function print statement will not run
try:
    a=input("enter number: ")
    l=[1,2,3,4,5]
    print(l[a])
except:
    print("some error occured")
finally:
    print("this statement will always get executed!!")
print("this statement will get executed but not always")

def fun():
    try:
        a=input("enter number: ")
        l=[1,2,3,4,5]
        print(l[a])
    except:
       print("some error occured")
    # finally:
    #     print("this statement will always get executed!!")
    print("this statement will get executed but not always")

x=fun()
print(x)