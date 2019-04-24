import random
class Hero(object):
    def __init__(self, name):
        self.name = name
        self.powah = random.randint(1000, 99999)
        self.hp = random.randint(50000, 99999)
    def attack(self, object):
        while self.hp > 0 and object.health > 0:
            print("Lv.99 {} has {} health and {} power.".format(self.name, self.hp, self.powah))
            print("Lv.99 Cicilene has {} health and {} power.".format(object.health, object.powah))
            print()
            print("No time for indecision!")
            print(f"1. Attack {object.name}")
            print("2. Guard!")
            print("3. Escape!")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                # Hero attacks goblin
                object.health -= self.powah
                print("{} attacks for {} damage to {}.".format(self.name, self.powah, object.name))
                if object.health <= 0:
                    print("Creda: 'Come on little sister, you'll have to try harder to beat me.'")
                if object.health >= 1:
                    print(f"Cicilene deals {object.powah} damage to you with Sword Dance!")
                    self.hp -= object.powah
                    if self.hp <= 0:
                        print("Cicilene: 'Finally...finally, I won one!' ")
            elif raw_input == "2":
                self.hp -= int(object.powah / 3)
                print(f"Cicilene deals {object.powah / 3} damage to you with Sword Dance!")
                if self.hp <= 0:
                    print("Cicilene: 'Finally...finally, I won one!' ")
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

class Enemy(object):
    def __init__(self, name):
        self.name = name
        self.powah = random.randint(500, 9999)
        self.health = random.randint(100000, 999999)
    def attack(self, object):
        while self.health >= 0:
            object.hp -= self.powah
            print(f"{self.name} deals {self.powah} damage to {object.name}")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

creda = Hero("Creda")
cicilene = Enemy("Cicilene")

creda.attack(cicilene)
# def main():