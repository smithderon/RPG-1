import random

class Char():
    def __init__(self, name):
        self.name = name
        self.powah = random.randint(1000, 99999)
        self.hp = random.randint(50000, 99999)
    def attack(self, object):
        if self.hp > 0 and object.hp > 0:
            object.hp -=  self.powah
            print(f"Creda deals {self.powah} damage!")
    def alive(self):
        if self.hp >= 1:
            return self.hp
    def status(self):
        if self.hp >= 0:
            print(f"{self.name} has {self.hp} remaining.")
        elif self.hp <= 0:
            print(f"{self.name} has been defeated.")


class Hero(Char):
    def __init__(self, name):
        self.name = name
        self.powah = random.randint(1000, 99999)
        self.hp = random.randint(50000, 99999)
    def attack(self, object):
        if self.hp > 0 and object.hp > 0:
            object.hp -=  self.powah
            print(f"Creda deals {self.powah} damage!")
    def alive(self):
        if self.hp >= 1:
            return self.hp
    def status(self):
        if self.hp >= 0:
            print(f"{self.name} has {self.hp} remaining.")
        elif self.hp <= 0:
            print(f"{self.name} has been defeated.")

class Enemy(Char):
    def __init__(self, name):
        self.name = name
        self.powah = random.randint(500, 9999)
        self.hp = random.randint(100000, 999999)
    def attack(self, object):
        if self.hp >= 0:
            object.hp -= self.powah
            print(f"{self.name} deals {self.powah} damage to {object.name}")
    def alive(self):
        if self.hp >= 1:
            return self.hp
    def status(self):
        if self.hp >= 0:
            print (f"{self.name} has {self.hp} remaining.")
        elif self.hp <= 0:
            print(f"{self.name} has been defeated.")
        

creda = Hero("Creda")
cicilene = Enemy("Cicilene")


#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def main():

    while cicilene.alive() and creda.alive():
        print(f"""
        Lv.99 {creda.name} with an attack power of {creda.powah}, 
        has encountered a power lv.{cicilene.powah} {cicilene.name}!
        """)
        print()
        print("""
        Battle Menu: 
        """)
        print("1. Fight Creda")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            creda.attack(cicilene)
            if cicilene.alive():
                cicilene.status
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if  cicilene.alive():
            # Goblin attacks hero
            cicilene.attack(creda)
        creda.status()
        cicilene.status()
main()