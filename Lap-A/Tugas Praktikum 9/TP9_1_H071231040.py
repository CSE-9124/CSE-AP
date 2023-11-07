# Soal 1 : Membuat class Human, Warrior, Assassin, dan Support
import os
os.system('cls')

# Class Grandparent
class Human:
    def __init__(self, name, pos_x, speed):
        self.Name = name
        self.__Position = int(pos_x)
        self._Speed = int(speed)

    # Method
    def movement(self, arah):
        if arah.upper() == 'L':
            self.__Position -= self._Speed
        elif arah.upper() == 'R':
            self.__Position += self._Speed

    # Getter    
    def get_position(self):
        return self.__Position
    def get_speed(self):
        return self._Speed
    
    # Setter
    def set_position(self, position):
        self.__Position = position
    def set_speed(self, speed):
        self._Speed = speed

# Class Parent
class Hero(Human):
    def __init__(self, name, pos_x, speed):
        super().__init__(name, pos_x, speed)
        self._Power = 15
        self._Health = 400
        self._Armor = 15
        self._Speed = 3

    # Method
    def attack(self, target):
        target._Health -= self._Power

    # Getter
    def get_power(self):
        return self._Power
    def get_health(self):
        return self._Health
    def get_armor(self):
        return self._Armor
    def get_speed(self):
        return self._Speed

    # Setter
    def set_power(self, power):
        self._Power = power
    def set_health(self, health):
        self._Health = health
    def set_armor(self, armor):
        self._Armor = armor  
    def set_speed(self, speed):
        self._Speed = speed

# Class Child
class Warrior(Hero):
    def __init__(self, name, pos_x, speed):
        super().__init__(name, pos_x, speed)
        self._Power = 26
        self._Armor = 30

    # Method
    def special(self, target):
        self.set_power(32)
        self.set_armor(45)
        target._Health -= self._Power

class Assassin(Hero):
    def __init__(self, name, pos_x, speed):
        super().__init__(name, pos_x, speed)
        self._Power = 35
        self._Speed = 4

    # Method
    def special(self, target):
        self.Speed = 7
        self.set_power(42)
        target._Health -= self._Power

class Support(Hero):
    def __init__(self, name, pos_x, speed):
        super().__init__(name, pos_x, speed)
        self._Health = 500
        self._Armor = 8
        self._Speed = 4

    # Method
    def special(self, target):
        self._Speed = 6
        target._Health += 150


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