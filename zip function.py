#user=("user1","user2","user3")
#names=("pragya","pallavi","shivangi")
#zip=(("user1","pragya"),("user2","pallavi"),("user3","shivangi"))
user=("user1","user2","user3")
names=("pragya","pallavi","shivangi")
print(zip(user,names))#output--->zip object
zip=list(zip(user,names))
print(zip)