#! Python 3.6.9
"""
Title: Pokemon Battle Sim
Author: GOyan93
Initial Date: May 15, 2020
Description: This is a program that uses OOP to simulate the basic battle structure from the pokemon video games.
             This project is from codecademy but it is not build using walkthroughs.
             The game consists of 2 trainers with up to 6 pokemon that can battle those pokemon against each other.


"""






import random, sys, time


  

class Pokemon:
  global turn
  
  def __init__(self, name, level, pkm_type, base_hp, attack_range, has_fainted = False):
    self.name = name
    self.level = level
    self.pkm_type = pkm_type
    self.base_hp = base_hp
    self.max_hp = int(self.base_hp * (self.level * 0.25))
    self.current_hp = self.max_hp
    self.has_fainted = has_fainted
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

  def gain_hp(self, health_gain):
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
    if (self.pkm_type == 'fire' and other.pkm_type == 'grass') or (self.pkm_type == 'water' and other.pkm_type == 'fire') or (self.pkm_type == 'grass' and other.pkm_type == 'water') or (self.pkm_type == 'electric' and other.pkm_type == 'water'):
      print("It's super effective!\n")
      return 2
    if (self.pkm_type == 'grass' and other.pkm_type == 'fire') or (self.pkm_type == 'fire' and other.pkm_type == 'water') or (self.pkm_type == 'water' and other.pkm_type == 'grass'):
      print("It's not very effective!\n")
      return 0.5
    return 1

  def attack(self, other_pkm):
    global turn
    if self.has_fainted != True:
      print(f'{self.name} has attacked {other_pkm.name}!\n')
      attack_power = int(random.randint(self.attack_range[0], self.attack_range[1]) * self.type_mult(other_pkm))
      other_pkm.lose_health(attack_power)
      turn += 1
    else:
      print("Your pokemon has fainted.")
      
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
    if self.num_of_pkballs < 7:
      self.pkm_balls.append(pkm)
      print(f'{pkm.name} has been added to your collection.\n')
    else:
      print("You cannot add anymore pokemon!")
    
  def use_potion(self):
    global turn
    if self.active_pkm.current_hp == self.active_pkm.max_hp:
      print('Your pokemon is already at max health.\n')
    elif self.potions > 0:
      print(f'You have given {self.active_pkm.name} a potion!\n')
      self.active_pkm.gain_hp(15)
      self.potions -= 1
      
    else:
      print('You do not have any potions left.\n')

  def use_revive(self):
    if len(self.fainted_pkm) > 0:
      print('Which pokemon would you like to revive? (1-6)')
      print(self.fainted_pkm)
      try:
        choice = int(input() - 1)
      except:
        print('Please type in a valid number. 1-9')
        choice = int(input() - 1)
      self.active_pkm = self.fainted_pkm[choice]
      if self.revives > 0 and self.active_pkm.current_hp <= 0:
        self.active_pkm.gain_hp(int(self.active_pkm.max_hp * 0.5))
        self.active_pkm.has_fainted = False
        self.fainted_pkm.remove(self.active_pkm)
        self.revives -= 1
        print(f'You have revived {self.active_pkm.name}!\n')
      else:
        print('You do not have any revives left\n')
    elif len(self.fainted_pkm) == 0:
      print('All of your pokemon are healthy.\n')
    

  def attack(self, other_pkm):
    if self.active_pkm.has_fainted == True:
      print('Your pokemon has fainted.\n')
      self.switch_pkm()
    else:
      self.active_pkm.attack(other_pkm)

  def switch_pkm(self):
    global turn
    global game_limit
    for i in range(len(self.pkm_balls)):
      choice = i + 1
      print(f'{choice}: {self.pkm_balls[i]}')
    try:
      choice = int(input("Choose your pokemon (1-6):\n"))
    except:
      print('Please type in a valid number. 1-9')
      choice = int(input("Choose your pokemon (1-6):\n"))
    try:
      if self.pkm_balls[int(choice)-1].current_hp < 0:
        print("This pokemon has fainted.\nChoose another pokemon.")
        for i in range(len(self.pkm_balls)):
          choice = i + 1
          print(f'{choice}: {self.pkm_balls[i]}')
        try:
          choice = int(input("Choose your pokemon (1-6):\n"))
        except:
          print('Please type in a valid number. 1-9')
          choice = int(input("Choose your pokemon (1-6):\n"))
    except IndexError:
      print(f'Please type a number within 1 and {game_limit}.')
      try:
        choice = int(input("Choose your pokemon (1-6):\n"))
      except:
        print('Please type in a valid number. 1-9')
        choice = int(input("Choose your pokemon (1-6):\n"))
    self.active_pkm = self.pkm_balls[int(choice)-1]
    print(f"{self.active_pkm.name} I choose you!\n")
    print(self.active_pkm)
    print('')
    turn += 1
      
  def run_away(self):
    trainer_input = input("Are you sure you want to run? (Yes or No)\n")
    if 'y' in trainer_input.lower():
      print('You have successfully run away')
      replay()
    else:
      return None
    
  def faint_check(self):
    global turn
    if self.active_pkm.has_fainted == True:
      self.fainted_pkm.append(self.active_pkm)
      if len(self.fainted_pkm) == game_limit:
        game_over()
        replay()
      print(f'{self.name}, please choose another pokemon.')
      turn += 1
      self.switch_pkm()
      


# Game Functions
def game_function():
  global turn
  if turn % 2 != 0:
    player = player1
  else:
    player = player2
  
  print(f'{player.name}: Choose your action.\nAttack, Switch, Use Potion, Use Revive, Run')
  choice = input()
  if 'attack' in choice.lower():
    if player == player1:
      player.attack(player2.active_pkm)
      player2.faint_check()
    elif player == player2:
      player.attack(player1.active_pkm)
      player1.faint_check()
  if 'switch' in choice.lower():
    player.switch_pkm()
  if 'potion' in choice.lower():
    player.use_potion()
  if 'revive' in choice.lower():
    player.use_revive()
  if 'run' in choice.lower():
    player.run_away()
    

def game_over():
  if turn % 2 != 0:
    print(f'{player2.name} has won!\n\n')
    time.sleep(0.5)
    replay()
  else:
    print(f'{player1.name} has won!\n\n')
    time.sleep(0.5)
    replay()
    
def replay():
  global turn
  print("Would you like to play again?")
  choice = input()
  if choice[:1].lower() == 'y':
    turn = 1
    player1.pkm_balls = []
    player1.fainted_pkm = []
    player1.potions = 3
    player1.revives = 1
    player2.pkm_balls = []
    player2.fainted_pkm = []
    player2.potions = 3
    player2.revives = 1
    pkm_init()
    start_game()
  if choice.lower() == 'no':
    print("Thank you for playing!")
    sys.exit()

def start_game():
  global game_limit
  print('How many pokemon would you like to play with? (Max 6)')
  try:
    num_of_pkm = int(input())
  except:
    print('Please type in a valid number. 1-6')
    num_of_pkm = int(input())
  if 0 < num_of_pkm > 6:
    print('Please choose a number between 1-6.')
    num_of_pkm = int(input())
  game_limit = num_of_pkm
  while num_of_pkm != 0:
  # Present pokemon choices
    print(f'{player1.name}, choose your pokemon! (numerical choice)')
    for i in range(len(pokemon_list)):
        num = i+1
        print(f'{num}: {pokemon_list[i]}\n')
    try:
      pkm_idx = int(input())
    except ValueError or TypeError:
      print('Please type in a valid number. 1-9')
      pkm_idx = int(input())
    try:
      player1.add_pkm(pokemon_list[pkm_idx-1])
    except IndexError:
      print('Please type a number within 1 and {num_of_pkm}.')
      pkm_idx = int(input())
      player1.add_pkm(pokemon_list[pkm_idx-1])
    pokemon_list.remove(pokemon_list[pkm_idx-1])
    print(f'{player2.name}, choose your pokemon! (numerical choice)')
    for i in range(len(pokemon_list)):
        num = i+1
        print(f'{num}: {pokemon_list[i]}\n')
    try:
      pkm_idx = int(input())
    except ValueError or TypeError:
      print('Please type in a valid number. 1-9')
      pkm_idx = int(input())
    try:
      player2.add_pkm(pokemon_list[pkm_idx-1])
    except IndexError:
      print('Please type a number within 1 and {num_of_pkm}.')
      pkm_idx = int(input())
      player2.add_pkm(pokemon_list[pkm_idx-1])
    pokemon_list.remove(pokemon_list[pkm_idx-1])
    num_of_pkm -= 1
  print('Lets Battle!')
  # Ask which pokemon to battle
  print(f'{player1.name}, choose which pokemon to battle with! (numerical choice)')
  player1.switch_pkm()
  print(f'{player2.name}, choose which pokemon to battle with! (numerical choice)')
  player2.switch_pkm()
  while True:
    game_function()

        

# Pokemon Instances
# TODO Add more pokemon
# Remove selected pokemon from list.
def pkm_init():
  global pokemon_list
  pokemon_list = []
  bulbasaur = Pokemon('Bulbasaur', random.randint(5, 10), 'grass', 50, (5, 10))
  pokemon_list.append(bulbasaur)
  bulbasaur1 = Pokemon('Bulbasaur', random.randint(5, 10), 'grass', 50, (5, 10))
  pokemon_list.append(bulbasaur1)
  charmander = Pokemon('Charmander', random.randint(5, 10), 'fire', 30, (9, 15))
  pokemon_list.append(charmander)
  charmander1 = Pokemon('Charmander', random.randint(5, 10), 'fire', 30, (9, 15))
  pokemon_list.append(charmander1)
  squirtle = Pokemon('Squirtle', random.randint(5, 10), 'water', 40, (7, 12))
  pokemon_list.append(squirtle)
  squirtle1 = Pokemon('Squirtle', random.randint(5, 10), 'water', 40, (7, 12))
  pokemon_list.append(squirtle1)
  pikachu = Pokemon('Pikachu', random.randint(5, 10), 'electric', 35, (8, 13))
  pokemon_list.append(pikachu)
  pikachu1 = Pokemon('Pikachu', random.randint(5, 10), 'electric', 35, (8, 13))
  pokemon_list.append(pikachu1)
  





##### Game Sequence #####

print("""
POKEMON BATTLE SIM!
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
RULES:
- Each player enters their name.
- Choose the number of pokemon that you would like to play with.
- Each player will get to choose a pokemon from the list. After a pokemon is chosen, it is removed from the list.
- Each player will then choose which pokemon they want to battle with.
- The player will be presented with a set of choices:
      - Attack: Attacks the opposing players pokemon.
      - Switch: Player can switch pokemon. A turn will be used.
      - Use potion: Heals the pokemon by 15 HP. Each player only has 3 potions.
      - Use revive: Revives 1 fainted pokemon, restoring 1/2 their health. Only 1 revive per player.
      - Run: Used to run away from the battle and ends the game.

- Once all of a players pokemon have fainted and their revives are used up, the game is over.
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

********LET'S BATTLE!********
""")


# Get player name / instantiate Trainers
turn = 1
pkm_init()
print('Player 1: What is your name?')
player1_name = input()
print('Player 2: What is your name?')
player2_name = input()
player1 = Trainer(player1_name)
player2 = Trainer(player2_name)
start_game()

# Start Main Game Loop











