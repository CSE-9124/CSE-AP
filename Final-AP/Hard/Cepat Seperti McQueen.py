def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    else:
        while x1 < x2:
            x1 += v1
            x2 += v2

        if x1 == x2:
            return "YES"
        else:
            return "NO"


arr = list(map(int, input().split()))
print(kangaroo(arr[0], arr[1], arr[2], arr[3]))