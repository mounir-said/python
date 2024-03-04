

from classes.ninja import Ninja
from classes.pirate import Pirate
import random

# * Use the starter code to make a RPG battle game between ninjas and pirates.

# * Have an instance of a ninja and pirate battle it out 
# * until one's health is depleted.

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

while michelangelo.health > 0 and jack_sparrow.health > 0:
    initial_ninja_attack = random.randint(0,michelangelo.speed)
    initial_pirate_attack = random.randint(0,jack_sparrow.speed)
    if initial_ninja_attack > initial_pirate_attack:
        michelangelo.attack(jack_sparrow)
        jack_sparrow.show_stats()
        michelangelo.show_stats()
    elif initial_pirate_attack > initial_ninja_attack:
        jack_sparrow.attack(michelangelo)
        michelangelo.show_stats()
        jack_sparrow.show_stats()
    else:
        print("The Battle Rages On! They Battle To The Death!\n")

if michelangelo.health == 0:
    print(f"The victor is the pirate {jack_sparrow.name}.")
else:
    print(f"The victor is the ninja {michelangelo.name}.")