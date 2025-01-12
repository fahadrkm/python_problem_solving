r=[]
n=int(input())
for i in range(n):
    k=input()
    j=float(input())
    s=[]
    s.append(k)
    s.append(j)
    r.append(s)

grades=sorted(set([student[1] for student in r]))
if len(grades)>2:
    second=grades[1]
    second_student=[student[0] for student in r if student[1]==second]
    print(second_student)

else:
    second=grades[0]
    second_student=[student[0] for student in r if student[1]==second]
    print(second_student)