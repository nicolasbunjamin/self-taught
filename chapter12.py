from math import pi


class Apple:
    def __init__(self, w, c, t, s):
        self.weight = w
        self.color = c
        self.taste = t
        self.source = s
        self.recs.append((self.w))


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (pi * self.radius ** 2)


# Challenge 3
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height * 0.5)


class Hexagon:
    def __init__(self, s):
        self.side = s

    def perimeter(self):
        return (6 * self.side)


my_apple = Apple(3, "red", "sweet", "Australia")

print("Challenge 1!")
print(my_apple.weight)
print(my_apple.color)
print(my_apple.taste)
print(my_apple.source)
print()

circle_a = Circle(5)

print("Challenge 2!")
print("Radius: {}".format(circle_a.radius))
print("Circle Area: {}".format(circle_a.area()))
print()

triangle_b = Triangle(4, 5)

print("Challenge 3!")
print("Triangle Area: {}".format(triangle_b.area()))
print()

hexagon_c = Hexagon(6)

print("Challenge 4!")
print("Perimeter: {}".format(hexagon_c.perimeter()))
print()
