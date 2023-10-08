#if we entered any string which in 'a' this code will give error hence our imp lines od code will also not get print that's why we use "try" keyword

a=input("enter a number: ")
print(f"multiplication table of {a} is: ")

try:
    for i in range(1,11):
     print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
   print(e)
   print("sorry some error occured")

#now these lines will run irrespective of whether above code is correct or not
print("some imp lines of code")
print("end of program")

try:
   num=int(input("enter number: "))
   a=[7,9,8,2]
   print(a[num])
except ValueError:
   print("Input is not integer")

except IndexError:
   print("Invalid index")