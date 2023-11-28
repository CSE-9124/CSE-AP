max_row, max_col = list(map(int, input().split()))

row = 1

while row <= max_row:
    col = 1

    while col <= max_col:
        if col <= row:
            print("#", end=" ")
        else:
            print("*", end=" ")

        col += 1

    print()
    row += 1
