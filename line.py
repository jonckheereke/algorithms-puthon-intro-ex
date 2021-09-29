import math

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def lengthLine(self):
        return math.sqrt(squared(self.point2.get_x() - self.point1.get_x()) + squared(self.point2.get_y() - self.point1.get_y()))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x (self):
        return self.x
    
    def get_y (self):
        return self.y
        
def squared(n):
    return n * n

point1 = Point(2, 1)
point2 = Point(8, 12)

line = Line(point1, point2)
print("Length of the line is: ", line.lengthLine())