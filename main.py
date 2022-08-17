import random
from secrets import choice

herc_attr = {
    "Health" : 500,
    "Attack Power" : [50 ,75, 100],
    "Attacks" : ["BOnk", "Roar", "Mighty Swing"]
}

enmy_attr = {
    "Health" : 150,
    "Attack Power" : [25, 50, 75],
    "Attacks" : ["Scream", "Chilling Touch", "Wail"]
}

def presents_story():
    print("The story begins.....Hercules faces the enemies, the spectral forms of his own children")

def select_atk():
   
    print("make a nice spaced out display of choices")
    player_atk_choice = input("Select attack:")
    herc_attr["Attacks"][ player_atk_choice]
    #if statement? if 0 1 2 3


def enmy_atk():
    enemy_choice = random.choice(enmy_attr["Attacks"]) #I believe alot of math will need to be done here

    print("enemy used attkname it did x damage!")

def Attack():
    #terminate when HP for either = 0
    if herc_attr["Health"] == 0:
        return True
    if enmy_attr["Health"] == 0: 
        return True
    if herc_attr["Health"] != 0:
        select_atk()
    if enmy_attr["Health"] != 0:
        enmy_atk()


#
#Try to make one function that logs damage from either 
#

def run_game(bool):
    presents_story()#dont want this to loop, may not be the best place
    #this will call all other functions
    while bool == False:
      Attack()

run_game(False)