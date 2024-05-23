#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Map Module
"""Contains data for the map"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Array containing the map
Floor1Map = [["Destroyed Hive", "Stairs", "Documentation Room", "Cryopod Monitoring Room"],
             ["Overgrown Hallway", "Experiment Room", "Hallway", "Cryopod Room"],
             ["Weapon Testing Chamber", "Equipment Room", "Heating", "Cryopod Generator Room"]]

# Data for every room on the first floor
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
                  "reward-type": "key",
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
        "item": "Floor 1 Map",
        "enemy": "N/A",
        "visited": 0,
        "event": {"event-type": "unlock",
                  "reward-type": "map",
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

