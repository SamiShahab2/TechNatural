#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Title: Technatural
# Class: Computer Science 30
# Assignment: RPG
# Coder: Sami Shahab
# Version: v0.4
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''A gridbased text-adventure rpg'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Imports and Global Variables =================================================================
import sys

# Tracks the player's health
_playerhealth_ = 100
# Tracks player's horizontal location
_playerx_ = 3
# Tracks player's vertical location
_playery_ = 1
# Tracks the player's weapons
_playerweapons_ = "Glass Shard"
# Tracks the player's equipped weapon
_playereqweapon_ = "Glass Shard"
# Tracks player's movement choice
_playerchoice_ = "N/A"

# Lists ========================================================================================

Floor1Map = [["Destroyed Hive", "Stairs", "Documentation Room", "Cryopod Monitoring Room"],
             ["Overgrown Hallway", "Experiment Room", "Hallway", "Cryopod Room"],
             ["Weapon Testing Chamber", "Equipment Room", "Heating", "Cryopod Generator Room"]]

LabFloor1 = {
    "Destroyed Hive": {
        "item": "N/A",
        "enemy": "Metallic Bee",
        "description": 
        """Before you lies what seems to be the remains of a beehive.  
Pieces of sharp metal and wax litter the room. Suddenly, a piece of shrapnel 
flies past your head, barely missing you!""" 
    },
    "Overgrown Hallway": {
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """You find yourself in a hallway filled with lush foliage. The walls
and ground are covered in vines and greenery while the roof is bursting with
flowers, each with a pleasant aroma."""
    },
    "Weapon Testing Chamber": {
        "item": "N/A",
        "enemy": "Rocket Ram",
        "description":
        """As you enter the room, smokey, debris filled air enters your lungs.
It seems as if this was an area to test out weapons, though it has been destroyed.
In the middle of the room stands one ram, seemingly the culprit of this destruction.
Suddenly, a rocket launcher emerges from a panel on the ram's side!"""
    },
    "Stairs": {
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """A staircase stands before you, leading up into the next room.
There is a sweet, flowery aroma creeping down from the upper floor.
You can choose to move up the staircase or stay in this floor for a bit longer."""
    },
    "Experiment Room": {
        "item": "N/A",
        "enemy": "Lazeep",
        "description":
        """Tools for welding and surgery litter this room. It appears they were
merging animals and technology together in this location.
A laser fired in your direction proves that these efforts weren't fruitless"""
    },
    "Equipment Room": {
        "item": "Weak Paralyzer",
        "enemy": "N/A",
        "description":
        """This room seems to have contained securtity equipment, though it has been
ransacked and mostly cleared out. Empty panels once containing armour and
weapons are sprawled across the walls, all open. Still, maybe there is something
of use to be found?"""
    },
    "Documentation Room": {
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """You nearly trip over a fallen over file cabinet while entering the room.
Littering the floor are several empty file holders and empty cabinets.
There appears to be one cabinet however that is closed, albeit electronically locked."""
    },
    "Hallway": {
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """You peer through the door to find a hallway with more doors.
The hallway itself isn't noteworthy but there may be supplies in these other rooms."""
    },
    "Heating": {
            "item": "N/A",
            "enemy": "Venus Flame Trap",
            "description":
            """Steam gushes out of the mechanism within this room.
The Machine seems to have been designed to heat the facility.
However, the machine begins to sputter flames as two leaves emerge from it's sides.
These leaves form a mouth that begins to spew fire in your direction!"""
    },
    "Cryopod Monitoring Room": {
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """You walk into a room seemingly designed to monitor the cryopods.
Most of the devices have shut off or have been desecrated with foliage.
There still remains one device that is functional."""
    },
    "Cryopod Room": {
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """Looking around, you notice that the other cryopods have roots
and other plant life bursting out of them. They have been rendered useless."""
    },
    "Cryopod Generator Room": {
        "item": "N/A",
        "enemy": "Technoplant",
        "description":
        """This room contains the generators that power the cryopods.
A few are damaged but most are running. One of them has a root sticking out.
It's seemingly rerouting power to something. Following the root leads you to a
metallic plant that begins to thrash at you violently."""
    }
}

PlayerStats = {
    "health": _playerhealth_,
    "weapons": _playerweapons_,
    "equipweap": _playereqweapon_,
    "x-location": _playerx_,
    "y-location": _playery_
}

MoveOptions = ["a", "d", "w", "s"]

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
    # Checks the room the player currently is
    for roomname, roomattributes in LabFloor1.items():
        # If the room's name matches the name on the array
        # Determined using the player's coordinates
        if roomname == Floor1Map[_playery_][_playerx_]:
            # The room's description is printed and the loop breaks
            print(roomattributes["description"])
            break

def movement():
    """Code that controls the player's movements"""
    global _playerx_, _playery_, _playerchoice_
    # Plays the loop while a choice has not been inputted
    while _playerchoice_ == "N/A":
        try:
            # Prints out all of the movement options the players have
            print("\n")
            print("q - Quit Game")
            # If the player cannot move in that direction, the option is not printed
            if _playerx_ != 0:
                print("a - Move Left")
            if _playerx_ != 3:
                print("d - Move Right")
            if _playery_ != 0:
                print("w - Move Up")
            if _playery_ != 2:
                print("s - Move Down")
            # The player inputs their option here
            _playerchoice_ = input("Type the letter to choose where to go: ")
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
            if ((_playerx_ == 0 and _playerchoice_ == "a")
                or (_playerx_ == 3 and _playerchoice_ == "d")
                or (_playery_ == 0 and _playerchoice_ == "w") 
                or (_playery_ == 2 and _playerchoice_ == "s")):
                # If the player is on the edge of the map, the movement fails
                    # An error message is printed and the loop continues
                    print("Can't move in that direction!")
                    print("Movement Failed")
                    _playerchoice_ = "N/A"
            # Otherwise the code checks the playerchoice variable
            else:
              # Checks if player wants to move left
              if _playerchoice_ == "a":
                  _playerx_ = _playerx_ - 1
                  print("Moving left")
              # Checks if player wants to move right
              elif _playerchoice_ == "d":
                  _playerx_ = _playerx_ + 1
                  print("Moving right")
              # Checks if player wants to move up
              elif _playerchoice_ == "w":
                  _playery_ = _playery_ - 1
                  print("Moving up")
              # Checks if player wants to move down
              elif _playerchoice_ == "s":
                  _playery_ = _playery_ + 1
                  print("Moving down")
              # If none of the above matches then the general error message prints
              else:
                  # Unless the player chose to quit
                  if _playerchoice_ != "quit":
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

startup()
gameplay()