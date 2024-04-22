#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Search And Events Module
"""Contains functions that handle events and searching"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import map

import inventory

def searchroom():
  """Code that handles the searching of the room"""
  # Checks the room the player currently is in
  for roomname, roomattributes in map.LabFloor1.items():
      # If the room's name matches the name on the array
      # Determined using the player's coordinates
      if roomname == map.Floor1Map[map._playery_][map._playerx_]:
          try:
              print(roomattributes["search"])
              if "event" in roomattributes:
                  if (roomattributes["event"]["event-type"] == "find"
                      and roomattributes["event"]["status"] == 0):
                      print(roomattributes["event"]["solved"])
                      (inventory._playeritems_[roomattributes["event"]["reward-type"]]
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

def eventunlock(_playerchoice_):
  """Handles unlock events"""
   # Checks the room the player currently is in
  for roomname, roomattributes in map.LabFloor1.items():
      # If the room's name matches the name on the array
      # Determined using the player's coordinates
      if roomname == map.Floor1Map[map._playery_][map._playerx_]:
          try:
              if (roomattributes["event"]["event-type"] == "unlock"
                  and roomattributes["event"]["status"] == 1
                  and roomattributes["event"]["required-item"] == _playerchoice_):
                  print(roomattributes["event"]["solved"])
                  (inventory._playeritems_[roomattributes["event"]["reward-type"]]
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