class Rectangle:


    def __init__(self, length: int, width: int):

        self.length = length
        self.width = width

    def __iter__(self):

        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(5, 3)

# Iterate over the rectangle
for dimension in rect:
    print(dimension)

