class Square:
    square_list = []
    counter = 0

    def __init__(self, side):
        Square.counter += 1
        self.id = Square.counter
        self.side = side
        self.square_list.append((self.id, self.side))

    def image(self):
        print("{} by {} by {} by {}".format(self.side, self.side, self.side, self.side))


my_square = Square(4)
your_square = my_square
their_square = (4)


print(my_square.id)
my_square.image()

print(your_square is my_square)
print(their_square is my_square)
