from re import X


class Shape():
    pass

class Rectangle(Shape):
    def __init__(self,l,w) -> None:
        self.length = l
        self.width = w
    
    def area(self):
        print(self.length * self.width)

l,x = map(int,input().split())
Arectangle = Rectangle(l,x)
Arectangle.area()


        

