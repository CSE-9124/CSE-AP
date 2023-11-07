# Soal Nomor 2 :
# CARA 1 :
First = input('Masukkan Input Pertama : ')
Second = input('Masukkan Input Kedua : ')
Third = input('Masukkan Input Ketiga : ')

print()
if First == 'vertebrado':
    if Second == 'ave':
        if Third == 'carnivoro':
            print('aguia')
        elif Third == 'onivoro':
            print('pomba')
        else:
            print('Invalid Input')
    elif Second == 'mamifero':
        if Third == 'onivoro':
            print('homem')
        elif Third == 'herbivoro':
            print('vaca')
        else:
            print('Invalid Input')
    else:
        print('Invalid Input')
elif First == 'invertebrado':
    if Second == 'inseto':
        if Third == 'hematofago':
            print('pulga')
        elif Third == 'herbivoro':
            print('lagarta')
        else:
            print('Invalid Input')
    elif Second == 'anelideo':
        if Third == 'hematofago':
            print('sanguessuga')
        elif Third == 'onivoro':
            print('minhoca')
        else:
            print('Invalid Input')
    else:
        print('Invalid Input')
else:
    print('Invalid Input')

# # CARA 2 :
# Pertama = input('Masukkan Input Pertama : ')
# # daftar_Pertama = ['vertebrado','invertebrado']
# # if Pertama not in daftar_Pertama:
# #     print('Invalid input')
# #     exit()
# Kedua = input('Masukkan Input Kedua : ')
# # daftar_Kedua = ['ave','mamifero','inseto','anelideo']
# # if Kedua not in daftar_Kedua:
# #     print('Invalid input')
# #     exit()
# Ketiga = input('Masukkan Input Ketiga : ')
# # daftar_Ketiga = ['carnivoro','onivoro','herbivoro','hematofago']
# # if Ketiga not in daftar_Ketiga:
# #     print('Invalid input')
# #     exit()

# match Pertama:
#     case 'vertebrado':
#         match Kedua:
#             case 'ave':
#                 match Ketiga:
#                     case 'carnivoro':
#                         print('aguia')
#                     case 'onivoro':
#                         print('pomba')
#                     case _:
#                         print('Invalid input')
#             case 'mamifero':
#                 match Ketiga:
#                     case 'onivoro':
#                         print('homem')
#                     case 'herbivoro':
#                         print('vaca')
#                     case _:
#                         print('Invalid input')
#             case _:
#                 print('Invalid input')
#     case 'invertebrado':
#         match Kedua:
#             case 'inseto':
#                 match Ketiga:
#                     case 'hematofago':
#                         print('pulga')
#                     case 'herbivoro':
#                         print('lagarta')
#                     case _:
#                         print('Invalid input')
#             case 'anelideo':
#                 match Ketiga:
#                     case 'hematofago':
#                         print('sanguessuga')
#                     case 'onivoro':
#                         print('minhoca')
#                     case _:
#                         print('Invalid input')
#             case _:
#                 print('Invalid input')
#     case _:
#         print('Invalid input')    