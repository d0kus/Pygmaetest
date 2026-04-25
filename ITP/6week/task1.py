class Rectangle:
 def __init__(self, width, height):
    self.width = width
    self.height = height
    pass
 def area(self):
    return self.width * self.height
    pass
 def perimeter(self):
    return 2 * (self.width + self.height)
    pass
 def is_square(self):
    return self.width == self.height
    pass
 def __str__(self):
    return f'Rectangle {self.width} x {self.height}' if self.width!=self.height else f'Square {self.width} x {self.height}'
 pass
# ---- Test your code ----
r1 = Rectangle(4.0, 6.0)
r2 = Rectangle(5.0, 5.0)
print(r1) # Rectangle: 4.0 x 6.0
print(r1.area()) # 24.0
print(r1.perimeter())# 20.0
print(r1.is_square())# False
print(r2.is_square())# True