class TeamMemeber:
    year=2024
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
    def display(self):
        print(str(TeamMemeber.year))
        print(self.name)
        print(str(self.age))
        print(self.place)
        print("----------------------")


x=TeamMemeber("fahad",24,"kannur")
y=TeamMemeber("nihal",24,"city")



x.display()
y.display()

TeamMemeber.year=TeamMemeber.year+1

print("------------_______----")
x.add_age()
y.add_age()

x.display()
y.display()



  