x = int(input())
for i in range(1, x + 1):
    print(" " * (x - i) + "#" * i)

# x = int(input())
# for i in range(x):
#     numbers = ' '.join(str(j + 1) for j in range(i + 1))
#     print(numbers.rjust(x * 2 - 1))
