import matplotlib.pyplot as plt

# rectangle class
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_area(self):
        return self.width * self.height

    def draw(self):
        rectangle = plt.Rectangle((0, 0), self.width, self.height, facecolor="tab:blue",
                                  edgecolor="tab:blue", linewidth=3)
        plt.gca().add_patch(rectangle)
        plt.axis('equal')
        plt.show()


# square class
class square(rectangle):
    def __init__(self, length):
        self.length = length

    def get_perimeter(self):
        return self.length * 4

    def get_area(self):
        return self.length * self.length

    def draw(self):
        rectangle = plt.Rectangle((0, 0), self.length, self.length, facecolor="tab:blue",
                                  edgecolor="tab:blue", linewidth=3)
        plt.gca().add_patch(rectangle)
        plt.axis('equal')
        plt.show()

r1 = rectangle(5, 10)

print('The perimeter of the rectangle is:', r1.get_perimeter())
print('The area of the rectangle is:', r1.get_area())
r1.draw()

s1 = square(10)

print('The perimeter of the square is:', s1.get_perimeter())
print('The area of the square is:', s1.get_area())
s1.draw()