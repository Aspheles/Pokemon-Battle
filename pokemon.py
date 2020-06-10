import random
import gc # Garbage collector for bruteforcing the count of instances of Pokemon

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
    def attack(self, attack):
        return attack.damage


    def take_damage(self, damage, resistance, weakness):
            # if Pokemon type is equal to the resistance type, use the resistance value and deduct that from the damage
            # resistance in the parameters = Other pokemon type
            if(self.resistance.energyType == resistance):
                damage_with_resistance = damage - self.resistance.value
                self.health = self.health - damage_with_resistance
                return self.health
            # if Pokemon type is equal to the weakness type, use the weakness multiplier and add that damage to the total
            elif(resistance == self.weakness.energyType):
                damage_with_multiplier = damage * self.weakness.multiplier
                self.health = self.health - damage_with_multiplier
                return self.health
            # if there is no weakness or resistance, normal damage
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


class Resistance():
    def __init__(self, energyType, value):
        self.energyType = energyType
        self.value = value


class Battle:
    # Constructor of Fight class
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

     #Contains the construction of the battle in str so we can read the output
    def __str__(self):
        #print hp at start of Fight
        print(
            f"Pikachu HP: {self.pokemon1.health}, Charmeleon HP: {self.pokemon2.health}")
        # Electric ring attack
        self.pokemon2.take_damage(self.pokemon1.attack(
            self.pokemon1.attacks[0]), self.pokemon1.energyType, self.pokemon1.weakness)
        #Flare attack
        self.pokemon1.take_damage(self.pokemon2.attack(
            self.pokemon2.attacks[1]), self.pokemon2.energyType, self.pokemon2.weakness)
        #return hp at end of Fight
        return f"Pikachu HP: {self.pokemon1.health}, Charmeleon HP: {self.pokemon2.health}"





# Pikachu = Pokemon("Pikachu", EnergyType("Lightning"), 60,
#                   60, [Attack("Electric Ring", 50), Attack("Pika Punch", 20)], Weakness("Fire", 1.5), Resistance("Fighting", 20))

# Charmeleon = Pokemon("Charmeleon", EnergyType("Fire"), 60,
#                      60, [Attack("Head Butt", 10), Attack("Flare", 30)], Weakness("Water", 2), Resistance("Lightning", 10))

class Pikachu(Pokemon):
    def __init__(self, name):
      super().__init__(name, EnergyType("Lightning"), 60, 60,[Attack("Electric Ring", 50), Attack("Pika Punch", 20)], Weakness("Fire", 1.5), Resistance("Fighting", 20))

class Charmeleon(Pokemon):
    def __init__(self,name):
        super().__init__(name, EnergyType("Fire"), 60, 60, [Attack("Head Butt", 10), Attack("Flare", 30)], Weakness("Water", 2), Resistance("Lightning", 10))


spikachu = Pikachu('bob')
scharmeleon = Charmeleon("tom")

battle = Battle(spikachu, scharmeleon)
print(battle)

class Status:
    #staticmethode because no __init__, self
    @staticmethod
    def getPopulation():
        alive_pokemons = []
        for item in gc.get_objects():
         #Checking if item is pokemon
         if(isinstance(item, Pokemon)):
             #Checking if pokemon has more than 0 hp
             if(item.health > 0):
                 #Add pokemon to array
                 txt = "Name: {}, Health: {}"
                 alive_pokemons.append(txt.format(item.name, item.health))

        return alive_pokemons


check_alive_pokemons = Status
#print pokemon_list
print(check_alive_pokemons.getPopulation())