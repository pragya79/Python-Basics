# def calculategmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)
# calculategmean(9,8)
#variable length arguments
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is: ",sum/len(numbers))
average(3,9)
