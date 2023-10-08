import time
timestamp=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)
if(hour>=0 and hour<12):
    print("Good Morning!!")
elif(hour>=12 and hour<16):
    print("Good afernoon!!")
if(hour>=16 and hour<=20):
    print("Good evening!!")
minute=int(time.strftime('%M'))
print(minute)
second=int(time.strftime('%S'))
print(second)