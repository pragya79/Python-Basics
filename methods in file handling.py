#METHOD 1---->readline()
f=open("myfile.txt","r")

while True:
    line=f.readline()
    print(line)
    if not line:
        break
    # print(line)