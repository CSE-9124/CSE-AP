from TP9_1_H071231040 import Assassin, Warrior, Support

# Objek
warrior = Warrior("Bambang", 10, 5)
assassin = Assassin("Joko", 25, 5)
support = Support("Udin", 30, 5)


# Memanggil Metode class Human
print(f'Position (before) : {warrior.get_position()}')   # sebelum
warrior.set_speed(5)
warrior.movement('R')
print(f'Position (after)  : {warrior.get_position()}')   # sesudah

print("-"*50)


# Memanggil Metode class Hero
print(f'Health (before)   : {warrior.get_health()}')    # sebelum
assassin.attack(warrior)
print(f'Health (after)    : {warrior.get_health()}')     # sesudah

print("-"*50)


# sebelum
print(f'Warrior (health)  : {warrior.get_health()}')
print(f'Support (speed)   : {support.get_speed()}')
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.get_health())
print("Support (speed): ",support.get_speed())