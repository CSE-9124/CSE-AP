max_bulat = int(input())
max_plus = int(input())

bulat = 1

while bulat <= max_bulat:
    plus = 1

    while plus <= max_plus:
        
        if plus <= bulat:
            print("o", end=" ")
        else:
            print("+", end=" ")

        plus += 1

    print()
    bulat += 1
