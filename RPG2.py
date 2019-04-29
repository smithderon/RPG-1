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
        self.weps = []
        self.armor = []
        self.items = []
    def shop_inventory_wep(self, object):
        self.weps.append(object.name)
    def shop_inventory_armor(self, object):
        self.armor.append(object.name)
    def purchasing_wep(self,object):
        if object.count == 1:
            object.stats = [object.name, f"Cost:{object.value} gold", f"{object.strength} Attack", f"{object.sp} SP", f"No. left: {object.count}"]
            print(f"""
            Aisha: "Here are the stats for {object.name}".
            {object.stats}
            """)
            option1 = input("""
            Are you sure you want to buy it?
            (Y/N)
            """)
            if option1 == ("Y" or "y"):
                object.equip(creda)
            elif option1 == ("N" or "n"):
                print(f"""
                {self.name}: "Sorry, we'll set that aside."
                """)
        elif object.count <= 0:
            print(f"""
            Aisha: "You've already bonded with {object.name}."
            """)
    def purchasing_armor(self, object):
        if object.count == 1:
            object.stats = [object.name, f"Cost:{object.value} gold", f"{object.armor} Defense", f"{object.vitality} HP", f"No. left: {object.count}"]
            print(f"""
            Aisha: "Here are the stats for {object.name}.
            {object.stats}
            """)
            option1 = input("""
            Are you sure you want to buy it?
            (Y/N)
            """)
            if option1 == ("Y" or "y"):
                object.equip(creda)
            elif option1 == ("N" or "n"):
                print(f"""
                {self.name}: "Sorry, we'll set that aside."
                """)
        elif object.count <= 0:
            print(f"""
            Aisha: "You've already bonded with {object.name}."
            """)
    def purchasing_item(self, object):
        object.stats = [object.name, f"Cost:{object.value} gold", f"{object.hp_restored} HP value"]
    def purchasing_man(self, object):
        object.stats = [f"{object.name}", f"Cost:{object.value}", f"Levels gained: {object.exp}"]
        print(f"""
            Aisha: "Here are the stats for {object.name}.
            {object.stats}
            """)
        option1 = input("""
            Are you sure you want to buy it?
            (Y/N)
            """)
        if option1 == ("Y" or "y"):
            object.equip(creda)
        elif option1 == ("N" or "n"):
            print(f"""
            {self.name}: "Sorry, we'll set that aside." """)
    def purchased(self, object):
        if object is Weapons:
            self.weps.remove(object.name)
        elif object is Armor:
            self.armor.remove(object.name)
        # elif object is Items:
        #     object.count - 1
        #     object.char_count += 1
        #     creda.inv[object.name] = object.char_count

class Weapons(Shop):
    def __init__(self, name, strength, sp, value):
        self.name = name
        self.strength = strength
        self.value = value
        self.sp = sp
        self.count = 1
        if self.count < 1:
            self.count == 0
    def equip(self, object):
        if object.gold >= self.value and self.count >= 1:
            object.powah += self.strength
            object.sp +=  self.sp
            object.maxsp += self.sp
            object.gold -=  self.value
            self.count -= 1
            print("""
            Aisha: "Looks like you've bonded successfully with this one!"
            """)
        elif self.value > object.gold:
            print("""
            Aisha: "Remember that thing I said about sufficient compensation..."
            """)
        else:
            print(f"""
            Aisha: "Sorry, I can't help you with that one..."
            """)
            


class Armor(Shop):
    def __init__(self, name, armor, vitality, value):
        self.name = name
        self.armor = int(armor * 1.2)
        self.vitality = vitality
        self.value = value
        self.count = 1
    def equip(self, object):
        if object.gold >= self.value and self.count >= 1:
            object.defense += self.armor
            object.hp +=  self.vitality
            object.gold -=  self.value
            object.maxhp += self.vitality
            self.count -= 1
            print("""
            Aisha: "Looks like you've bonded successfully with this one!"
            """)
        elif self.value > object.gold:
            print("""
            Aisha: "Remember that thing I said about sufficient compensation..."
            """)
        else:
            print(f"""
            Aisha: "Sorry, I can't help you with that one..."
            """)

# class Items(Shop):
#     def __init__(self, name, value, hp_restored):
#         self.name = name
#         self.value = value
#         self.hp_restored = hp_restored
#         self.count = 100
#         self.char_count = 0
#     def use(self):
#         object.hp += self.hp_restored

class Manuals(Shop):
    def __init__(self, value, exp, name):
        self.value = value
        self.exp = exp
        self.name = name
    def equip(self,object):
        if object.level < 99 and object.gold >= self.value:
            object.level += self.exp
            object.gold -= self.value
            object.powah += (int(self.exp * 3))
            object.hp += int(100 + (25 * self.exp ** 1.6))
            object.maxhp += int(100 + (25 * self.exp ** 1.6))
            object.sp += 10 + (self.exp * 10)
            object.maxsp += 10 + (self.exp * 10)
            object.defense += int((3 * self.exp))
            print("""
            Aisha: "That sharpened look in your eye tells me all I need to know!" """)
        if (object.level + self.exp) > 99:
            object.level = 99
        if object.level == 99:
            print ("""
            Aisha: "Sorry, seems like you have all the training these books can help with."
            """)
        elif self.value > object.gold:
            print("""
            Aisha: "Remember that thing I said about sufficient compensation..."
            """)

class Char():
    def __init__(self, name, level, strength):
        self.name = name
        self.level = level
        if self.level <= 99:
            self.level == self.level
        elif self.level > 99:
            self.level = 99
        self.hp = int(100 + (25 * self.level ** 1.6))
        self.maxhp = int(100 + (25 * self.level ** 1.6))
        if self.hp == int(100 + (25 * self.level ** 1.6)):
            self.hp = self.hp
        elif self.hp >= int(100 + (25 * self.level ** 1.6)):
            self.hp = self.maxhp
        self.defense = int(20 + (3 *self.level))
        self.gold = 500
        self.sp = 10 + (self.level * 10)
        self.maxsp = 10 + (self.level * 10)
        self.powah = (int(strength + (self.level * 3)))
        self.shop_count = 0
        # self.inv = {}
        if self.powah <= 999:
            self.powah = self.powah
        elif self.powah > 999:
            self.powah = 999
    def attack(self, object):
        if self.hp > 0 and object.hp > 0:
            object.hp -=  self.powah
            print(f"{self.name} deals {self.powah} damage!")
    def alive(self):
        if self.hp >= 1:
            return self.hp
    def status(self):
        if self.hp >= 0:
            print(f"{self.name} has {self.hp} HP remaining.")
        elif self.hp <= 0:
            print(f"{self.name} has been defeated.")

class Abilities(Char):
    def __init__(self, name, skillpower, spcost, levelreq):
        self.name = name
        self.skillpower = skillpower
        self.spcost = spcost
        self.levelreq = levelreq
    
    def skill_use(self, object):
        pass
# triple_strike = Abilities("Triple Strike", 3, 30, 0)
# inc_draw = Abilities("Incinerating Draw", 5, 50, 0)
# sword_dance = Abilities("Sword Dance", 7.5, 80, 5)
# eclypse = Abilities("Eclyptic Slash", 11, 110, 12)
# dimension = Abilities("Dimensional Slash", 25, 200, 30)
# singularity = Abilities("Singularity Destruct", 50, 500, 40)
# obliterate = Abilities("Infinite Obliteration", 225, 1500, 75)

class Hero(Char):
    def attack(self, object):
        self.crit = random.randint(1, 5)
        if self.hp > 0 and object.hp > 0:
            object.hp -= (self.powah - object.defense)
            print(f"""{self.name} deals {self.powah - object.defense} damage!""")
            if self.crit == random.randint(1, 5):
                    object.hp -= self.powah * 1.5
                    print(f"""{self.name} deals additional {int(self.powah * 1.5)} damage with a crit hit!""")

    def skills(self, object):
        if self.name == "Creda":
            use_skill = input("""
            Skill Menu:

            'What skill should I use...'
            1. Triple Strike   - 15sp   2. Flame Draw      - 20sp
            3. Sword Dance     - 50sp   4. Eclyptic Slash  - 85sp
            5. Dimensional Cut - 120sp  6. Celestial Break - 200sp
            7. ???               500sp  8. ???             - 1500sp
            
            9. Return
            >>> """)
            if use_skill == "1" and self.sp >= 15:
                self.sp -= 15
                object.hp -= (self.powah * 3) - object.defense
                damage = (self.powah * 3) - object.defense
                print(f"""
                {self.name} deals {damage} damage with Triple Strike to {object.name}!""")    
            elif use_skill == "2" and self.sp >= 20:
                self.sp -= 20
                object.hp -= self.powah * 4.5
                damage = int((self.powah * 4.5))
                print(f"""
                {self.name} deals {damage} damage with Flame Draw to {object.name}!""")
            elif use_skill == "3" and self.sp >= 50:
                self.sp -= 50
                object.hp -= self.powah * 7
                damage = self.powah * 7
                print(f"""
                {self.name} deals {damage} damage with Sword Dance to {object.name}"! """)
            elif use_skill == "4" and self.sp >= 85:
                self.sp -= 85
                object.hp -= self.powah * 10
                damage = self.powah * 10
                print(f"""
                {self.name} deals {damage} damage with Eclyptic Slash to {object.name} """)
            elif use_skill == "5" and self.sp >= 120 and self.level >= 15:
                self.sp -= 120
                object.hp -= self.powah * 13
                damage = self.powah * 13
                print(f"""
                {self.name} deals {damage} damage with Dimensional Cut to {object.name}! """)
            elif use_skill == "6" and self.sp >= 200 and self.level >= 25:
                self.sp -= 100 
                object.hp -= (self.powah * 25)
                damage = self.powah * 25
                print(f"""
                {self.name} deals {damage} damage with Celestial Break to {object.name}! """)
            elif use_skill == "7" and self.sp >= 500 and self.level >= 40:
                self.sp -= 500
                object.hp -= (self.powah * 50) - object.defense
                damage = self.powah * 50
                print("""
                "Awakening skill: Singularity Destruct!" """)
                print(f"""
                {self.name} deals an immense {damage} damage with Singularity Destruct to {object.name}!
                """)
            elif use_skill == "8" and self.sp >= 1500 and self.level >= 65:
                self.sp -= 1500
                object.hp -= self.powah * 220
                damage = self.powah * 220
                print(""" "I will bring all of my power to bear!
                     Final Skill: Infinite Obliteration!" """)
                print(f"""
                {self.name} deals {damage} damage with Infinite Obliteration to {object.name}!
                """)
            elif use_skill == "":
                print("Wait, what am I even thinking right now!?")
                self.skills(object)
            elif use_skill == "9":
                print(""" 
                "Nevermind" """)
            elif use_skill == use_skill:
                print("\'I'm not quite ready to use that skill.\'")
                self.skills(object)

    def recover(self):
        if self.hp < self.maxhp:
            self.hp += int(self.maxhp / 5 + self.powah)
            self.sp += int(self.maxsp / 10 + (self.powah / 6))
            print("""
            "I'll take a hit, but I need to catch my breath." """)
            print(f"""System: Recovered {int(self.maxhp / 5 + self.powah)} Health.
            Recovered {int(self.maxsp / 10 + (self.powah / 6))} SP.""")
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        if self.sp > self.maxsp:
            self.sp = self.maxsp
        else:
            print("""
            "I don't really need to do that right now..." """)

    def alive(self):
        if self.hp >= 1:
            return self.hp
    def status(self):
        if self.hp >= 0:
            print(f"Lv.{self.level} {self.name}: {int(self.hp)}/{self.maxhp} HP {self.sp}/{self.maxsp} SP")
            print(f"{self.powah} Attack    {self.defense} Defense")
            print(f"Gold held: {self.gold}")
        elif self.hp <= 0:
            print(f"{self.name} has been defeated.")
            print("And so the world came face to face with annihilation...")

class Goon(object):
    def __init__(self, name, level, value):
        self.name = name
        if level <= 49:
            self.level = level
            self.hp = random.randint(200, 210) * (level / 3)
            self.maxhp = random.randint(200, 210) * (level / 3)
            self.powah = 20 + (self.level * self.level * 2) / 3
            self.defense = 3 + int(self.level ** 1.4)
        if level > 49:
            self.level = level
            self.hp = int(self.level) * (random.randint(200, 210) * (level / 2))
            self.maxhp = int(self.level) * (random.randint(200, 210) * (level / 2))
            self.defense = 3 + int(self.level ** 1.5)
            self.powah = 20 + int(self.level ** 2 * 2) / 1.2
        self.value = value * int(self.level * 1.002) + (self.level ** 2)
        self.maxpowah = self.powah * 2
    def attack(self, object):
        if self.level <= 50:
            if self.hp >= 0 and self.powah > (object.defense * 1.05):
                object.hp -= int(self.powah - object.defense * 1.05)
                print(f"{self.name} deals {int(self.powah - object.defense * 1.05)} damage to {object.name}!")
            elif self.hp >= 0:
                print(f"{self.name} attacks for 0 damage...")
        elif self.level >= 50:
            if self.hp >= 0 and self.powah > (1.05 * object.defense):
                object.hp -= int(self.powah - object.defense * 1.05)
                print(f"{self.name} deals {int(self.powah - object.defense * 1.05)} damage to {object.name}!")
            if self.hp < (self.maxhp / 2) and self.powah < self.maxpowah and self.hp > 0:
                self.powah *= 2
                print(f"""
                {self.name} has become enraged and doubled its power!""")
            if self.hp < (self.maxhp / 10) and self.hp > 0:
                self.hp += (self.maxhp / 4)
                print(f"""
                {self.name} radiates a majestic aura and recovers {int(self.maxhp / 5)} HP! """)
            elif self.hp >= 0 and self.powah <= object.defense:
                print(f"{self.name} attacks for 0 damage...")
    def status(self):
            if self.hp > 0 and self.hp <= self.maxhp:
                print(f"""
                {self.name} has {int(self.hp)} health remaining.
                """)
            elif self.hp <= 0:
                print(f""" 
                "Not even worth the trouble." """)
    def revive(self):
        if self.level < 49:
            self.hp = random.randint(200, 210) * (self.level/ 3)
        elif self.level > 49:
            self.hp = int(self.level) * (random.randint(200, 210) * (self.level / 3))
            self.powah = self.powah = 20 + int(self.level ** 2 * 2) / 1.2

class Sister(Char):
    def __init__(self, name):
        self.name = name
        self.powah = 99999
        self.hp = 9999999
        self.maxhp = 9999999
        self.defense = 9999
        self.level = 9999
        self.count = 0
    def attack(self, object):
        self.critchance = random.randint(1, 5)
        if self.hp >= (self.maxhp / 2) and self.powah > object.defense:
            object.hp -= self.powah - object.defense
            print(f"""{self.name} deals {self.powah - object.defense} damage to {object.name}""")
            if self.critchance == 1:
                object.hp -= (self.powah * 2) - object.defense
                print(f"""{self.name} deals an extra {self.powah * 2} damage with a critical hit!""")
        if self.hp < (self.maxhp / 2) and self.hp > (self.maxhp/10):
            skill_chance = random.randint(1, 2)
            if skill_chance == 1:
                object.hp -= int(self.powah * 2.2) - object.defense
                print(f"""
                {self.name}: "I'll show you how strong I've gotten!" 
                {self.name} deals {int(self.powah * 2.2 - object.defense)} damage with Luminary Torrent!""")
            if skill_chance == 2:
                object.hp -= int(self.powah * 2.25) - object.defense
                print(f"""
                {self.name}: "I can win, I will win!" 
                {self.name} deals {int(self.powah * 2.25 - object.defense)} damage with Grand Cross!""")
        if self.hp < (self.maxhp / 10) and self.count == 0:
            self.hp += int(self.maxhp / 8)
            print(f"""
            {self.name}: "I can see now that you're still very strong...sis.
            But I refuse to lose here! I will prove that I'm stronger!!"
            System: Warning - Cicilene is amasssing large amounts of energy and recovering.
            {self.name}: recovered {int(self.maxhp / 8)} HP
            """)
            self.count += 1 
        if self.count == 1: 
            self.count += 1
            print(f"""
            {self.name}: "Sister, I just want you to know...""")
        if self.count == 2:
            self.count += 1
            print(f"""
            {self.name}: "I don't resent you. Only the depths of your shadow" """)
        if self.count == 3:
            object.hp -= self.powah * 99
            print(f"""
            {self.name}: "But our fight ENDS HERE!!!" 
            {self.name} shatters reality with Art of Annihilation.
            {self.powah * 99} """)
            

        
# MC
creda = Hero("Creda", 5, 55)

# Final
cicilene = Sister("Cicilene")

# Goons
wolf = Goon("Wolf", random.randint(3, 7), 50)
fire_sprite = Goon("Fire Sprite", random.randint(5, 9), 60)
orc = Goon("Orc", random.randint(8,12), 75)
mercenary = Goon("Savage Mercenary", random.randint(13, 16), 80)
bandit = Goon("Bandit", random.randint(15, 19), 100)
captain = Goon("Mercenary Captain", random.randint(20, 25), 120)

# Higher Goons
dragon = Goon("Dragon", random.randint(49, 50), 200)
behemoth = Goon("Behemoth", random.randint(50, 58), 240)
catoblepas = Goon("Catoblepas", random.randint(60, 70), 300)
gigas = Goon("Gigas", random.randint(71, 80), 500)
bahamut = Goon("Bahamut", 99, 1500)


def battle(object):

    while object.hp >= 0 and creda.hp >= 1:

        nani = input(f"""
        Lv.{creda.level} HP: {creda.hp} SP: {creda.sp}
        "Well, how should I put this {object.name} out of its misery..."
        1. Attack
        2. Skill Menu
        3. Scan
        4. Recuperate
        5. Escape
        >>> """)
        if nani == "1":
            creda.attack(object)
            object.attack(creda)
        elif nani == "2":
            creda.skills(object)
            object.status()
            object.attack(creda)
        elif nani == "3":
            print(f""" "Alright let's see what exactly I'm up against..."
            Lv.{object.level} {object.name}: 
                {int(object.hp)} HP, {int(object.powah)} Attack
            """)
            object.attack(creda)
        elif nani == "4":
            creda.recover()
            object.attack(creda)
        elif nani == "5" and object.level >= 50:
            print(f"""
            "There's no way I'm going to get away from this {object.name}!"
            System: Can't escape. """)
        elif nani == "5":
            print("""
            "It'd actually be easier to get out of here."
            System: Successfully escaped.
            """)
            break
        else:
            print(""" "What am I actually thinking." """)
    if object.hp <= 0:
        creda.gold += object.value
        print(f"""
        {object.name} has been defeated! """)
        print(f"Creda gained {object.value} gold.")
    elif creda.hp <= 0:
        print(f"""
        "Crap, this thing's too strong!"
        
        System: Game Over
        """)

def callout(object):
    if object.level <= creda.level:
        print(f"""
        "Great, I ran into a Lv.{object.level} {object.name}. Should be easy practice!"
        """)
    elif object.level  > creda.level:
        print(f"""
        "Looks like a Lv.{object.level} {object.name}.
        I might be in trouble if I try to fight this..."
        """)

def encounter():
    opponent = random.randint(1, 7)
    while True:
        if opponent == 1:
            callout(wolf)
            wolf.revive()
            battle(wolf)
            break
        elif opponent == 2:
            callout(fire_sprite)
            fire_sprite.revive()
            battle(fire_sprite)
            break
        elif (opponent == 3 and creda.level >= 5):
            callout(orc)
            orc.revive()
            battle(orc)
            break
        elif opponent == 4 and creda.level >= 7:
            callout(mercenary)
            mercenary.revive()
            battle(mercenary)
            break
        elif opponent == 5 and creda.level >= 9:
            callout(bandit)
            bandit.revive()
            battle(bandit)
            break
        elif opponent == 6 and creda.level >= 12:
            callout(captain)
            captain.revive()
            battle(captain)
            break
        else:
            acquisition = random.randint(130, 220)
            creda.gold += acquisition
            print(f"""
            "Sweet, a treasure chest!" 
            System: Aquired {acquisition} Gold.""")
            break

def shop():
    if creda.shop_count == 0:
        print(f"""
        ???: "Irashai! My name is Aisha, welcome to my ritual shop!
        Here, I can bond the essence of my equipment with your soul, for sufficent compensation.
        I can also provide you with training manuals to increase your level, again, for sufficient compensation!
        In short I can make you stronger!
        So please, make use of all of the facilities. 
        Oh, and remember, the higher your level, the higher level enemies you'll come across which means bigger bounties! 
        One more thing! I have two legendary relics that I can't bond you with currently...
        But if you were to come back at maximum capacity...!" """)

    while creda.shop_count == creda.shop_count:
        choice = input(f"""
        Aisha: "What can I get for you, Creda?"
        Gold held: {creda.gold}
        1. Weapons
        2. Armor
        3. Items
        4. Training Manuals
        5. Exit
        >>> """)
        if choice == "1":
            print(f"""
            Aisha: "Here's what I have available -
            {aisha.weps}
            """)
            choice1 = input("""
            Aisha: Which would you like?
            (System: Enter key 1 - 8)
            """)
            if choice1 == "1":
                aisha.purchasing_wep(basic_kat)   
                aisha.purchased(basic_kat)    
            elif choice1 == "2":
                aisha.purchasing_wep(gold_kat)
                aisha.purchased(gold_kat)
            elif choice1 == "3":
                aisha.purchasing_wep(muramasa)
                aisha.purchased(muramasa)
            elif choice1 == "4":
                aisha.purchasing_wep(masamune)
                aisha.purchased(masamune)
            elif choice1 == "5":
                aisha.purchasing_wep(sky_divider)
                aisha.purchased(sky_divider)
            elif choice1 == "6":
                aisha.purchasing_wep(abyss)
                aisha.purchased(abyss)
            elif choice1 == "7":
                aisha.purchasing_wep(ame_no_murakumo)
                aisha.purchased(ame_no_murakumo)
            elif choice1 == "8" and creda.level >= 99:
                aisha.purchasing_wep(apocalypse)
                aisha.purchased(apocalypse)
            elif choice1 == "8" and creda.level != 99:
                print("""
                Aisha: "Sorry, I don't think you're quite ready for that one..." """)
            else:
                pass

        elif choice == "2":
            print(f"""
            Aisha: "Here's what I have available." 
            {aisha.armor}""")
            choice2 = input("""
            Aisha: "Which one would you like to have soul-bound?"
            (System: Enter key 1-7, or 8 to exit)
            >>> """)
            if choice2 == "1":
                aisha.purchasing_armor(mail)
                aisha.purchased(mail)
            elif choice2 == "2":
                aisha.purchasing_armor(chain)
                aisha.purchased(chain)
            elif choice2 == "3":
                aisha.purchasing_armor(diamond)
            elif choice2 == "4":
                aisha.purchasing_armor(grand)
            elif choice2 == "5":
                aisha.purchasing_armor(shroud)
            elif choice2 == "6":
                aisha.purchasing_armor(oric)
            elif choice2 == "7" and creda.level >= 99:
                aisha.purchasing_armor(frag)
            elif choice2 == "7" and creda.level != 99:
                print("""
                Aisha: "You're not ready for that one, sorry."
                """)
            else:
                print("""
                Aisha: "Oh, perhaps you had something else in mind?""")

        elif choice == "3":
            print (f"""
            Aisha: "My, this is embarrassing!
                    I haven't actually gotten any items in yet." """)
        elif choice == "4":
            option = input("""
            Aisha: "What manual would you like today?"
            1. Basic Manual
            2. Intermediate Manual
            3. Advance Manual
            4. Expert Manual
            5. Max Eptitiude Manual 
            >>> """)
            if option == "1":
                aisha.purchasing_man(basic)
            if option == "2":
                aisha.purchasing_man(interm)
            if option == "3":
                aisha.purchasing_man(adv)
            if option == "4":
                aisha.purchasing_man(ex)
            if option == "5":
                aisha.purchasing_man(macs)
        elif choice == "5":
            print("""
            Aisha: "Good luck out there!"
            """)
            break
        else:
                print("""
                Aisha: "Oh, perhaps you had something else in mind?""")
    creda.shop_count += 1

def encounter2():
    opponent = random.randint(1, 6)
    while True:
        if opponent == 1:
            callout(dragon)
            dragon.revive()
            battle(dragon)
            break
        elif opponent == 2:
            callout(behemoth)
            behemoth.revive()
            battle(behemoth)
            break
        elif opponent == 3 and creda.level >= 55:
            callout(catoblepas)
            catoblepas.revive()
            battle(catoblepas)
            break
        elif opponent == 4 and creda.level >= 60:
            callout(gigas)
            gigas.revive()
            battle(gigas)
            break
        elif opponent == 5 and creda.level >= 70:
            callout(bahamut)
            bahamut.revive()
            battle(bahamut)
            break
        else:
            acquisition = random.randint(2500, 4000)
            creda.gold += acquisition
            print(f"""
            "Jackpot! A ancient treasure chest!" 
            System: Aquired {acquisition} Gold.""")
            break

def final_battle(object):
    while object.hp >= 0 and creda.hp >= 1:

        nani = input(f"""
        Lv.{creda.level} HP: {creda.hp} SP: {creda.sp}
        "{object.name}...I never wished to harm you, little sister.
        I'll see for myself just how strong you've grown!"
        1. Attack
        2. Skill Menu
        3. Scan
        4. Recuperate
        >>> """)
        if nani == "1":
            creda.attack(object)
            object.attack(creda)
        elif nani == "2":
            creda.skills(object)
            object.status()
            object.attack(creda)
        elif nani == "3":
            print(f""" "Alright let's see what exactly I'm up against..."
            Lv.{object.level} {object.name}: 
                {int(object.hp)} HP, {int(object.powah)} Attack, {int(object.defense)} Defense
            """)
            object.attack(creda)
        elif nani == "4":
            creda.recover()
            object.attack(creda)
        else:
            print(""" "I have to focus here." """)
    if object.hp <= 0:
        print(f"""
        Creda: "Lene, Even though I won, I will always respect your strength.
                There's no shame in knowing I can protect you." 
        Cicilene: "I can't help it sis, I just wanted to beat you...at least one time..." 
        
        System: Thank you for playing! """)
    elif creda.hp <= 0:
        print(f"""
        "I'm really proud of how strong you've gotten...Cicilene..."
        System: "Thank you for playing!
        """)


def final_encounter():
    print("""
    "Well, I guess it's about time to see how much stronger we've each gotten.
    Still, I better make sure I'm absolutely prepared to fight her."
    """)
    while True:
        truly = input("""System: Do you truly wish to return home? (Y/N)
        >>> """)
        if truly == ("Y" or "y"):
            print("""
            Cicilene: "So, I take it your presence here means you're finally ready to see who's gotten strongest?" 
            Creda: "Sis, maybe we don--" """)
            raw_input = input("")
            if raw_input == raw_input:
                print("""
                Cicilene: "No! I will not be swayed with words! Only absolute power speaks from here on out! 
                Creda: "...Fine, if that what it takes to make you listen. """)
                final_battle(cicilene)
            break
        elif truly ==  ("N" or "n"):
            print("'No, not quite ready yet.'")
            break

def cave():
        while creda.hp >= 1:
            creda.status()
            choice = input(f"""
            "I can feel the intensity of the monsters in this cave...
            But...I'll definitely get a lot stronger in this cave as well!"
            1. Explore
            2. Check Status
            3. Rest
            4. Exit
            >>> """)
            if choice == "1":
                encounter2()
            if choice == "2":
                creda.status()
            if choice == "3":
                creda.hp = creda.maxhp
                creda.sp = creda.maxsp
            if choice == "4":
                break

def game():
    while creda.hp >= 1:
        creda.status()
        choice = str(input(f"""
        Now, what should I do for the moment?
        1. Explore
        2. Ritual Shop
        3. Return and Fight Cicilene
        4. Explore Nearby Cave
        5. Rest
        6. Buy Cicilene a peace offering. (Quit Game)
            >>> """))
        if choice == "1":
            encounter()
        if choice == "2":
            shop()
        if choice == "3":
            final_encounter()
        if choice == "4" and creda.level <= 40:
            really = input("""
            "I'm 100 percent sure it would be a bad idea for me to go in there right now..."
            System: Enter Cave? (Y/N)
            """)
            if really == ("Y" or "y"):
                cave()
            elif really == ("N" or "n"):
                print("""
                "Yeah, I think I'll go in there when I'm a little stronger."
                """)
        elif choice == "4" and creda.level >= 50:
            cave()
        if choice == "5":
            print("""
            "Phew, I need a breather!"
            System: Status restored.
            """)
            creda.hp = creda.maxhp
            creda.sp = creda.maxsp
        if choice == "6":
            print("""
            "I suppose I could just buy her some ice cream instead...
            Eh, I'll just think about that on the way back home." """)
            break

aisha = Shop("Aisha")

# Weapons
basic_kat = Weapons("Improved Katana", 60, 10, 1050)
gold_kat = Weapons("Golden Katana", 150, 20, 2200)
masamune = Weapons("Masamune", 500, 50, 7000) 
muramasa = Weapons("Muramasa", 280, 35, 4000)
sky_divider = Weapons("Sky Splitter", 1300, 100, 40000)
abyss = Weapons("Abyssal Touch", 1800, 250, 50000)
ame_no_murakumo = Weapons("Ame-no-Murakumo", 5000, 500, 200000)
apocalypse = Weapons("Apocalypse", 9999, 4000, 1000000)
aisha.shop_inventory_wep(basic_kat)
aisha.shop_inventory_wep(gold_kat)
aisha.shop_inventory_wep(muramasa)
aisha.shop_inventory_wep(masamune)
aisha.shop_inventory_wep(sky_divider)
aisha.shop_inventory_wep(abyss)
aisha.shop_inventory_wep(ame_no_murakumo)

# Armor
mail = Armor("Plate mail", 45, 150, 550)
chain = Armor("Chain mail", 70, 400, 1300)
diamond = Armor("Diamond mail", 180, 1000, 4000)
grand = Armor("Grand Armor", 370, 1800, 6000)
shroud = Armor("Darkness Shroud", 700, 3000, 20800)
oric = Armor("Orichalcum", 4000, 15900, 250000)
frag = Armor("Fragment of Infinity", 9999, 99999, 600000)
aisha.shop_inventory_armor(mail)
aisha.shop_inventory_armor(chain)
aisha.shop_inventory_armor(diamond)
aisha.shop_inventory_armor(grand)
aisha.shop_inventory_armor(shroud)
aisha.shop_inventory_armor(oric)


basic = Manuals(600, 1, "Basic Manual")
interm = Manuals(1150, 2, "Adept Manual")
adv = Manuals(2200, 5, "Advanced Manual")
ex = Manuals(4300, 10, "Expert Manual")
macs = Manuals(15000, 35, "Divine Manual")
print("""
"Finally made it to the Edge of Nowhere...
Now I can train for my fight with Cicilene!"
""")
game()