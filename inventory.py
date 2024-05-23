#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Inventory Module
"""Contains data for the player's inventory and menus that interact with the inventory"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import stats

# Keys that the player uses in the inventory
InventoryOptions = ["w", "i", "e"]

def inventory(_playerchoice_):
  """Code that handles use of the player's inventory"""
  # Loop continues until player chooses to exit
  while _playerchoice_ != "e":
      try:
          # Prints out options for player
          print("\n")
          print("""w - Weapons
i - Items
e - Exit""")
          # Player inputs which option they want (automatically lowercase)
          _playerchoice_ = input("Choose which inventory to access: ").lower()
          print("\n")
          # Input is changed to a float to check for a number
          _playerchoice_ = float(_playerchoice_)
      # If a ValueError occurs, the value is confirmed to be a string
      except ValueError:
          # Checks if the player's choice is one of the options for the inventory
          if _playerchoice_ not in InventoryOptions:
              # If not then this message displays
              print("Input a letter from the options")
      else: 
            # No ValueError indicates a number value, causing this message to print
            print("Don't type a number")
      finally:
          # If the player's choice was "w" then the weapon menu opens
          if _playerchoice_ == "w":
              weaponmenu()
          # If the player's choice was "i" then the item menu opens
          elif _playerchoice_ == "i":
              playeritems.itemmenu(_playerchoice_)
  # If the player's choice was "e" then the loop will break, otherwise it continues


def weaponmenu():
  "Encapsulates code for the functions of the weapon menu"
  # Stores the value of the player's currently equipped weapon
  PreviousWeapon = stats.player.equipweap
  # Prepares the value for the loop
  stats.player.equipweap = "choose"
  # Loop checks if the player's input is either a weapon or an exit
  while (stats.player.equipweap not in stats.player.weapons
         and stats.player.equipweap != "E"):
      try:
          print("\n")
          # Prints all of the weapons from the player's inventory
          for weapons in stats.player.weapons:
              print(f"- {weapons}")
          # Prints the option to exit
          print("e - Exit")
          print("\n")
          # Input is automatically capitalized to match weapon names
          stats.player.equipweap = input(
            "Select a weapon by entering it's name or type 'e' to exit: ").title()
          print("\n")
          # ValueError check
          stats.player.equipweap = float(stats.player.equipweap)
      except ValueError:
          # If the chosen weapon is not in player weapons or the player isn't trying to exit:
          if (stats.player.equipweap not in stats.player.weapons
              and stats.player.equipweap != "E"):
              # This error message prints
              print("Type the name of a weapon or type 'e' to exit")
      else:
          # If the input was a number then this message prints
          print("Don't type a number")
      finally:
            # Checks if the player chose to exit
            if stats.player.equipweap == "E":
                print("Returning to previous menu")
                # Player weapon is reset to the stored value
                stats.player.equipweap = PreviousWeapon
            # If the player's weapon was a valid selection then this message prints
            elif stats.player.equipweap in stats.player.weapons:
                print(f"{stats.player.equipweap} equipped")
            else:
                # If neither of the above apply, this message prints and the loop continues
                print("Try choosing again")


class Inventory:

    def __init__(self, key, heal, map):
        self.key = key
        self.heal = heal
        self.map = map


    def itemmenu(self, _playerchoice_):
      """Handles the navigation of the item menu and use of items"""
      import searchnevent
      # Resets the player's choice
      _playerchoice_ = "choose"
      # Loops if the player is not trying to exit
      while _playerchoice_ != "E":
          try:
              print("\n")
              # Prints items in the key "Heal"
              for names in self.heal.keys():
                  print(f"- {names}")
              # If the item is a map then it isn't printed
              # Finishes by printing the Key items
              for names in self.key:
                  print(f"- {names}")
              # Prints the exit option
              print("e - exit")
              print('\n')
              # Input is automatically capitalized to match item names
              _playerchoice_ = input("Choose an item or type 'e' to exit: ").title()
              print('\n')
              # ValueError check
              _playerchoice_ = float(_playerchoice_)
          except ValueError:
              # Checks if the input is not any of the valid options
              if (_playerchoice_ not in self.heal
                  and _playerchoice_ not in self.key
                  and _playerchoice_ != "E"
                  or _playerchoice_ in self.map):
                  # If so then this message prints
                  print("Type the name of an item or type 'e' to exit")
          else:
              # If input is a number, this message prints
              print("Don't type a number")
          finally:
              # Checks if the input is a healing item
              if _playerchoice_ in self.heal:
                  # Player's health increases
                  stats.player.health = (stats.player.health 
                                         + self.heal[_playerchoice_])
                  # This message prints telling the player how much they healed
                  print(f"You healed {self.heal[_playerchoice_]} HP!")
                  # The healing item is removed
                  self.heal.pop(_playerchoice_)
              # If the input is a Key item, the eventunlock function runs
              elif _playerchoice_ in self.key:
                searchnevent.eventunlock(_playerchoice_)
    
    
    def mapview(self, _playerchoice_):
      """Handles viewing of the map"""
      # Checks if player is trying to exit
      while _playerchoice_ != "E":
          try:
              # If the player has no maps then this message prints and the function stops
              if self.map == []:
                  print("You currently have no maps!")
                  print("\n")
                  _playerchoice_ = "E"
              else:
                  # Prints the maps the player has
                  for names in self.map:
                      print(f"- {names}")
                  # Prints exit option
                  print("e - Exit")
                  print("\n")
                  # Input is automatically capitalized to match weapon names
                  _playerchoice_ = input("Type the name of a map or 'e' to exit: ").title()
                  print("\n")
              # ValueError check
              _playerchoice_ = float(_playerchoice_)
          except ValueError:
              # If the choice is not valid then this message prints
              if (_playerchoice_ not in self.map
                  and _playerchoice_ != "E"):
                  print("Type the name of a map or type 'e' to exit")
          else:
              # If the input was a number then this message prints
              print("Don't type a number")
          finally:
              # Checks if the player's choice in in the player's inventory
              if _playerchoice_ in self.map:
                  # If the choice was the first floor map
                  if _playerchoice_ == "Floor 1 Map":
                      # The file containing the map opens
                      with open('Labmap1.txt', "r") as file:
                          try:
                              # The map name and map prints
                              print(_playerchoice_)
                              print(file.read())
                          except:
                              # Error message prints
                              print("Something went wrong when trying to view the map")
                          finally:
                              # Prints a space
                              print("\n")


playeritems = Inventory([], {"Bandaid" : 10}, ["Floor 1 Map"])