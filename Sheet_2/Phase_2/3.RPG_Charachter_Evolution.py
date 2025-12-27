class Warrior:

    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self,enemy):
        enemy.health -= self.power
        print(f"{self.name} attacks {enemy.name} and deals {self.power} damage.")

class Paladin(Warrior):
    def __init__(self,name,health,power):
        super().__init__(name,health,power)

    def heal(self,ally):
        ally.health += self.power
        print(f"{self.name} heals {ally.name} and restores {self.power} health.")

    def attack(self,enemy):
        enemy.health -= self.power * 1.2
        print(f"{self.name} attacks {enemy.name} and deals {self.power * 1.2} damage.")

kushal = Paladin("Kushal",100,20)
rahul = Warrior("Rahul",100,20)
kushal.attack(rahul)
kushal.heal(kushal)
print(rahul.health)
print(kushal.health)