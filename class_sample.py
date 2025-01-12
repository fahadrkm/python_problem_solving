class Mysample:
    def hello(self,n):
        self.name=n
        print("hi "+n)
    def print_name(self):
        print("second",self.name)
x=Mysample()
name="nikil"
x.hello(name)
x.print_name()



