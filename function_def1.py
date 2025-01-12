a="fahad"

def name():
    print("my name is "+ a)
name()


def second(s):
    print("my name is"+ s)
value="asus"

second(value)
#my name is fahad
#my name isasus
   

def twoarg(dep,year):
    print("depis"+ dep+" year is "+year)

twoarg("it","forth")
#depisit year is forth
#it will replace dep and forth  will replACE YEAR

def multi(*val):
    print("first val  is "+val[0]+" second val is "+val[1])
multi("fahad","rahman")
