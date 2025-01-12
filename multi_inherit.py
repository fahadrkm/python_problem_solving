class first:
    def displayfirst(self):
        print("first")

class second:
    def displaysecond(self):
        print("second")

class third(first,second):
    def displaythird(self):
        print("third")

x=third()
x.displaythird()
x.displaysecond()
