import os
path = "/Users/salamatmuldashov/Desktop/PP2(python)"

print("Existence: " + str(os.access(path,os.F_OK)))
print("Readability: " + str(os.access(path,os.R_OK)))
print("Writeability: " + str(os.access(path,os.W_OK)))
print("Executability: " + str(os.access(path,os.X_OK)))
