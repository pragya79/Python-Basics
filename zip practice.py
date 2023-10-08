l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
#to return avg of each corresponding element of list i.e (1+4+7)/3,(2+5+8)/3 etc
for triplet in zip(l1,l2,l3):
    avg=sum(triplet)/len(triplet)
    print(avg)