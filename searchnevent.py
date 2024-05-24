#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Search And Events Module
"""Contains functions that handle events and searching"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import map

import stats

import inventory

def searchroom():
  """Code that handles the searching of the room"""
  global _room_  
  # Checks the room the player currently is in
  for roomname, roomattributes in map.LabFloor1.items():
      # If the room's name matches the name on the array
      # Determined using the player's coordinates
      if roomname == map.Floor1Map[stats.player.y_loc][stats.player.x_loc]:
          try:
              # Prints the search description
              print(map._room_.search)
              # Checks if there is an event in the room
              if "event" in roomattributes:
                  # If the event is a find type and it has not been triggered
                  if (map._room_.event["event-type"] == "find"
                      and map._room_.event["status"] == 0):
                      # The solved text is printed
                      print(map._room_.event["solved"])
                      # The event reward is added to the player's inventory
                      type_finder(map._room_)
                      print("\n")
                      # The player is told which item they obtained
                      print(f"""You obtained {map._room_.item}!""")
                      # The event is set as complete
                      map._room_.event["status"] = 2
                      print("\n")
                  # If the event is not a find type
                  else:
                      # If the event has not been discovered then it is set to discovered
                      if map._room_.event["status"] == 0:
                          map._room_.event["status"] = 1
                      # If the event has been discovered, a hint is printed
                      elif map._room_.event["status"] == 1:
                          print(map._room_.event["hint"])
                      else:
                          # Otherwise the completed text is printed
                          print(map._room_.event["complete"])
          # If "search" can't be found, this message prints
          except AttributeError:
              print("Nothing notable in here")
          finally:
              # The search is completed and this message prints to indicate it
              print("Search Complete!")


def eventunlock(_playerchoice_):
  """Handles unlock events"""
  global _room_
  # Checks the room the player currently is in
  for roomname, roomattributes in map.LabFloor1.items():
      # If the room's name matches the name on the array
      # Determined using the player's coordinates
      if roomname == map.Floor1Map[stats.player.y_loc][stats.player.x_loc]:
          try:
              # If the event is an unlock type,
              if (roomattributes["event"]["event-type"] == "unlock"
                  # has been discovered,
                  and roomattributes["event"]["status"] == 1
                  # and the player has chosen the correct item
                  and roomattributes["event"]["required-item"] == _playerchoice_):
                  # The solved text is printed
                  print(roomattributes["event"]["solved"])
                  # The event reward is placed into the player's inventory
                  type_finder(roomname, roomattributes)
                  print("\n")
                  # The player is told which item has been obtained
                  print(f"""You obtained {roomattributes['item']}!""")
                  # The event is set to completed
                  roomattributes["event"]["status"] = 2
                  print("\n")
              # If the event has not been discovered, then this message prints
              elif roomattributes["event"]["status"] == 0:
                  print("You are unsure what to use the item on")
              # Otherwise the event must be complete and this text prints
              else:
                  print(roomattributes["event"]["complete"])
          # If there is not an event in the room then this message prints
          except KeyError:
              print("Can't use this item here")
          # Function concludes
          finally:
              pass


def type_finder(room):
    """Determines what the type of the reward item is and
    places the item into the correct section in the inventory"""
    # If the reward is a key item
    if room.event["reward-type"] == "key":
        # Add it to the key item section
        print(room.name)
        inventory.playeritems.key.append(room.item)
    # If the reward is a health item
    elif room.event["reward-type"] == "heal":
        # Add it to the heal item section
        (inventory.playeritems.heal.append(room.item))
    # Otherwise
    else:
        # Add the item to the map section
        (inventory.playeritems.map.append(room.item))