a=int(input("enter any number between 5 & 9: "))
if(a<5 or a>9):
    raise ValueError("enter value between 5 and 9")