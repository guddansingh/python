import os

folder=os.listdir("data")

for folders in folder:
    print(folders)

    print(os.listdir(f"data/{folders}"))

print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())

