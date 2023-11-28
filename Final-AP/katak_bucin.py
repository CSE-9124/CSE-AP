n = int(input())
frogs = input().split()

if len(frogs) != n:
    print("Panjang Tidak Sama")

else:
    frogs.sort()
    i = 0
    count_same = 0
    while i < n-1:

        if frogs[i] == frogs[i+1]:
            count_same += 1
            i += 2
        else:
            i += 1

    print(count_same)