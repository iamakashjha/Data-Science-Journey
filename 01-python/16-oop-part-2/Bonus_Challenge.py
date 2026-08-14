class shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

class rectangle(shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class circle(shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shapes = [
    rectangle("Rectangle", 10, 5),
    circle("Circle", 7)
]

for shape in shapes:
    print(shape.area())