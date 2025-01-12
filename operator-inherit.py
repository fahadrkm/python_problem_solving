class sample:
    def setname(self,name):
        self.name=name
    def __add__(self,other):
       name=self.name+other.name
       return name

firstname=sample()
secondname=sample()

firstname.setname("smart ")
secondname.setname("boys")

fullname=firstname+secondname

print(fullname)
#here it will print smart boys