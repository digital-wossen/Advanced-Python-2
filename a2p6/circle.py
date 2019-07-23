# JTSK-350112
# a2 6.py
# Wossen Hailemariam
# w.haillemarim@jacobs-university.de



import math


class Circle(object):
    "class of circle"
    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color
        

    def getRadius(self):
        "returns radius"
        return self.__radius
    
    def setRadius(self, radius = 1.0):
        "sets radius"
        self.__radius = radius

    def getColor(self):
        "returns color"
        return self.__color

    def setColor(self, color = "red"):
        "sets color"        
        self,__color = color

    def getArea(self, radius):
        "getting area pi r square"
        return math.pi*radius*radius

    def getPerimeter(self, radius):
        "getting perimere 2 pi r"
        return math.pi*2*radius

    def __add__(self, other):
        "overloading addition"
        return self.getArea(self.__radius) + other.getArea(other.__radius)

    def __sub__(self, other):
        "overloading subtraction"
        return self.getArea(self.__radius) - other.getArea(other.__radius)
        
    def __str__(self):
        """returns string representation"""
        return "Radius:" + str(self.__radius) + "\nColor:" + self.__color +\
            "\nArea:" + str(self.getArea(self.__radius)) + "\nPerimeter:" + \
                str(self.getPerimeter(self.__radius))

