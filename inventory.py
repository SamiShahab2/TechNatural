#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Inventory Module
"""Contains data for the player's inventory and menus that interact with the inventory"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Tracks the player's health
_playerhealth_ = 100
# Tracks the player's weapons
_playerweapons_ = ["Glass Shard"]
# Tracks the player's equipped weapon
_playereqweapon_ = "Glass Shard"

InventoryOptions = ["w", "i", "e"]


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
          for weapons in _playerweapons_:
              print(f"- {weapons}")
          print("e - Exit")
          print("\n")
          _playereqweapon_ = input(
            "Select a weapon by entering it's name or type 'e' to exit: ").title()
          print("\n")
          _playereqweapon_ = float(_playereqweapon_)
      except ValueError:
          if (_playereqweapon_ not in _playerweapons_
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
  import searchnevent
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
            searchnevent.eventunlock(_playerchoice_)



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