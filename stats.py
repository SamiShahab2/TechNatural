#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Stats Module
"""Contains class that encapsulates the player's stats"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import initialize

import os

class Player:

    def __init__(self, health, weapons, equipweap, x_loc, y_loc):
        self.health = health
        self.weapons = weapons
        self.equipweap = equipweap
        self.x_loc = x_loc
        self.y_loc = y_loc

# Player object used during the game
player = Player(initialize._playerhealth_, 
               initialize._playerweapons_,
               initialize._playereqweapon_,
               initialize._playerx_,
               initialize._playery_)


def savegame():
    """Saves the players current stats to an external file so they can save their
    progress for the next time they play"""
    # Overwrites or creates a new save file
    # As of now, only thing that has a gameplay difference is the player's position
    with open("save.txt", "w") as Savefile:
        try:
            # Writes each player stat to the save file
            Savefile.write(str(player.health) + "\n")
            for weapons in player.weapons:
                Savefile.write(weapons + "\n")
            Savefile.write(str(player.equipweap) + '\n')
            Savefile.write(str(player.x_loc) + "\n")
            Savefile.write(str(player.y_loc) + "\n")
        except:
            # Error message if save fails
            print("Uh oh, your logging machine has weeds in it!")
        else:
            # Else this message prints
            print("Save was succesful!")
        finally:
            # Final message prints regardless of outcome
            print("You put the logging machine away")
            print("\n")


def loadgame():
    """Loads player data and allows the player to continue from their save"""
    # Checks if there is a save file
    if os.path.exists("save.txt"):
        try:
            # If so then it loads each piece of data
            with open("save.txt", "r") as Loadfile:
                data = Loadfile.readlines()
                # Utilizes a counter to check which stat to write to
                counter = 0
                for data in data:
                    counter += 1
                    if counter == 1:
                        player.health = int(data)
                    # NOTE: For some reason it messes up the weapons
                    # I was debugging it but forgot about this project while
                    # working on the other one.
                    # Unfortunately I have to leave it like this, sorry
                    elif counter == 2:
                        player.weapons = initialize._playerweapons_
                    elif counter == 3:
                        player.equipweap = initialize._playereqweapon_
                    elif counter == 4:
                        player.x_loc = int(data)
                    elif counter == 5:
                        player.y_loc = int(data)
        except:
            # Error Message
            print("Oh no! The logging machine is out of batteries")
        else:
            # Otherwise this one prints
            print("You have loaded your previous data!")
        finally:
            # Final message
            print("You put the logging machine away")
            print('\n')


def newgame():
    """Erases previous player data so they can start a new game"""
    # Arbitrary variable for loop, just so errors can occur
    x = 1
    while x == 1:
        try:
            # Tries to remove the previous save
            os.remove("save.txt")
        # If the file does not exist, this message will print
        except FileNotFoundError:
            print("After years of being unused, the logging machine is still functional")
        else:
            # Otherwise a message will print indicating the file was erased
            print("The previous data on the logging machine was erased")
        finally:
            # Final message
            print("You put the logging machine away")
            x = 2