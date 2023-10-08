#Operations on sets are same as in maths
s1={1,2,3,2,1,4,3}
s2={2,3,1,5,6,2,7,9}
# print(s1.union(s2))
# print(s1.intersection(s2))
# s1.update(s2)#it means s1 mein s2 wali values bhi le aao
# print(s1)
# s1.intersection_update(s2)
# print(s1)
#SYMMETRIC DIFFERENCE
'''it means values which are not common in both the sets
i.e AUB-A intersection B'''
# s3=s1.symmetric_difference(s2)
# print(s3)

# s1.difference(s2)#just like A-B

print(s1.difference(s2))#element which is present in A but not in B
