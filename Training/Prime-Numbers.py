def primenumber(z):
    if z <= 1:
        return f'{z} is not a Prime Number'
    else:
        for i in range(2, z):
            if z % i == 0:
                return f'{z} is not a Prime Number'

    return f'{z} is a Prime Number'

print(primenumber(5))