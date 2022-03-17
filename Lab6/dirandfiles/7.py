from asyncore import read
from copy import copy
import os
file1 = open('123.txt', 'r')
file2 = open('12345.txt', 'w')
for line in file1:
    file2.write(line)


