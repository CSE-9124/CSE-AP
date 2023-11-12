import random
import os

def cls():
    os.system("cls")
def showhealt():
    cls()
    print(f"""
 = = = = = = H E A L T H = = = = = =
{player1.name}: {player1.hp} HP
{player2.name}: {player2.hp} HP
""")

class spawn:
    def __init__(self,name, HP = 0, AP = 0):
        self.name = name
        self.hp = HP
        self.ap = AP

    def attacked(self, apOPS):
        self.hp -= apOPS

    def attacking (self,aptotal):
        return self.ap + aptotal
cls()
print("============== C H A R A C T E R =============\n")

print("ENTER YOUR NAME PLAYER 1 !")
while True:
    player1 = spawn(input("What Is Your Name Challenger? : "), HP= 100, AP = random.randint(20,50))
    print(f"""
======   YOUR STATS   ======
YourName = {player1.name} +
HP = 100 
AP = {player1.ap}
============================
   PRESS ENTER TO CONTINUE
              """)
    if type(input()) == str:
        break
    
            
cls()
print("ENTER YOUR NAME PLAYER 2 !")
while True:
    player2 = spawn(input("What Is Your Name Challenger? : "), HP= 100, AP = random.randint(20,50))
    print(f"""
======   YOUR STATS   ======
YourName = {player2.name} 
HP = 100 
AP = {player2.ap}
============================
   PRESS ENTER TO CONTINUE
              """)
    if type(input()) == str:
        break

cls()
print("==================F I G H T===================\n")

showhealt()
gofirst = random.randint(0,1)
while player1.hp > 0 and player2.hp > 0:
    if gofirst == 1:
        showhealt()
        print(f"{player1.name} You have the chance to attack \n")
        if input("type 'ATTACK' to attack your enemy!  : \n") == "ATTACK":
            bonus = random.randint(1,25)
            player2.attacked(player1.attacking(bonus))
            cls()
            showhealt()
            print (f"{player1.name} ATTACK {player2.name} dealing {bonus+player1.ap} DMG !!!\n")

        else:
            showhealt()
            print("You missed!!!, NOW the enemy has the chance to attack you\n")
            player1.attacked(player2.attacking(0))
            cls()
            showhealt()
            print (f"{player2.name} ATTACK {player1.name} dealing {bonus+player1.ap} DMG !!!\n")
            

        gofirst = 0

    elif gofirst == 0:
        showhealt()
        print(f"{player1.name} You have the chance to attack  : \n")
        if input("type 'ATTACK' to attack your enemy!\n") == "ATTACK":
            bonus = random.randint(1,25)
            player1.attacked(player2.attacking(bonus))
            cls()
            showhealt()
            print (f"{player2.name} ATTACK {player1.name} dealing {bonus+player1.ap} DMG !!!\n")

        else:
            showhealt()
            print("You missed!!!, NOW the enemy has the chance to attack you\n")
            player2.attacked(player1.attacking(0))
            cls()
            showhealt()
            print (f"{player1.name} ATTACK {player2.name} dealing {bonus+player1.ap} DMG !!!\n")

        gofirst = 1
if player1.hp > 0:
    print(f"{player1.name} WIN")
else:
    print(f"{player2.name} WIN")
        
