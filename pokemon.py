#! Python 3.6.9
"""
Title: Pokemon Battle Sim
Author: GOyan93
Initial Date: May 15, 2020
Description: This is a program that uses OOP to simulate the basic battle structure from the pokemon video games.
             This project is from codecademy but it is not build using walkthroughs.
             The game consists of 2 trainers with up to 6 pokemon that can battle those pokemon against each other.


"""

class pokemon:
  def __init__(self, name, level, element, max_hp, current_hp, faint = False):
    self.name = name
    self.level = level
    self.element = element
    self.max_hp = max_hp
    self.current_hp = current_hp
    self.faint = faint

  def lose_health(self):
    pass

  def gain_health(self):
    pass

  def has_fainted(self):
    pass

  def revive(self):
    pass

  def attack(self, other_pokemon):
    pass

class Trainer:
  def __init__(self, name, num_of_pkm = 1, active_pkm = 1):
    self.name = name
    self.num_of_pkm = num_of_pkm # max 6
    self.active_pkm = active_pkm # 1-6

  def use_potion(self):
    pass

  def attack(self):
    pass

  def switch_pkm(self, other_pkm):
    pass

