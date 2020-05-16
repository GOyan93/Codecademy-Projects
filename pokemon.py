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

  def lose_health(self, health_loss):
    self.current_hp -= health_loss
    print(f'{self.name} lost {health_loss}HP.\n{self.name} has {self.current_hp}HP left.')
    self.has_fainted()
    return self.current_hp

  def gain_health(self, health_gain):
    self.current_hp += health_gain
    print(f'{self.name} gained {health_gain}HP.\n{self.name} has {self.current_hp}HP.')

  def has_fainted(self):
    if self.current_hp == 0:
      print(f'{self.name} has fainted.')
      return True
    return False

  def revive(self):
    self.current_hp = self.max_hp / 2
    print(f'{self.name} has been revived!\n{self.name} has {self.current_hp}.')

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

