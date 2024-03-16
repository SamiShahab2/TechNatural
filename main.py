#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Title: Technatural
# Class: Computer Science 30
# Assignment: RPG
# Coder: Sami Shahab
# Version: v0.2
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''A gridbased text-adventure rpg'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Lists ========================================================================================
LabFloor1={
    "Destroyed Hive": {
        "x": 4, 
        "y": 3, 
        "item": "N/A",
        "enemy": "Metallic Bee",
        "description": 
        """Before you lies what seems to be the remains of a beehive.  
Pieces of sharp metal and wax litter the room. Suddenly, a piece of shrapnel 
flies past your head, barely missing you!""" 
    },
    "Overgrown Hallway": {
        "x": 4,
        "y": 2,
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """You find yourself in a hallway filled with lush foliage. The walls
and ground are covered in vines and greenery while the roof is bursting with
flowers, each with a pleasant aroma."""
    },
    "Weapon Testing Chamber": {
        "x": 4,
        "y": 1,
        "item": "N/A",
        "enemy": "Rocket Ram",
        "description":
        """As you enter the room, smokey, debris filled air enters your lungs.
It seems as if this was an area to test out weapons, though it has been destroyed.
In the middle of the room stands one ram, seemingly the culprit of this destruction.
Suddenly, a rocket launcher emerges from a panel on the ram's side!"""
    },
    "Stairs": {
        "x": 3,
        "y": 3,
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """A staircase stands before you, leading up into the next room.
There is a sweet, flowery aroma creeping down from the upper floor.
You can choose to move up the staircase or stay in this floor for a bit longer."""
    },
    "Experiment Room": {
        "x": 3,
        "y": 2,
        "item": "N/A",
        "enemy": "Lazeep",
        "description":
        """Tools for welding and surgery litter this room. It appears they were
merging animals and technology together in this location.
A laser fired in your direction proves that these efforts weren't fruitless"""
    },
    "Equipment Room": {
        "x": 3,
        "y": 1,
        "item": "Weak Paralyzer",
        "enemy": "N/A",
        "description":
        """This room seems to have contained securtity equipment, though it has been
ransacked and mostly cleared out. Empty panels once containing armour and
weapons are sprawled across the walls, all open. Still, maybe there is something
of use to be found?"""
    },
    "Documentation Room": {
        "x": 2,
        "y": 3,
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """You nearly trip over a fallen over file cabinet while entering the room.
Littering the floor are several empty file holders and empty cabinets.
There appears to be one cabinet however that is closed, albeit electronically locked."""
    },
    "Hallway": {
        "x": 2,
        "y": 2,
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """You peer through the door to find a hallway with more doors.
The hallway itself isn't noteworthy but there may be supplies in these other rooms."""
    },
    "Heating": {
            "x": 2,
            "y": 1,
            "item": "N/A",
            "enemy": "Venus Flame Trap",
            "description":
            """Steam gushes out of the mechanism within this room.
The Machine seems to have been designed to heat the facility.
However, the machine begins to sputter flames as two leaves emerge from it's sides.
These leaves form a mouth that begins to spew fire in your direction!"""
    },
    "Cryopod Monitoring Room": {
        "x": 1,
        "y": 3,
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """You walk into a room seemingly designed to monitor the cryopods.
Most of the devices have shut off or have been desecrated with foliage.
There still remains one device that is functional."""
    },
    "Cryopod Room": {
        "x": 1,
        "y": 2,
        "item": "N/A",
        "enemy": "N/A",
        "description":
        """Looking around, you notice that the other cryopods have roots
and other plant life bursting out of them. They have been rendered useless."""
    },
    "Cryopod Generator Room": {
        "x": 1,
        "y": 1,
        "item": "N/A",
        "enemy": "Technoplant",
        "description":
        """This room contains the generators that power the cryopods.
A few are damaged but most are running. One of them has a root sticking out.
It's seemingly rerouting power to something. Following the root leads you to a
metallic plant that begins to thrash at you violently."""
    }
}

# Imports and Global Variables =================================================================
# Tracks player's horizontal location
_playerx_ = 1
# Tracks player's vertical location
_playery_ = 2


# Functions ====================================================================================

def startup():
    """Prints text at the beginning of the game"""
    print()