#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Title: Technatural
# Class: Computer Science 30
# Assignment: RPG
# Coder: Sami Shahab
# Version: v3.4
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''A gridbased text-adventure rpg'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Imports and Global Variables =================================================================
import sys

import map

import inventory

import searchnevent

import stats

# Tracks player's input choice
_playerchoice_ = "N/A"


# Lists ========================================================================================


# Contains all of the keys used in the movement function
MoveOptions = ["a", "d", "w", "s", "c", "f", "m"]


# Functions ====================================================================================

def startup():
    """Prints text at the beginning of the game"""
    print("Welcome to Technatural! A text based adventure RPG!")
    print("""You wake up in a cryopod with no prior memory of your past.
Emerging from the tank, you see that you are in a man made room covered with plant-life.
There does not seem to be anyone else here, though there are noises from other rooms.
Arming yourself with a glass shard, you set out to escape.""")


def describeroom():
    """Prints the description of the room the player is in"""
    global _room_
    # Checks the room the player currently is in
    for roomname, roomattributes in map.LabFloor1.items():
        # If the room's name matches the name on the array
        # Determined using the player's coordinates
        if roomname == map.Floor1Map[stats.player.y_loc][stats.player.x_loc]:
            print(roomname)
            print("\n")
            map.room_assigner(roomname, roomattributes)
            # If the room has been visited then the alt description prints
            if map._room_.visited == 1:
                print(map._room_.alt_description)
                # The loop then breaks early
                break
            else:
                # Otherwise if the room has an alt description, it's marked as visited
                if map._room_.visited == 0:
                    map._room_.visited = 1
            # The room's description is printed and the loop breaks
            print(map._room_.description)
            break

def movement():
    """Code that controls the player's movements"""
    global _playerchoice_
    # Plays the loop while a choice has not been inputted
    while _playerchoice_ == "N/A":
        try:
            # Prints out all of the movement options the players have
            print("\n")
            print("""q - Quit Game
c - Search
f - Inventory
m - Map""")
            # If the player cannot move in that direction, the option is not printed
            if stats.player.x_loc != 0:
                print("a - Move Left")
            if stats.player.x_loc != 3:
                print("d - Move Right")
            if stats.player.y_loc != 0:
                print("w - Move Up")
            if stats.player.y_loc != 2:
                print("s - Move Down")
            # The player inputs their option here
            _playerchoice_ = input("Type the letter to choose what to do: ").lower()
            print("\n")
            # If the player inputs "q" then the player will exit the game
            if _playerchoice_ == "q":
                print("Bye Bye!")
                _playerchoice_ = "quit"
                sys.exit()
            # The input is tested to see if it's an number
            _playerchoice_ = float(_playerchoice_)
        # A ValueError indicates the input is a string
        except ValueError:
            # Checks if the player's is a valid movement option
            if _playerchoice_ not in MoveOptions:
                # If not, an error message is shown and the loop continues
                print("Input an letter from the options")
                _playerchoice_ = "N/A"
        # No ValueError indicates the input is a number
        else:
            # An error message is displayed and the loop continues
            print("Don't input a number")
            _playerchoice_ = "N/A"
        finally:
            # Checks if the player can move in that direction
            if ((stats.player.x_loc == 0 and _playerchoice_ == "a")
                or (stats.player.x_loc == 3 and _playerchoice_ == "d")
                or (stats.player.y_loc == 0 and _playerchoice_ == "w") 
                or (stats.player.y_loc == 2 and _playerchoice_ == "s")):
                # If the player is on the edge of the map, the movement fails
                    # An error message is printed and the loop continues
                    print("Can't move in that direction!")
                    print("Movement Failed")
                    _playerchoice_ = "N/A"
            # Otherwise the code checks the playerchoice variable
            else:
              # Checks if player wants to move left
              if _playerchoice_ == "a":
                  stats.player.x_loc = stats.player.x_loc - 1
                  print("Moving left")
              # Checks if player wants to move right
              elif _playerchoice_ == "d":
                  stats.player.x_loc = stats.player.x_loc + 1
                  print("Moving right")
              # Checks if player wants to move up
              elif _playerchoice_ == "w":
                  stats.player.y_loc = stats.player.y_loc - 1
                  print("Moving up")
              # Checks if player wants to move down
              elif _playerchoice_ == "s":
                  stats.player.y_loc = stats.player.y_loc + 1
                  print("Moving down")
              # Checks if the player searched, opened their inventory, or tried to check maps
              elif (_playerchoice_ == "c" 
                    or _playerchoice_ == "f"
                    or _playerchoice_ == "m"):
                  # If the player inputs c then the search function runs
                  if _playerchoice_ == "c":
                      searchnevent.searchroom()
                  # If the player inputs f then the inventory function runs
                  elif _playerchoice_ == "f":
                      inventory.inventory(_playerchoice_)
                  # If the player inputs m then the map function runs
                  elif _playerchoice_ == "m":
                      inventory.playeritems.mapview(_playerchoice_)
                  # Loop will continue after the function has concluded
                  _playerchoice_ = "N/A"
              # If none of the above matches then the general error message prints
              else:
                  # Unless the player chose to quit or search
                  if (_playerchoice_ != "quit" 
                      or _playerchoice_ != "c"
                      or _playerchoice_ != "f"):
                      print("Movement Failed!")
    # Choice is set back to N/A
    _playerchoice_ = "N/A"
    # When the function is called again, the loop will work properly
        

def gameplay():
    """Encapsulates the essential functions for gameplay"""
    while True:
        print("\n")
        describeroom()
        movement()
        map.refresh_room()


startup()
gameplay()