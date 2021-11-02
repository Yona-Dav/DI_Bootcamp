# Mini-Project: Characters Game

class Character:
    def __init__(self,name,life=20,attack=10):
        self.name = name
        self.life = life
        self.attack = attack
    
    def basic_attack(self,other):
        self.life -= 1

class Druid(Character):
    def __init__(self,name,life=20,attack=10):
        super().__init__(name,life=20,attack=10)
        print('I am a Druid')
    
    def meditate(self):
        self.life +=10
        self.attack -=2
        return f'Number of life of {self.name}: {self.life} \nand number of attack  of {self.name}: {self.attack}'
    
    def animal_help(self):
        self.attack -= 5
        return f'Number of attack of {self.name}: {self.attack} '
    
    def fight(self, other):
        other.life -= (0.75*self.life + 0.75*self.attack)
        return f'Number of life of {other.name}: {other.life} '

class Warior(Character):
    def __init__(self,name,life=20,attack=10):
        super().__init__(name,life=20,attack=10)
        print('I am a Warior')
        if self.life <1 or self.attack<1:
            return f'{self.name} you lose '

    def brawl(self,other):
        self.life += 0.5*self.attack
        other.life -= 2*self.attack
        if other.life <1:
            return f'{other.name} you lose '
        else:
            return f'Number of life of {self.name} : {self.life}\nNumber of life of {other.name} : {other.life}'
    
    def train(self):
        self.life*=2
        self.attack*=2
        return f'Number of life of {self.name}: {self.life} \nand number of attack  of {self.name}: {self.attack}'
    
    def roar(self,other):
        other.attack -= 3
        if other.attack <1:
            return f'{other.name} you lose'
        else:
            return f'Number of attack of {other.name}: {other.attack}'

class Mage(Character):
    def __init__(self,name,life=20,attack=10):
        super().__init__(name,life=20,attack=10)
        print('I am a Mage')

    def curse(self,other):
        other.attack -= 2
        if other.attack <1:
            return f'{other.name} you lose'
        else:
            return f'Number of attack of {other.name}: {other.attack}'

    def summon(self):
        self.attack +=3
        return f'Number of attack of {self.name}: {self.attack}'
    
    def cast_spell(self, other):
        if self.life <1:
            return f'{self.name} you lose'
        else:
            num = int(self.attack/self.life)
            other.life -= num
            if other.attack <1:
                return f'{other.name} you lose'
            else:
                return f'Number of life of {other.name} : {other.life}'

druide1 = Druid('Panoramix')
warior1 = Warior('Asterix')
mage1 = Mage('Merlin')

print(druide1.meditate())
print(druide1.animal_help())
print(druide1.fight(warior1))

print(warior1.brawl(mage1))
print(warior1.train())
print(warior1.roar(druide1))

print(mage1.curse(druide1))
print(mage1.summon())
print(mage1.cast_spell(warior1))
