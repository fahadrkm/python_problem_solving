class BaseClass:
    def __init__(self):
        print('super init')
    def set_name(self,name):
        print("super base set name"+name)
        self.name=name
    
        


class SubClass(BaseClass):

    def __init__(self):
        super().__init__()
        print("subclass init")


    def set_name(self,name):
        super().set_name(name)
        print("subclss set nme"+name)
        self.name=name


    def welcome(self,n):
        print("welcome "+n)

    def display_name(self):
        print("displyname"+self.name)
    

y=SubClass()
y.welcome("frk")
y.set_name("fahadrahman")
y.display_name() 