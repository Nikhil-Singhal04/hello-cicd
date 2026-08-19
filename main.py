import os
print(os.getcwd())
print(os.listdir(os.getcwd()))
cur=os.getcwd()
for i in os.listdir(cur):
    if os.path.isfile():
        print(i)
print(len(os.listdir(os.getcwd())))
