class Pokemon:
    def __init__(self, name, energyType, maxHealth, health, attacks, weakness, resistance):
        self.name = name
        self.energyType = energyType
        self.maxHealth = maxHealth
        self.health = health
        self.attacks = attacks
        self.weakness = weakness
        self.resistance = resistance

    def fight(self, target):
        print(self.name)
        print(target.name)

    def apply_weakness(self, target):
        # checking attack and damage
        chosenAttack = self.attacks[0]
        damage = chosenAttack.damage

        # Checking Weakness
        if(target.weakness.energyType == self.energyType.name):
            damage = damage * target.weakness.multiplier

    def apply_resistance(self, target):
        if(target.resistance.energyType == self.energyType.name):

            damage = damage - (damage*target.resistance.value/100)
        else:
            print("{0} type pokemon can nott resist {1} type attack.".format(
                self.energyType.name, target.resistance.energyType))

    def takeDamage(self, value, target):

        target.health -= value


class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class EnergyType:
    def __init__(self, name):
        self.name = name


class Weakness:
    def __init__(self, energyType, multiplier):
        self.energyType = energyType
        self.multiplier = multiplier


class Resistance:
    def __init__(self, energyType, value):
        self.energyType = energyType
        self.value = value


class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2


# Pokemon needs to be made to its own class method
Pikachu = Pokemon("Pikachu", EnergyType("Lightning"), 60,
                  60, [Attack("Electric Ring", 50), Attack("Pika Punch", 20)], Weakness("Fire", 1.5), Resistance("Fire", 20))

Charmeleon = Pokemon("Charmeleon", EnergyType("Fire"), 60,
                     60, [Attack("Head Butt", 10), Attack("Flare", 30)], Weakness("Water", 2), Resistance("Lightning", 10))


Pikachu.fight(Charmeleon)
