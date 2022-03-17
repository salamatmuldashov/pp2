import os
path = '/Users/salamatmuldashov/Desktop/PP2(python)/Lab6/dirandfiles/123456.txt'
if os.access(path,os.F_OK):
    os.remove(path)
else:
    print("File does not exist")
