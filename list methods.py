lovetriangle=["Raghav","Pragya"]
# lovetriangle.append("Priyanshu")
# print(lovetriangle[0::2])
# lovetriangle.sort(reverse=True)
# print(lovetriangle)
# lovetriangle.reverse()
# print(lovetriangle)
nothing=lovetriangle#nothing is another listname--->list can be changed
nothing.append("Adhyan")
print(nothing)
nothing=lovetriangle.copy()#makes another copy of list
print(nothing)
nothing.insert(2,"Hridayesh")
print(nothing)
nothing.extend(lovetriangle)#combines the 2 lists---->lovetriangle ko nothing ke end me daaldo
print(nothing)
print(nothing.count("P"))