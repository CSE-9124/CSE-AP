def Hollow_Square(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print('*' * rows)
        else:
            print('*' + ' ' * (rows - 2) + '*')

rows = int(input())
Hollow_Square(rows)