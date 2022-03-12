import re
s = input()
x = re.findall('[a-zA-Z][^A-Z]*', s)
print(x)

