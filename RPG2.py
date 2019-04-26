import random
"""
Creating a print template for character selection:

"Who would you like to choose?"
__________________________________________
object.name     object.powah     object.sp etc.
"""

class Shop(object):
    def __init__(self, name):
        self.name = name
        self.shoplist = []
    def shop_inventory(self, object):
        self.shoplist.append(object)
    def purchasing_gear(self,object):
        object.stats = [object.name, f" cost:{object.value}", object.strength, object.sp]
class Weapons(Shop):
    def __init__(self, name, strength, sp, value):
        self.name = name
        self.strength = strength
        self.value = value
        self.sp = sp
    def equip(self):
        object.powah += self.strength
        object.sp +=  self.sp


class Armor(Shop):
    def __init__(self, name, armor, vitality, value):
        self.name = name
        self.armor = int(armor * 1.6)
        self.vitality = vitality
        self.value = value

class Items(Shop):
    def __init__(self, name, value, hp_restored):
        self.name = name
        self.value = value
        self.hp_restored = hp_restored
    def use(self):
        object.hp += self.hp_restored


class Char():
    def __init__(self, name, level, strength, sp):
        self.name = name
        self.level = level
        self.hp = int(100 + (25 * self.level ** 1.6))
        self.equips = None
        self.gold = 150
        self.sp = 20 
        self.powah = (int(strength + (self.level * 3)))
        if self.powah <= 9999:
            self.powah = self.powah
        elif self.powah > 9999:
            self.powah = 9999
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
    def attack(self, object):
        self.crit = random.randint(1, 5)
        if self.hp > 0 and object.hp > 0:
            object.hp -=  self.powah
            print(f"{self.name} deals {self.powah} damage!")
            if self.crit == random.randint(1, 5):
                    object.hp -= self.powah * 1.5
                    print(f"{self.name} deals additional {int(self.powah * 1.5)} damage with a crit hit!")

    def skills(self, object):
        if self.name == "Creda":
            use_skill = int(input("""
            Skill Menu:

            'What skill should I use...'
            1. Triple Strike   - 15sp   2. Flame Draw      - 50sp
            3. Sword Dance     - 50sp   4. Eclyptic Slash  - 85sp
            5. Dimensional Cut - 100sp  6. Celestial Break - 125sp
            7. ???               200sp  8. ???             - 450sp
            >>> """))
            if use_skill == 1 and self.sp >= 15:
                self.sp - 15
                object.hp -= (self.powah * 3) - object.defense
                damage = (self.powah * 3) - object.defense
                print(f"""
                {self.name} deals {damage} damage to {object.name}!
                """)    
            elif use_skill == 2 and self.sp >= 20:
                self.sp - 20
                object.hp -= self.powah * 4.5
                damage = int((self.powah * 4.5))
                print(f"""
                {self.name} deals {damage} damage to {object.name}!
                {object.name} has {int(object.hp)} health remaining.

                """)
            elif use_skill == 3 and self.sp >= 50:
                self.sp - 50
                object.hp -= self.powah * 7
                damage = self.powah * 7
                print(f"""
                {self.name} deals {damage} damage to {object.name}!
                {object.name} has {int(object.hp)} health remaining.

                """)
            elif use_skill == 4 and self.sp >= 85:
                self.sp - 85
                object.hp -= self.powah * 10
                damage = self.powah * 10
                print(f"""
                {self.name} deals {damage} damage to {object.name}!
                {object.name} has {int(object.hp)} health remaining.

                """)
            elif use_skill == 5 and self.sp >= 100:
                self.sp - 100
                object.hp -= self.powah * 12
                damage = self.powah * 12
                print(f"""
                {self.name} deals {damage} damage to {object.name}!
                {object.name} has {int(object.hp)} health remaining.

                """)
            elif use_skill == 6 and self.sp >= 125:
                self.sp - 100
                object.hp -= self.powah * 15
                damage = self.powah * 15
                print(f"""
                {self.name} deals {damage} damage to {object.name}!
                {object.name} has {int(object.hp)} health remaining.

                """)
            elif use_skill == 7 and self.sp >= 200:
                self.sp - 200
                object.hp -= self.powah * 50
                damage = self.powah * 50
                print("""
                Awakening skill: Singularity Destruct!
                """)
                print(f"""
                {self.name} deals {damage} damage to {object.name}!
                {object.name} has {int(object.hp)} health remaining.

                """)
            elif use_skill == 8 and self.sp >= 450:
                self.sp - 450
                object.hp -= self.powah * 200
                damage = self.powah * 200
                print("""
                I will bring all of my power to bear!
                Final Skill: Infinite Obliteration!
                """)
                print(f"""
                {self.name} deals {damage} damage to {object.name}!
                {object.name} has {int(object.hp)} health remaining.

                """)
            elif use_skill in range(9, 100):
                print("Wait, what am I even thinking right now!?")
                self.skills(object)
            else:
                print("\'I don't have enough energy for that skill.\'")
                self.skills(object)

    def alive(self):
        if self.hp >= 1:
            return self.hp
    def status(self):
        if self.hp >= 0:
            print(f"{self.name} {self.hp}")
        elif self.hp <= 0:
            print(f"{self.name} has been defeated.")
            print("And so the world came face to face with annihilation...")

class Goon(object):
    def __init__(self, name, level):
        self.name = name
        self.hp = random.randint(200, 210) * (level / 3)
        self.level = level
        self.defense = 3 + self.level
        self.powah = 6 + (self.level * self.level * 2) / 3
        
    def attack(self, object):
            if self.hp >= 0:
                object.hp -= int(self.powah - object.defense * 1.5)

class Enemy(Char):
    def __init__(self, name):
        self.name = name
        self.powah = 9999
        self.hp = 150000000
        self.critchance = random.randint(1, 5)
        self.defense = 800
    def attack(self, object):
        if self.hp >= 0:
            object.hp -= self.powah
            print(f"{self.name} deals {self.powah} damage to {object.name}")
            if self.critchance == 1:
                self.powah = self.powah * 3

        

creda = Hero("Creda", 1, 50, 50)
# cicilene = Enemy("Cicilene")
# wolf = Goon("Wolf", 10)
creda.status()
def game():
    while creda.hp >= 1:
        print("""
        "Finally made it to the Edge of Nowhere...
        Now I can train for my fight with Cicilene!"
        """)
        choice = int(input("""
        The real question is, what should I do for the moment?
        1. Explore
        2. Visit Shop
        3. Check Status
        4. Return and Fight Cicilene
        5. Explore Nearby Cave
        6. Buy Cicilene a peace offering. (Quit Game)
            >>> """))
        if choice == 1:
            print("ok")
        if choice == 2:
            pass
        if choice == 3:
            creda.status()
        if choice == 4:
            pass
        if choice == 5:
            print("""
            "I suppose I could just buy her some ice cream instead...
            Eh, I'll just think about that on the way back home."
            """)
            break
game()