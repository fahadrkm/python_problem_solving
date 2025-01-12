n=int(input())
s=int(input())
d=str(s)
App=[]
for i in d:
    App.append(i)
g= list(set(d))
f=sorted(g, key=int)

print(f[-2])