#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Title: Technatural
# Class: Computer Science 30
# Assignment: RPG
# Coder: Sami Shahab
# Version: v2.5
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
_playerweapons_ = ["Glass Shard"]
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
        "visited": 0,
        "description": 
        """Before you lies what seems to be the remains of a beehive.  
Pieces of sharp metal and wax litter the room. Suddenly, a piece of shrapnel 
flies past your head, barely missing you!""",
        "alt-description":
        """Before you lies what seems to be the remains of a beehive.  
Pieces of sharp metal and wax litter the room."""
    },
    "Overgrown Hallway": {
        "item": "N/A",
        "enemy": "N/A",
        "visited": 2,
        "description":
        """You find yourself in a hallway filled with lush foliage. The walls
and ground are covered in vines and greenery while the roof is bursting with
flowers, each with a pleasant aroma."""
    },
    "Weapon Testing Chamber": {
        "item": "N/A",
        "enemy": "Rocket Ram",
        "visited": 0,
        "description":
        """As you enter the room, smokey, debris filled air enters your lungs.
It seems as if this was an area to test out weapons, though it has been destroyed.
In the middle of the room stands one ram, seemingly the culprit of this destruction.
Suddenly, a rocket launcher emerges from a panel on the ram's side!""",
        "alt-description":
        """As you enter the room, smokey, debris filled air enters your lungs.
It seems as if this was an area to test out weapons, though it has been destroyed."""
    },
    "Stairs": {
        "item": "N/A",
        "enemy": "N/A",
        "visited": 2,
        "description":
        """A staircase stands before you, leading up into the next room.
There is a sweet, flowery aroma creeping down from the upper floor.
You can choose to move up the staircase or stay in this floor for a bit longer."""
    },
    "Experiment Room": {
        "item": "N/A",
        "enemy": "Lazeep",
        "visited": 0,
        "description":
        """Tools for welding and surgery litter this room. It appears they were
merging animals and technology together in this location.
A laser fired in your direction proves that these efforts weren't fruitless""",
        "alt-description":
        """Tools for welding and surgery litter this room. It appears they were
merging animals and technology together in this location."""
    },
    "Equipment Room": {
        "item": "Weak Paralyzer",
        "enemy": "N/A",
        "visited": 0,
        "event": {"event-type": "find",
                  "reward-type": "Key",
                  "status": 0,
                  "solved":
          """You managed to find a functional, albeit weak paralyzer in the room""",
          "complete": 
          """No other items seem to remain here"""
         },
        "description":
        """This room seems to have contained securtity equipment, though it has been
ransacked and mostly cleared out. Empty panels once containing armour and
weapons are sprawled across the walls, all open. Still, maybe there is something
of use to be found?""",
        "alt-description":
        """This room seems to have contained securtity equipment, though it has been
ransacked and mostly cleared out. 
Whoever was last here wanted to be prepared for something...""",
        "search":
      """You begin searching the room for any useful supplies"""
    },
    "Documentation Room": {
        "item": "N/A",
        "enemy": "N/A",
        "visited": 0,
        "event": {"event-type": "unlock",
                  "reward": "Floor 1 Map",
                  "reward-type": "Map",
                  "required-item": "Weak Paralyzer",
                  "status": 0,
                  "hint":
                  """Perhaps a weak electric discharge can cause it to open""",
                  "solved":
                  """The Paralyzer short-circuits the electric lock and causes the safe
to open. You find a map of the first floor within. After taking the map out, 
the safe shuts tight, seemingly broken.""",
                  "complete": 
                  """You had managed to open it earlier but now it's shut tight"""
                 },
        "description":
        """You nearly trip over a fallen over file cabinet while entering the room.
Littering the floor are several empty file holders and empty cabinets.""",
        "alt-description":
        """Littering the floor are several empty file holders and empty cabinets.""",
        "search":
        """There appears to be one cabinet however that is closed, 
albeit electronically locked."""
    },
    "Hallway": {
        "item": "N/A",
        "enemy": "N/A",
        "visited": 2,
        "description":
        """You peer through the door to find a hallway with more doors.
The hallway itself isn't noteworthy but there may be supplies in these other rooms."""
    },
    "Heating": {
            "item": "N/A",
            "enemy": "Venus Flame Trap",
            "visited": 0,
            "description":
            """Steam gushes out of a massive mechanism within this room.
The machine seems to have been designed to heat the facility.
However, it begins to sputter flames as two leaves emerge from it's sides.
These leaves form a mouth that begins to spew fire in your direction!""",
            "alt-description":
            """Steam gushes out of a massive mechanism within this room.
The machine seems to have been designed to heat the facility."""
    },
    "Cryopod Monitoring Room": {
        "item": "N/A",
        "enemy": "N/A",
        "visited": 2,
        "description":
        """You walk into a room seemingly designed to monitor the cryopods.
Most of the devices have shut off or have been damaged by foliage.
There still remains one device that is functional."""
    },
    "Cryopod Room": {
        "item": "N/A",
        "enemy": "N/A",
        "visited": 2,
        "description":
        """Looking around, you notice that the other cryopods have roots
and other plant life bursting out of them. They have been rendered useless."""
    },
    "Cryopod Generator Room": {
        "item": "N/A",
        "enemy": "Technoplant",
        "visited": 0,
        "description":
        """This room contains the generators that power the cryopods.
A few are damaged but most are running. One of them has a root sticking out.
It's seemingly rerouting power to something. Following the root leads you to a
metallic plant that begins to thrash at you violently.""",
        "alt-description":
        """This room contains the generators that power the cryopods.
A few are damaged but most are running."""
    }
}

# Tracks player's items
_playeritems_ = {
  "Heal": {
    "Bandaid": 10
  },
  "Key": 
    [],
  "Map":
    ["Floor 1 Map"]
}

PlayerStats = {
    "health": _playerhealth_,
    "weapons": _playerweapons_,
    "equipweap": _playereqweapon_,
    "x-location": _playerx_,
    "y-location": _playery_,
    "items": _playeritems_
}

MoveOptions = ["a", "d", "w", "s", "c", "f", "m"]

InventoryOptions = ["w", "i", "e"]

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
    # Checks the room the player currently is in
    for roomname, roomattributes in LabFloor1.items():
        # If the room's name matches the name on the array
        # Determined using the player's coordinates
        if roomname == Floor1Map[_playery_][_playerx_]:
            print(roomname)
            print("\n")
            # If the room has been visited then the alt description prints
            if roomattributes["visited"] == 1:
                print(roomattributes["alt-description"])
                # The loop then breaks early
                break
            else:
                # Otherwise if the room has an alt description, it's marked as visited
                if roomattributes["visited"] == 0:
                    roomattributes["visited"] = 1
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
            print("""q - Quit Game
c - Search
f - Inventory
m - Map""")
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
              # Checks if the player searched or opened their inventory
              elif (_playerchoice_ == "c" 
                    or _playerchoice_ == "f"
                    or _playerchoice_ == "m"):
                  # If the player inputs c then the search function runs
                  if _playerchoice_ == "c":
                      searchroom()
                  elif _playerchoice_ == "f":
                      inventory(_playerchoice_)
                  elif _playerchoice_ == "m":
                      mapview(_playerchoice_)
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

def searchroom():
    """Code that handles the searching of the room"""
    # Checks the room the player currently is in
    for roomname, roomattributes in LabFloor1.items():
        # If the room's name matches the name on the array
        # Determined using the player's coordinates
        if roomname == Floor1Map[_playery_][_playerx_]:
            try:
                print(roomattributes["search"])
                if "event" in roomattributes:
                    if (roomattributes["event"]["event-type"] == "find"
                        and roomattributes["event"]["status"] == 0):
                        print(roomattributes["event"]["solved"])
                        (_playeritems_[roomattributes["event"]["reward-type"]]
                        .append(roomattributes["item"]))
                        print("\n")
                        print(f"""You obtained {roomattributes['item']}!""")
                        roomattributes["event"]["status"] = 2
                        print("\n")
                    else:
                        if roomattributes["event"]["status"] == 0:
                            roomattributes["event"]["status"] = 1
                        elif roomattributes["event"]["status"] == 1:
                            print(roomattributes["event"]["hint"])
                        else:
                            print(roomattributes["event"]["complete"])
            except KeyError:
                print("Nothing notable in here")
            finally:
                print("Search Complete!")

def inventory(_playerchoice_):
    """Code that handles use of the player's inventory"""
    while _playerchoice_ != "e":
        try:
            print("\n")
            print("""w - Weapons
i - Items
e - Exit""")
            _playerchoice_ = input("Choose which inventory to access: ").lower()
            print("\n")
            _playerchoice_ = float(_playerchoice_)
        except ValueError:
            if _playerchoice_ not in InventoryOptions:
                print("Input a letter from the options")
        else: 
              print("Don't type a number")
        finally:
            if _playerchoice_ == "w":
                weaponmenu()
            elif _playerchoice_ == "i":
                itemmenu(_playerchoice_)

    

def weaponmenu():
    "Encapsulates code for the functions of the weapon menu"
    global _playereqweapon_
    PreviousWeapon = _playereqweapon_
    _playereqweapon_ = "choose"
    while (_playereqweapon_ not in _playerweapons_
           and _playereqweapon_ != "E"):
        try:
            print("\n")
            for weapons in PlayerStats["weapons"]:
                print(f"- {weapons}")
            print("e - Exit")
            print("\n")
            _playereqweapon_ = input(
              "Select a weapon by entering it's name or type 'e' to exit: ").title()
            print("\n")
            _playereqweapon_ = float(_playereqweapon_)
        except ValueError:
            if (_playereqweapon_ not in PlayerStats["weapons"]
                and _playereqweapon_ != "E"):
                print("Type the name of a weapon or type 'e' to exit")
        else:
            print("Don't type a number")
        finally:
              if _playereqweapon_ == "E":
                  print("Returning to previous menu")
                  _playereqweapon_ = PreviousWeapon
              elif _playereqweapon_ in _playerweapons_:
                  print(f"{_playereqweapon_} equipped")
              else:
                  print("Try choosing again")

def itemmenu(_playerchoice_):
    """Handles the navigation of the item menu and use of items"""
    global _playeritems_, _playerhealth_
    _playerchoice_ = "choose"
    while _playerchoice_ != "E":
        try:
            print("\n")
            for items in _playeritems_.keys():
                if items == "Heal":
                    for names in _playeritems_["Heal"]:
                        print(f"- {names}")
                elif items == "Map":
                    pass
                else:
                    for names in _playeritems_["Key"]:
                        print(f"- {names}")
            print("e - exit")
            print('\n')
            _playerchoice_ = input("Choose an item or type 'e' to exit: ").title()
            print('\n')
            _playerchoice_ = float(_playerchoice_)
        except ValueError:
            if (_playerchoice_ not in _playeritems_["Heal"]
                and _playerchoice_ not in _playeritems_["Key"]
                and _playerchoice_ != "E"
                or _playerchoice_ in _playeritems_["Map"]):
                print("Type the name of an item or type 'e' to exit")
        else:
            print("Don't type a number")
        finally:
            if _playerchoice_ in _playeritems_["Heal"]:
                _playerhealth_= _playerhealth_ + _playeritems_["Heal"][_playerchoice_]
                print(f"You healed {_playeritems_['Heal'][_playerchoice_]} HP!")
                _playeritems_["Heal"].pop(_playerchoice_)
            elif _playerchoice_ in _playeritems_["Key"]:
                eventunlock(_playerchoice_)

def eventunlock(_playerchoice_):
    """Handles unlock events"""
     # Checks the room the player currently is in
    for roomname, roomattributes in LabFloor1.items():
        # If the room's name matches the name on the array
        # Determined using the player's coordinates
        if roomname == Floor1Map[_playery_][_playerx_]:
            try:
                if (roomattributes["event"]["event-type"] == "unlock"
                    and roomattributes["event"]["status"] == 1
                    and roomattributes["event"]["required-item"] == _playerchoice_):
                    print(roomattributes["event"]["solved"])
                    (_playeritems_[roomattributes["event"]["reward-type"]]
                    .append(roomattributes["event"]["reward"]))
                    print("\n")
                    print(f"""You obtained {roomattributes['event']['reward']}!""")
                    roomattributes["event"]["status"] = 2
                    print("\n")
                elif roomattributes["event"]["status"] == 0:
                    print("You are unsure what to use the item on")
                else:
                    print(roomattributes["event"]["complete"])
            except KeyError:
                print("Can't use this item here")
            finally:
                pass

def mapview(_playerchoice_):
    """Handles viewing of the map"""
    while _playerchoice_ != "e":
        try:
            if _playeritems_["Map"] == []:
                print("You currently have no maps!")
                print("\n")
                _playerchoice_ = "e"
            else:
                for names in _playeritems_["Map"]:
                    print(f"- {names}")
                print("e - Exit")
                print("\n")
                _playerchoice_ = input("Type the name of a map or 'e' to exit: ")
                print("\n")
            _playerchoice_ = float(_playerchoice_)
        except ValueError:
            if (_playerchoice_ not in _playeritems_["Map"]
                and _playerchoice_ != "e"):
                print("Type the name of a map or type 'e' to exit")
        else:
            print("Don't type a number")
        finally:
            if _playerchoice_ in _playeritems_["Map"]:
                if _playerchoice_ == "Floor 1 Map":
                    with open('Labmap1.txt', "r") as file:
                        try:
                            print(_playerchoice_)
                            print(file.read())
                        except:
                            print("Something went wrong when trying to view the map")
                        finally:
                            print("\n")
                
def gameplay():
    """Encapsulates the essential functions for gameplay"""
    while True:
        print("\n")
        describeroom()
        movement()

startup()
gameplay()