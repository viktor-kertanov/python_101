import math

class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    def __str__(self):
        return (f"Объект Circle: радиус {self.radius}. Центр: ({self.x, self.y})")

    def __len__(self):
        return int(self.radius * 2 * math.pi)


circle = Circle(10, 0, 0)

print(type(circle))

circle_represenation = str(circle)
print(circle_represenation)

a = [10, 20, 30]
a_representation = str(a)
print(a_representation, type(a_representation))

print(len(circle))


