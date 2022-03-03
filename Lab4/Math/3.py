import math
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
parameter = sides * length
apothem = length / (2 * (math.tan(math.pi/sides)))
area = (parameter * apothem)/2
print("The are of polygon is: " + str(int(area)))



