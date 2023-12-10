import os

class Human:
    def __init__(self, Name, Age, Gender):
        self.Name = Name
        self.__Age = int(Age)
        self._Gender = Gender

        def get_Age(self):
            return self.__Age
        def get_Gender(self):
            return self._Gender
        
        def set_Age(self, New_Age):
            self.__Age = New_Age
        def set_Gender(self, New_Gender):
            self._Gender = New_Gender

class Titan(Human):
    def __init__ (self, Name, Age, Gender):
        super().__init__(Name, Age, Gender)
        self.Attack = 0
        self.Defense = 0
        self.Speed = 0
        self.Leadership = 0
        self