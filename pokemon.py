import random
import gc 

class Pokemon:
    def __init__(self, name, energyType, maxHealth, health, attacks, weakness, resistance):
        self.name = name
        self.energyType = energyType
        self.maxHealth = maxHealth
        self.health = health
        self.attacks = attacks
        self.weakness = weakness
        self.resistance = resistance


    #Takes attack damage and is used in take_damage to be calculated
    def attack(self, target, attack):
        #Returns the damage, which is used for the calculation
        target.damage_calculation(attack.damage, self.energyType)
        
    def damage_calculation(self, damage, energyType):
            # checking resistance type with targets type
            if(self.resistance.energyType == energyType.name):
                damage_with_resistance = damage - self.resistance.value
                self.health = self.health - damage_with_resistance
                return self.health
            # checking weakness type if it matches, applying the multiplier to the damage from the pokemon skill
            elif(energyType.name == self.weakness.energyType):
                damage_with_multiplier = damage * self.weakness.multiplier
                self.health = self.health - damage_with_multiplier
                return self.health
            # return damage if nothing is matching
            self.health = self.health - damage
            return self.health      
            

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class EnergyType:
    def __init__(self, name):
        self.name = name


class Weakness():
    def __init__(self, energyType, multiplier):
        self.energyType = energyType
        self.multiplier = multiplier


class Resistance(EnergyType):
    def __init__(self, energyType, value):
        self.energyType = energyType
        self.value = value


class Battle:
    # Constructor of Fight class
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

        #print hp at start of Fight
        print(f"Pikachu HP: {self.pokemon1.health}, Charmeleon HP: {self.pokemon2.health}")
        # Pokemon1 which is Pikachu is using Electring ring on Pokemon2 (Charmaleon) the target
        self.pokemon1.attack(self.pokemon2, self.pokemon1.attacks[0])
        # Pokemon2 which is Charmaleon is using Flare on Pokemon1 (Pikachu) the target
        self.pokemon2.attack(self.pokemon1, self.pokemon2.attacks[1])

        #print result of battle
        print(f"Pikachu HP: {round(self.pokemon1.health)}, Charmeleon HP: {round(self.pokemon2.health)}")

       

class Pikachu(Pokemon):
    def __init__(self, name):
      super().__init__(name, EnergyType("Lightning"), 60, 60,[Attack("Electric Ring", 50), Attack("Pika Punch", 20)], Weakness("Fire", 1.5), Resistance("Fighting", 20))

class Charmeleon(Pokemon):
    def __init__(self,name):
        super().__init__(name, EnergyType("Fire"), 60, 60, [Attack("Head Butt", 10), Attack("Flare", 30)], Weakness("Water", 2), Resistance("Lightning", 10))


spikachu = Pikachu('bob')
scharmeleon = Charmeleon("tom")

#Battle takes 2 arguments of 2 Pokemon objects
battle = Battle(spikachu, scharmeleon)

def getPopulation():
        alive_pokemons = []
        for item in gc.get_objects():
         #Checking if item is pokemon
         if(isinstance(item, Pokemon)):
             #Checking if pokemon has more than 0 hp
             if(item.health > 0):
                 #Add pokemon to array
                 txt = "Name: {}, Health: {}"
                 alive_pokemons.append(txt.format(item.name, round(item.health)))

        return alive_pokemons


print(getPopulation())