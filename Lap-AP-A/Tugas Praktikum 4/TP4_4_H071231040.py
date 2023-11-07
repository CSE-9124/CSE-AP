# CARA 1: Menggunakan Fungsi abs()
def catAndMouse(catA, catB, mosC):
    A = abs(mosC - catB)
    B = abs(mosC - catA)

    if A > B :
        return "Cat A"
    elif B > A :
        return "Cat B"
    else:
        return "Mouse C"
    
catA = int(input('Cat A : '))
catB = int(input('Cat B : '))
mosC = int(input('Mouse C : '))
print(catAndMouse(catA=catA, catB=catB, mosC=mosC))


# CARA 2: Menggunakan If-Else
def catAndMouse(catA, catB, mosC):
    if mosC > catA:
        A = -(mosC - catB)
    else:
        A = (mosC - catB)
    
    if mosC > catB:
        B = -(mosC - catA)
    else:
        B = (mosC - catA)

    if A > B:
        return "Cat A"
    elif B > A :
        return "Cat B"
    else:
        return "Mouse C"

KucingA = int(input('Cat A : '))
KucingB = int(input('Cat B : '))
TikusC = int(input('Mouse C : '))
print(catAndMouse(KucingA, KucingB, TikusC))


# CARA 3: Menggunakan Pangkat 2
def catAndMouse(catA, catB, mosC):
    A = (mosC - catB)**2
    B = (mosC - catA)**2

    if A > B :
        return "Cat A"
    elif B > A :
        return "Cat B"
    else:
        return "Mouse C"

Tom = int(input('Cat A : '))
Neko = int(input('Cat B : '))
Jerry = int(input('Mouse C : '))
print(catAndMouse(catA=Tom, catB=Neko, mosC=Jerry))