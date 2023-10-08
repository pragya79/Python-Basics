f=open("pragya.py","r")
f2=open("pragya.py","a")
text=f.read()
print(text)
text2=f2.write("hello")
print(f2)
with open("pragya.py","a"):
    f2.write("hi this is another method")
f.close()