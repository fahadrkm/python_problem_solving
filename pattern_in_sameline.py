count = 5
for i in range(1, count + 1):
    for j in range(1, count + 1):
        if j == 1 or j == count or i == (count + 1) // 2:  # 'H' Pattern
            print('*', end='')
        else:
            print(' ', end='')

    print('   ', end='')  # Space between 'H' and 'I'

    for j in range(1, count + 1):
        if i == 1 or i == count or j == (count + 1) // 2:  # 'I' Pattern
            print('*', end='')
        else:
            print(' ', end='')

    print()  # Move to the next line after each row
