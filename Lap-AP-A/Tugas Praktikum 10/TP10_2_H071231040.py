from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def sound(self):
        pass

    def get_Name(self):
        return self.__name
    
    def set_Name(self, new_name):
        self.__name = new_name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def sound(self):
        return "Meow!"

# Interface
def animal_sound(animal):
    return animal.sound()

# Objek
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f'Anjing bernama {dog.get_Name()} mengeluarkan suara {animal_sound(dog)}')
print(f'Kusing bernama {cat.get_Name()} mengeluarkan suara {animal_sound(cat)}')



# class Human:
#     def __init__(self, Name, Age, Gender):
#         self.Name = Name
#         self.__Age = int(Age)
#         self._Gender = Gender

#         def get_Age(self):
#             return self.__Age
#         def get_Gender(self):
#             return self._Gender
        
#         def set_Age(self, New_Age):
#             self.__Age = New_Age

# class Titan(Human):
#     def __init__ (self, Name, Age, Gender):
#         super().__init__(Name, Age, Gender)
#         self._Power = int