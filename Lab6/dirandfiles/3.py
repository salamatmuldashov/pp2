import os
path = "/Users/salamatmuldashov/Desktop/PP2(python)"
if os.path.exists(path):
    print("Filename of the given path: "+ str(os.path.basename(path)))
    print("Directory portion of the given path: " + str(os.path.dirname(path)))
else:
    print("Path does not exist")


