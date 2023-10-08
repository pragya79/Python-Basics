#Dictionary is an ordered collection of data 
'''syntax=
dict_name={
    key=value,
    key=value
}'''
dic={
   "Pragya":"IT",
   "Raghav":"IT",
   "Hridayesh":"CSE"
}
print(dic["Hridayesh"])
# print(dic['akshat'])#this line will give error as there is no akshat in dic
print(dic.get('akshat'))#this line will not give error and prints none
print(dic.items())