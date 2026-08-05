# Create a Book class.

# Attributes:

# Title
# Author
# Price

# Methods:

# Display book details
# Check if the book is expensive (price > ₹1000)

# Create three book objects and test the methods.

class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")

    def is_expensive(self):
        return self.price > 1000

book1 = book("The Great Gatsby", "F. Scott Fitzgerald", 1200)
book2 = book("To Kill a Mockingbird", "Harper Lee", 800)
book3 = book("1984", "George Orwell", 1500)

book1.display_details()
print(f"Is Expensive: {'Yes' if book1.is_expensive() else 'No'}")
print()
book2.display_details()
print(f"Is Expensive: {'Yes' if book2.is_expensive() else 'No'}")
print()
book3.display_details()
print(f"Is Expensive: {'Yes' if book3.is_expensive() else 'No'}")
print()




# Create a Rectangle class.

# Attributes:

# Length
# Width

# Methods:

# area()
# perimeter()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(5, 3)
print(f"Area: {rectangle1.area()}")
print(f"Perimeter: {rectangle1.perimeter()}")