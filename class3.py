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
    @classmethod
    def addyear(cls):
        TeamMemeber.year=TeamMemeber.year+1

    


x=TeamMemeber("fahad",24,"kannur")
y=TeamMemeber("nihal",24,"city")



x.display()
y.display()



print("------------_______----")

TeamMemeber.addyear()
TeamMemeber.year=TeamMemeber.year+1
#here 2times years added bcoz 2 commands

x.add_age()
y.add_age()

x.relocate("delhi")
y.relocate('chennai')

x.display()
y.display()

