#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Stats Module
"""Contains class that encapsulates the player's stats"""
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import initialize

class Player:

    def __init__(self, health, weapons, equipweap, x_loc, y_loc):
        self.health = health
        self.weapons = weapons
        self.equipweap = equipweap
        self.x_loc = x_loc
        self.y_loc = y_loc


player = Player(initialize._playerhealth_, 
               initialize._playerweapons_,
               initialize._playereqweapon_,
               initialize._playerx_,
               initialize._playery_)

