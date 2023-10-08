import os
folder=os.listdir("data")
print(os.getcwd())
os.chdir("/users")
print(os.getcwd())
# print(folder)
# for folder in folder:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))