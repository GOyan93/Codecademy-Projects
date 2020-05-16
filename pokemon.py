#! Python 3.6.9
"""
Title: Pokemon Battle Sim
Author: GOyan93
Initial Date: May 15, 2020
Description: This is a program that uses OOP to simulate the basic battle structure from the pokemon video games.
             This project is from codecademy but it is not build using walkthroughs.
             The game consists of 2 trainers with up to 6 pokemon that can battle those pokemon against each other.


"""
import random


  

class Pokemon:
  def __init__(self, name, level, pkm_type, max_hp, attack_range):
    self.name = name
    self.level = level
    self.pkm_type = pkm_type
    self.max_hp = max_hp
    self.current_hp = int(self.max_hp * (self.level * 0.25))
    self.has_fainted = False
    self.attack_range = [(int(i *(self.level * 0.15))) for i in attack_range]

  def __repr__(self):
    return (f'{self.name}, Level: {self.level}, Type: {self.pkm_type}, HP: {self.current_hp}, Attack: {self.attack_range}')

  def lose_health(self, health_loss):
    self.current_hp -= health_loss
    print(f'{self.name} lost {health_loss}HP.\n{self.name} has {self.current_hp}HP left.')
    if self.current_hp < 1:
      print(f'{self.name} has fainted.')
      self.has_fainted = True
    return self.current_hp

  def gain_health(self, health_gain):
    self.current_hp += health_gain
    print(f'{self.name} gained {health_gain}HP.\n{self.name} has {self.current_hp}HP.')

  def revive(self):
    self.current_hp = self.max_hp / 2
    print(f'{self.name} has been revived!\n{self.name} has {self.current_hp}.')

  def type_mult(self, other):
    if (self.pkm_type == 'fire' and other.pkm_type == 'grass') or (self.pkm_type == 'water' and other.pkm_type == 'fire') or (self.pkm_type == 'grass' and other.pkm_type == 'water'):
      print("It's super effective!")
      return 2
    if (self.pkm_type == 'grass' and other.pkm_type == 'fire') or (self.pkm_type == 'fire' and other.pkm_type == 'water') or (self.pkm_type == 'water' and other.pkm_type == 'grass'):
      print("It's not very effective!")
      return 0.5

  def attack(self, other_pkm):
    if self.has_fainted != True:
      print(f'{self.name} has attacked {other_pkm.name}!')
      attack_power = int(random.randint(self.attack_range[0], self.attack_range[1]) * self.type_mult(other_pkm))
      other_pkm.lose_health(attack_power)
    

  def display(self):
    print(f'{self.name}, Health: {self.current_hp}')


class Trainer:
  def __init__(self, name):
    self.name = name 
    self.pkm_balls = []
    self.num_of_pkballs = len(self.pkm_balls)
    self.active_pkm = active_pkm # 1-6

  def add_pkm(self, pkm):
    if self.num_of_pkballs < 6:
      self.pkm_balls.append(pkm)
      print(f'{pkm.name} has been added to your collection')
      
    else:
      print('You already have 6 pokemon. You cannot add any more.')
    
  def use_potion(self, pkm):
    pkm.gain_health(15)
    print(f'You have given {pkm.name} a potion!')

  def attack(self, other_pkm):
    self.active_pkm.attack(other_pkm)
    # This needs some editing?
    pass

  def switch_pkm(self, other_pkm):
    # Will change the index of the pkm_balls
    pass

  def run_away(self):
    trainer_input = input("Are you sure you want to run? (Yes or No)")
    if 'y' in trainer_input.lower():
      print('You have successfully run away')
      #replay function
    else:
      return None
    


# Pokemon Instances
bulbasaur = Pokemon('Bulbasaur', random.randint(1, 10), 'grass', 50, (5, 10))
charmander = Pokemon('Charmander', random.randint(1, 10), 'fire', 30, (9, 15))
squirtle = Pokemon('Squirtle', random.randint(1, 10), 'water', 40, (7, 12))



# Main Game Loop
bulbasaur.display()
charmander.display()
while bulbasaur.has_fainted == False and charmander.has_fainted == False:
  bulbasaur.attack(charmander)
  charmander.attack(bulbasaur)
 

print(bulbasaur)
print(charmander)
          

