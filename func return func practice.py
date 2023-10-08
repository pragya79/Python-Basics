def power(x):
    def cal_power(n):
        return n**x
    return cal_power(n)
n=int(input("enter any number(n): "))
x=int(input("enter power(x): "))
print(power(x))