with open("myfile.txt","r") as f:
    print(type(f))
    #moves to the 10th byte in the file
    # f.seek(0)
    print(f.tell())
    data=f.read(6)#reads next 6 bytes
    print(data)