# file: main.py

# begin: import modules
import os
# end: import modules

# memprint nama OS
print("os name: ", os.name)

# memprint current working directory
print("current working directory: ", os.getcwd())

# memprint absolute path dari directory saat ini
print("absolute path: ", os.path.abspath('.'))

# melisting files dan sub-directory di directory saat ini
print("list directory: ", os.listdir('.'))

# me-rename file
if os.path.isfile("sample.txt") :
    os.rename("sample.txt","renamed.txt")
elif os.path.isfile("renamed.txt") :
    os.rename("renamed.txt","sample.txt")