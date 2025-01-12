class first:
    def display(self):
        print("first")

class second:
    def display(self):
        print("second")

class third(second,first):
    def display(self):
        print("third")

x=third()
#x.displaythird()
x.display() 