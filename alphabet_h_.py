count=5
for i in range(1,count+1):
    for j in range(1,count+1):
        if (j==5 or i==(count+1)//2 or j==1) :
            print('*',end='')
        else:
            print(' ', end='')  
    print('')