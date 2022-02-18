from cmath import pi

def Volume(radius):
    x = (4/3*pi) * (radius**3)
    print(x)

radius = float(input())
Volume(radius)



