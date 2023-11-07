class Human:
    def __init__(self, name, position, speed):
        self.name = name
        self._position = position
        self._speed = speed

    def movement(self, arah):
        if arah == "L":
            self._position -= self._speed
        elif arah == "R":
            self._position += self._speed

    def getPosition(self):
        return self._position

    def setPosition(self, position):
        self._position = position

    def getSpeed(self):
        return self._speed

    def setSpeed(self, speed):
        self._speed = speed


class Hero(Human):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._power = 15
        self._health = 400
        self._armor = 15

    def attack(self, target):
        target.setHealth(target.getHealth() - self._power)

    def getPower(self):
        return self._power

    def setPower(self, power):
        self._power = power

    def getHealth(self):
        return self._health

    def setHealth(self, health):
        self._health = health

    def getArmor(self):
        return self._armor

    def setArmor(self, armor):
        self._armor = armor


class Warrior(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._power = 32
        self._armor = 45
        target.setHealth(target.getHealth() - self._power)


class Assassin(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._power = 42
        self._speed = 7
        target.setHealth(target.getHealth() - self._power)


class Support(Hero):
    def __init__(self, name, position, speed):
        super().__init__(name, position, speed)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target.setHealth(target.getHealth() + 150)


warrior = Warrior("bambang", 10, 0)
assassin = Assassin("joko", 25, 0)
support = Support("udin", 30, 0)

# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)

# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())
