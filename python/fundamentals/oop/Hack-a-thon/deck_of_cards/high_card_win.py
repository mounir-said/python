# Pick a card. higher number wins. (without counting suits)
# from classes import card
from classes.deck import Deck
import random

draw = Deck()
pick_1 = draw.pick_a_card()
pick_2 = draw.pick_a_card()

# print(pick_1)
# print(pick_2)

if int(pick_1[1]) > int(pick_2[1]):
    print("Pick One wins")
elif int(pick_1[1]) < int(pick_2[1]):
    print("Pick Two wins")
else:
    print("Let's re-draw!")