#! Python 3.6.9
"""
Title: Pokemon Battle Sim
Author: GOyan93
Initial Date: May 15, 2020
Description: This is a program that uses OOP to simulate the basic battle structure from the pokemon video games.
             This project is from codecademy but it is not build using walkthroughs.
             The game consists of 2 trainers with up to 6 pokemon that can battle those pokemon against each other.


"""

# TODO Create main game structure
  # TODO Ask player for name (istantiate Trainers)
  # TODO Display Pokemon List
  # TODO Players choose pokemon (adds to pkm ball list)
    # TODO removes Pokemon from list OR instantiates Pokemon
  # TODO Choose pokeballs to create active pokemons
  # TODO While loop based off turn number (odd = player 1, even = player 2)
    # TODO Player chooses actions
  # TODO End Game when player has no active pokemon in pokeball list
# TODO Fix revive function




import random, sys, time


  

class Pokemon:
  global turn
  
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
    print(f'{self.name} lost {health_loss}HP.\n{self.name} has {self.current_hp}HP left.\n')
    if self.current_hp < 1:
      print(f'{self.name} has fainted.')
      self.has_fainted = True
    return self.current_hp

  def gain_health(self, health_gain):
    global turn
    self.current_hp += health_gain
    print(f'{self.name} gained {health_gain}HP.\n{self.name} has {self.current_hp}HP.\n')
    turn += 1

  def revive(self):
    global turn
    self.current_hp = self.max_hp / 2
    print(f'{self.name} has been revived!\n{self.name} has {self.current_hp}.\n')
    turn += 1

  def type_mult(self, other):
    if (self.pkm_type == 'fire' and other.pkm_type == 'grass') or (self.pkm_type == 'water' and other.pkm_type == 'fire') or (self.pkm_type == 'grass' and other.pkm_type == 'water'):
      print("It's super effective!\n")
      return 2
    if (self.pkm_type == 'grass' and other.pkm_type == 'fire') or (self.pkm_type == 'fire' and other.pkm_type == 'water') or (self.pkm_type == 'water' and other.pkm_type == 'grass'):
      print("It's not very effective!\n")
      return 0.5

  def attack(self, other_pkm):
    global turn
    if self.has_fainted != True:
      print(f'{self.name} has attacked {other_pkm.name}!\n')
      attack_power = int(random.randint(self.attack_range[0], self.attack_range[1]) * self.type_mult(other_pkm))
      other_pkm.lose_health(attack_power)
      turn += 1
      
  def display(self):
    print(f'{self.name}, Health: {self.current_hp}\n')


class Trainer:
  global turn
  
  def __init__(self, name):
    self.name = name 
    self.pkm_balls = []
    self.num_of_pkballs = len(self.pkm_balls)
    self.active_pkm = None
    self.potions = 3
    self.revives = 1
    self.fainted_pkm = []
    
  def add_pkm(self, pkm):
    if self.num_of_pkballs < 2:
      self.pkm_balls.append(pkm)
      print(f'{pkm.name} has been added to your collection.\n')
    else:
      print("You cannot add anymore pokemon!")
    
  def use_potion(self):
    global turn
    if self.potions > 0:
      print(f'You have given {self.active_pkm.name} a potion!\n')
      self.active_pkm.gain_health(15)
      self.potions -= 1
      turn += 1 
    print('You do not have any potions left.\n')

  def use_revive(self):
    # Display list of fainted pokemon
    # Remove pokemon from fainted list, append to active list
    # Restore 1/2 health, changed fainted status
    # Lower revive count
    if self.revives > 0 and pkm.current_health <= 0:
      self.pkm.gain_health(self.pkm.max_health * 0.5)
      self.revives -= 1
      print(f'You have revived {pkm.name}!\n')
    print('You do not have any revives left\n')

  def attack(self, other_pkm):
    if self.active_pkm.has_fainted == True:
      print('Your pokemon has fainted.\n')
      self.switch_pkm()
    self.active_pkm.attack(other_pkm)

  def switch_pkm(self):
    global turn
    print(self.pkm_balls)
    choice = input("Choose your pokemon (1-3):\n")
    if self.active_pkm != None:
      if self.active_pkm.has_fainted == True:
        self.fainted_pkm.append(self.active_pkm)
    self.active_pkm = self.pkm_balls[int(choice)-1]
    print(f"{self.active_pkm.name} I choose you!\n")
    turn += 1
    
    

  def run_away(self):
    trainer_input = input("Are you sure you want to run? (Yes or No)\n")
    if 'y' in trainer_input.lower():
      print('You have successfully run away')
      sys.exit()
      #replay function
    else:
      return None
    
  def display_pokeballs(self):
    pass
    #displays list of pokemon


# Game Function
def game_function():
  if turn % 2 != 0:
    player = player1
  else:
    player = player2
  
  print(f'{player.name}: Choose your action.\nAttack, Switch, Use Potion, Use Revive, Run')
  choice = input()
  if 'attack' in choice.lower():
    if player == player1:
      player.attack(player2.active_pkm)
    elif player == player2:
      player.attack(player1.active_pkm)
  if 'switch' in choice.lower():
    player.switch_pkm()
  if 'potion' in choice.lower():
    player.use_potion()
  if 'revive' in choice.lower():
    player.use_revive()
  if 'run' in choice.lower():
    player.run_away()
    




# Pokemon Instances
pokemon_list = []
bulbasaur = Pokemon('Bulbasaur', random.randint(5, 10), 'grass', 50, (5, 10))
pokemon_list.append(bulbasaur)
charmander = Pokemon('Charmander', random.randint(5, 10), 'fire', 30, (9, 15))
pokemon_list.append(charmander)
squirtle = Pokemon('Squirtle', random.randint(5, 10), 'water', 40, (7, 12))
pokemon_list.append(squirtle)





##### Game Sequence #####

# Get player name / instantiate Trainers
turn = 1
print('Player 1: What is your name?')
player1_name = input()
print('Player 2: What is your name?')
player2_name = input()
player1 = Trainer(player1_name)
player2 = Trainer(player2_name)
# Present pokemon choices
print('Choose your pokemon! (numerical choice)')
for i in range(len(pokemon_list)):
    num = i+1
    print(f'{num}: {pokemon_list[i]}\n')
pkm_idx = int(input())
player1.add_pkm(pokemon_list[pkm_idx-1])
for i in range(len(pokemon_list)):
    num = i+1
    print(f'{num}: {pokemon_list[i]}\n')
pkm_idx = int(input())
player2.add_pkm(pokemon_list[pkm_idx-1])
print('Lets Battle!')
# Ask which pokemon to battle
print('Choose your pokemon to battle')
player1.switch_pkm()
player2.switch_pkm()
# Start Main Game Loop

while (len(player1.pkm_balls) != 0 or player1.revives != 0 )and (len(player2.pkm_balls) != 0 or player2.revives != 0):
  game_function()
        








# Test
bulbasaur.display()
squirtle.display()
while bulbasaur.has_fainted == False and squirtle.has_fainted == False:
  bulbasaur.attack(squirtle)
  squirtle.attack(bulbasaur)
 

print(bulbasaur)
print(squirtle)
          

