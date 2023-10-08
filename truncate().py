with open("myfile.txt","w") as f:
    f.write("We are truncating")#It will reduce the number of characters in our original file
    f.truncate(10)
with open("myfile.txt","r") as f:
    print(f.read())