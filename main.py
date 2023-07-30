import pygame
import random
import os
import sys
from SaveLoad import saveloadsystem
import time

# initialize the pygame
pygame.init()
saveload = saveloadsystem(".txt", "save_folder")

# create screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
duration = 3000

# Title and Icon
pygame.display.set_caption("A Budgeted Adventure")
icon = pygame.image.load('fighting-game.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('swordsman.png')
playerX = 350
playerY = 250
text_font = pygame.font.SysFont('Times New Roman', 26, italic=True)
text_font2 = pygame.font.SysFont('Lobster', 35, italic=True, bold=True)
text_font3 = pygame.font.SysFont('Times New Roman', 26, italic=True, bold=True)
Stats_font = pygame.font.SysFont('Comic Sans MS', 50, italic=True, bold=True)
Stats_font2 = pygame.font.SysFont('Times New Roman', 50, italic=True, bold=True)

def player():
    screen.blit(playerImg, (playerX, playerY))


# Drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Stats
stats = {'Health': 100, 'Speed': 10, 'Attack': 10, 'Defence': 10, 'Intelligence': 10, 'Mana': 10, 'Cash': 0, 'Level': 1, 'Exp required': 10, 'Exp gained': 0}
items = []
Attacks = []
global chose
chose = ''
Weapons_stats = {'Basic Sword': 10, 'Basic Wand': 10, 'Basic Glove': 10, 'Slime Knife': 15}
Weapons_increase = {'Basic Sword': 'Attack', 'Basic Wand': 'Mana', 'Basic Glove': 'Speed', 'Slime Knife': 'Attack'}
current_items = {'Headgear': None, 'Chest': None, 'Pants': None, 'Feet': None, 'Weapon': None}
current_event = None
villages = []
Boss_fights = []
count = 0
inventory = []
global difficulty_multiplier
difficulty_multiplier = 1


# button images
start_img = pygame.image.load('start-button.png')
arrow_img = pygame.image.load('arrow.png')
Instruction_Guide_img = pygame.image.load('Instruction guide.png')
Instruction_Guide_img = pygame.transform.scale(Instruction_Guide_img, (60, 60))
Sword_selection_img = pygame.image.load('SwordSelection.png')
Sword_selection_img = pygame.transform.scale(Sword_selection_img, (256, 256))
Wand_selection_img = pygame.image.load('WandSelection.png')
Wand_selection_img = pygame.transform.scale(Wand_selection_img, (256, 256))
Glove_selection_img = pygame.image.load('GloveSelection.png')
Glove_selection_img = pygame.transform.scale(Glove_selection_img, (256, 256))
Basic_Sword_img = pygame.image.load('BasicSword.png')
Basic_Wand_img = pygame.image.load('BasicWand.png')
Basic_Glove_img = pygame.image.load('BasicGlove.png')
Weapon_equip_img = pygame.image.load('Weapon_equip.png')
exit_img = pygame.image.load('Exit button.png')
Buying_defence_rune = pygame.image.load('Buy defence rune.png')
Buying_defence_rune = pygame.transform.scale(Buying_defence_rune, (256, 256))
Buying_mana_rune = pygame.image.load('Buy mana rune.png')
Buying_mana_rune = pygame.transform.scale(Buying_mana_rune, (256, 256))
Buying_health_rune = pygame.image.load('Buy health rune.png')
Buying_health_rune = pygame.transform.scale(Buying_health_rune, (256, 256))
Buying_attack_rune = pygame.image.load('Buy attack rune.png')
Buying_attack_rune = pygame.transform.scale(Buying_attack_rune, (256, 256))
Buying_intelligence_rune = pygame.image.load('Buy intelligence rune.png')
Buying_intelligence_rune = pygame.transform.scale(Buying_intelligence_rune, (256, 256))
Buying_speed_rune = pygame.image.load('Buy speed rune.png')
Buying_speed_rune = pygame.transform.scale(Buying_speed_rune, (256, 256))

# functions/Items buttons
StarterBag = pygame.image.load('StarterBag.png')
StarterBag = pygame.transform.scale(StarterBag, (150, 150))
OpenStarterBag = pygame.image.load('OpeningStartingBag.png')
OpenStarterBag = pygame.transform.scale(OpenStarterBag, (150, 150))
guide_img = pygame.image.load('guide.png')
Go_Forect_img = pygame.image.load('GoForest.png')
Go_Forect_img = pygame.transform.scale(Go_Forect_img, (256, 256))
Fight_Him_img = pygame.image.load('Fight against him.png')
Fight_Him_img = pygame.transform.scale(Fight_Him_img, (256, 256))
Return_To_Shop_img = pygame.image.load('Return to the shop.png')
Return_To_Shop_img = pygame.transform.scale(Return_To_Shop_img, (256, 256))
Continuing_Fight_img = pygame.image.load('Continue and Fight.png')
Continuing_Fight_img = pygame.transform.scale(Continuing_Fight_img, (256, 256))
event_folder_path = 'path/to/save/current_event.py'
item_folder_path = "path/to/item_folder"
attack_folder_path = "path/to/attack_folder"
if not os.path.exists(item_folder_path):
    os.makedirs(item_folder_path)
if not os.path.exists(attack_folder_path):
    os.makedirs(attack_folder_path)
if not os.path.exists(event_folder_path):
    os.makedirs(event_folder_path)
# Backgrounds
background1 = pygame.image.load('beginner town.png')
begin = pygame.transform.scale(background1, (800, 600))
background2 = pygame.image.load('glitched.png')
begin2 = pygame.transform.scale(background2, (800, 600))
background3 = pygame.image.load('inventory.png')
begin3 = pygame.transform.scale(background3, (800, 600))
background4 = pygame.image.load('Forest.png')
begin4 = pygame.transform.scale(background4, (800, 600))
background5 = pygame.image.load('Victory_screen.png')
begin5 = pygame.transform.scale(background5, (800, 600))
background6 = pygame.image.load('Defeat screen.png')
begin6 = pygame.transform.scale(background6, (800, 600))
background7 = pygame.image.load('Main Screen.png')
begin7 = pygame.transform.scale(background7, (800, 600))
background8 = pygame.image.load('Some time later.png')
begin8 = pygame.transform.scale(background8, (800, 600))
background9 = pygame.image.load('Silent Sanctum.png')
begin9 = pygame.transform.scale(background9, (800, 600))
background10 = pygame.image.load('Anciet Scroll.png')
begin10 = pygame.transform.scale(background10, (800, 600))
background11 = pygame.image.load('Ruins image.png')
begin11 = pygame.transform.scale(background11, (800, 600))
background12 = pygame.image.load('Map.png')
begin12 = pygame.transform.scale(background12, (800, 600))
background13 = pygame.image.load('Map of forest.png')
begin13 = pygame.transform.scale(background13, (800, 600))

# Monsters
Slime_img = pygame.image.load('Slime.png')
Imperial_spirit_img = pygame.image.load('Imperial Spirit.png')
Imperial_spirit_img = pygame.transform.scale(Imperial_spirit_img, (600, 600))
Grass_Bear_img = pygame.image.load('Grass bear.png')

# Set the transparency level (0-255, where 0 is fully transparent and 255 is fully opaque)
transparency = 128

# Set the rectangle dimensions and position
rect_width = 800
rect_height = 130
rect_x = (810 - rect_width)//2
rect_y = (1100 - rect_height)//2

# Create a surface with transparency
surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)

# Fill the surface with a translucent color (red with 50% opacity)
pygame.draw.rect(surface, (255, 255, 255, transparency), surface.get_rect())
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
CELL_SIZE = 60
GRID_COLS = 5
GRID_ROWS = 4
INVENTORY_WIDTH = CELL_SIZE * GRID_COLS
INVENTORY_HEIGHT = CELL_SIZE * GRID_ROWS

# Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
bag_button_rect = pygame.Rect(10, 10, 100, 50)

# Attack buttons
Slash_button_img = pygame.image.load('Slash_Attack.png')
Slash_button_img = pygame.transform.scale(Slash_button_img, (256, 256))
Taunt_img = pygame.image.load("Taunt.png")
Energy_Ball_img = pygame.image.load("Energy_Ball.png")
Energy_Ball_img = pygame.transform.scale(Energy_Ball_img, (256, 256))
Strong_Punch_img = pygame.image.load("Strong_Punch.png")
Strong_Punch_img = pygame.transform.scale(Strong_Punch_img, (256, 256))
Use_Potion_img = pygame.image.load("Use_Potion.png")
Use_Potion_img = pygame.transform.scale(Use_Potion_img, (256, 256))
Target_img = pygame.image.load("Target .png")

# Items
Slime_knife_img = pygame.image.load("Slime Knife.png")
jiggly_blob_img = pygame.image.load("Slime Jelly.png")
Slimeballs_img = pygame.image.load("Slimeball.png")
Blue_slimeballs_img = pygame.image.load('Blue Slimeball.png')
Slime_Soureign_Circlet = pygame.image.load("Slime Soverign's Circlet.png")

# Background music and sounds
sound_effect1 = pygame.mixer.Sound('Slash Sound.mp3')
global Background_tracks
Background_tracks = {
    'Opening': '07 Opening Theme.wav',
    'Town': 'Town Shop.wav',
    'Victory': 'Victory Theme.wav',
    'Losing': 'Game Over Theme.wav',
    'Battle 1': 'Battle 1 music.wav',
    'Battle 2': 'Battle 2 music.wav',
    'Battle 3': 'Battle 3 music.wav',
    # Add more locations and their corresponding music files
}
# Every location like fighting or the shop
global current_location
current_location = None
global current_music
current_music = None





class Player:
    def __init__(self, name, level):
        self.name = 'Adventurer'
        self.level = stats['Level']
        self.previouslevel = self.level
        self.max_health = stats['Health']
        self.current_health = self.max_health
        self.strength = stats['Attack']
        self.magic_capacity = stats['Mana']
        self.defence = stats['Defence']
        self.speed = stats['Speed']
        self.intelligence = stats['Intelligence']
        self.attacks = []
        self.debuffs = []
        self.cash = 0
        self.exp = 0
        self.exp_needed = 10
        self.level = 1
        self.alive = True
        self.turn = False
        self.attacking = False
        self.moves = {'Energy Ball': {'damage': self.strength + 20,
                                        'description': "", 'debuff': None},
            'Slash': {'damage': self.strength + 20,
                              'description': "", 'debuff': None},
            'Strong Punch': {'damage': self.strength + 20,
                                'description': "",
                                'debuff': None},
            'Fireball': {'damage': self.strength+10,
                             'description': "",
                             'debuff': 'Burn'},
            'Slow': {'damage': 0,
                             'description': "",
                             'debuff': 'Slow'}}
        self.debuff_duration = {
            'Stun': 2,  # The number of turns the stun debuff will last
            'Slow': 3 # Add other debuffs and their durations here
        }
        self.current_debuff = None
        self.debuff_timer = 0
        self.use_taunt = False
        self.crithit = False

    def add_attack(self, attack):
        self.attacks.append(attack)

    def apply_debuff(self, debuff, duration):
        draw_text(f"{self.name} (Level {self.level}) was hit by {debuff} that lasts {duration} turns", text_font3, (255, 255, 255), 10, 450)
        self.current_debuff = debuff
        self.debuff_timer = duration

    def update_debuff(self):
        if self.debuff_timer > 0:
            self.debuff_timer -= 1
            draw_text(f"{self.name} (Level {self.level}) is still {self.current_debuff}ed for {self.debuff_timer} turns",text_font3, (255, 255, 255), 10, 450)
        else:
            self.current_debuff = None

    def attack(self, target, target1, target_defence, move_name, crit, random_chance):
        self.crithit = False
        if self.current_debuff != None and self.current_debuff == 'Stun':
            print(f"{self.name} (Level {self.level}) is stunned and is unable to attack!")
            draw_text(f"{self.name} (Level {self.level}) is stunned and is unable to attack!", text_font3, (255, 255, 255), 10, 500)
        else:
            if move_name:
                draw_text(f"{self.name} (Level {self.level}) attacks {target} with {move_name}!", text_font3, (255, 255, 255), 10, 500)
                move = self.moves[move_name]
                if move['damage'] < target_defence:
                    damage = 0
                    debuff = move['debuff']
                    if debuff is not None:
                        target1.apply_debuff(debuff, self.debuff_duration[debuff])
                else:
                    damage = move['damage'] - target_defence
                    if crit == 1:
                        damage = move['damage'] * 1.5 - target_defence
                        self.crithit = True
                    if random_chance in [1, 2, 3, 4]:
                        debuff = move['debuff']
                        if debuff is not None:
                            target1.apply_debuff(debuff, self.debuff_duration[debuff])

    def take_damage(self, damage, target_crit_hit):
        if damage <= 0:
            damage_received = 5  # Minimum 5 damage when damage is 0 or less
            if target_crit_hit:
                damage_received = round(damage_received * 1.5)
                print(f"CRITICAL HIT! {self.name} took {damage_received} damage!")
                draw_text(f"CRITICAL HIT! {self.name} took {damage_received} damage!", text_font3, (255, 255, 255), 10, 550)
            else:
                print(f"{self.name} took {damage_received} damage!")
                draw_text(f"{self.name} (Level {self.level}) took {damage_received} damage!", text_font3, (255, 255, 255), 10, 550)
        else:
            if target_crit_hit:
                damage = round(damage * 1.5)
                print(f"CRITICAL HIT! {self.name} took {damage} damage!")
                draw_text(f"CRITICAL HIT! {self.name} took {damage} damage!", text_font3, (255, 255, 255), 10, 550)
            else:
                print(f"{self.name} took {damage} damage!")
                draw_text(f"{self.name} (Level {self.level}) took {damage} damage!", text_font3, (255, 255, 255), 10, 550)

            self.current_health -= damage
            self.current_health = max(self.current_health, 0)


    def update_stats(self, level):
        self.previouslevel = self.level
        self.name = 'Adventurer'
        self.level = stats['Level']
        self.max_health = stats['Health']
        self.current_health = self.max_health
        self.strength = stats['Attack']
        self.magic_capacity = stats['Mana']
        self.speed = stats['Speed']
        self.defence = stats['Defence']
        self.intelligence = stats['Intelligence']
        self.cash = stats['Cash']


class Slime:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_health = random.randint(14 * level, 15 * level)
        self.current_health = self.max_health
        self.defence = random.randint(2 * level, 3 * level)
        self.damage = random.randint(2 * level, 5 * level)
        self.speed = random.randint(2 * self.level, 5 * self.level)
        self.moves = {'Slime Shot': {'damage': self.damage,
                                        'description': "The slime gathers a giant mass of slimy substances and fires at the player."
                                                       "After getting hit, the player speed will be temporarily lowered."
                                                       , 'debuff': 'Slow'},
            'Tackle': {'damage': round(self.damage / 1.5),
                              'description': ""
                                             ""
                                             "", 'debuff': None},
            'Slap': {'damage': 30,
                                'description': ""
                                               "",
                                'debuff': None}}
        self.moveset = ['Slime Shot', 'Tackle', 'Slap']
        self.alive = True
        self.turn = False
        self.attacking = False
        self.taunted = False
        self.crithit = False
        self.debuff_duration = {
            'Stun': 2,  # The number of turns the stun debuff will last
            'Slow': 3,
        }
        self.current_debuff = None  # basically checking if the boss gets stunned or hit by other debuffs
        self.debuff_timer = 0

    def apply_debuff(self, debuff, duration):
        draw_text(f"{self.name} (Level {self.level}) was hit by {debuff} that lasts {duration} turns", text_font3, (255, 255, 255), 10, 450)
        self.current_debuff = debuff
        self.debuff_timer = duration

    def update_debuff(self):
        if self.debuff_timer > 0:
            self.debuff_timer -= 1
            draw_text(f"{self.name} (Level {self.level}) is still {self.current_debuff}ed for {self.debuff_timer}!", text_font3, (255, 255, 255), 10, 450)
        else:
            self.current_debuff = None

    def attack(self, target, target1, target_defence, move_name, crit, random_chance):
        self.crithit = False
        if self.current_debuff != None and self.current_debuff == 'Stun':
            print(f"{self.name} (Level {self.level}) is stunned and is unable to attack!")
            draw_text(f"{self.name} (Level {self.level}) is stunned and is unable to attack!", text_font3,
                      (255, 255, 255),
                      10, 500)
        else:
            if move_name:
                draw_text(f"{self.name} (Level {self.level}) attacks {target} with {move_name}!", text_font3, (255, 255, 255), 10, 500)
                move = self.moves[move_name]
                if move['damage'] < target_defence:
                    damage = 0
                    debuff = move['debuff']
                    if debuff is not None:
                        target1.apply_debuff(debuff, self.debuff_duration[debuff])


    def take_damage(self, damage, target_crit_hit):
        if damage <= 0:
            damage_received = 5  # Minimum 5 damage when damage is 0 or less
            if target_crit_hit:
                damage_received = round(damage_received * 1.5)
                print(f"CRITICAL HIT! {self.name} took {damage_received} damage!")
                draw_text(f"CRITICAL HIT! {self.name} took {damage_received} damage!", text_font3, (255, 255, 255), 10,
                          550)
            else:
                print(f"{self.name} took {damage_received} damage!")
                draw_text(f"{self.name} (Level {self.level}) took {damage_received} damage!", text_font3,
                          (255, 255, 255), 10, 550)
        else:
            if target_crit_hit:
                damage = round(damage * 1.5)
                print(f"CRITICAL HIT! {self.name} took {damage} damage!")
                draw_text(f"CRITICAL HIT! {self.name} took {damage} damage!", text_font3, (255, 255, 255), 10, 550)
            else:
                print(f"{self.name} took {damage} damage!")
                draw_text(f"{self.name} (Level {self.level}) took {damage} damage!", text_font3, (255, 255, 255), 10,
                          550)

            self.current_health -= damage
            self.current_health = max(self.current_health, 0)

class GrassBear:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_health = random.randint(5 * level, 10 * level)
        self.current_health = self.max_health
        self.defence = random.randint(1 * level, 2 * level)
        self.damage = random.randint(2 * level, 5 * level)
        self.speed = random.randint(2 * self.level, 5 * self.level)
        self.moves = {'Heavy Slash': {'damage': self.damage,
                                     'description': ""
                                                    ""
            , 'debuff': 'Slow'},
                      'Grassy Barrage': {'damage': round(self.damage / 1.5),
                                 'description': ""
                                                ""
                                                "", 'debuff': None},
                      'Razor Leaf': {'damage': 40,
                               'description': ""
                                              "",
                               'debuff': None}}
        self.moveset = ['Heavy Slash', 'Grassy Barrage', 'Razor Leaf']
        self.alive = True
        self.turn = False
        self.attacking = False
        self.taunted = False
        self.crithit = False
        self.debuff_duration = {
            'Stun': 2,  # The number of turns the stun debuff will last
            'Slow': 3,
        }
        self.current_debuff = None  # basically checking if the boss gets stunned or hit by other debuffs
        self.debuff_timer = 0



    def apply_debuff(self, debuff, duration):
        draw_text(f"{self.name} (Level {self.level}) was hit by {debuff} that lasts {duration} turns", text_font3, (255, 255, 255), 10, 450)
        self.current_debuff = debuff
        self.debuff_timer = duration

    def update_debuff(self):
        if self.debuff_timer > 0:
            self.debuff_timer -= 1
            draw_text(f"{self.name} (Level {self.level}) is still {self.current_debuff}ed for {self.debuff_timer}!", text_font3, (255, 255, 255), 10, 450)
        else:
            self.current_debuff = None

    def attack(self, target, target1, target_defence, move_name, crit, random_chance):
        self.crithit = False
        if self.current_debuff != None:
            print(f"{self.name} (Level {self.level}) is taunted and is unable to attack!")
            draw_text(f"{self.name} (Level {self.level}) is taunted and is unable to attack!", text_font3,
                      (255, 255, 255), 10, 500)
        else:
            if move_name:
                draw_text(f"{self.name} (Level {self.level}) attacks {target} with {move_name}!", text_font3,
                          (255, 255, 255), 10, 500)
                move = self.moves[move_name]
                damage = move['damage'] - target_defence
                if crit == 1:
                    damage = move['damage'] * 1.5 - target_defence
                    self.crithit = True
                if random_chance in [1, 2, 3, 4]:
                    debuff = move['debuff']
                    if debuff is not None:
                        target1.apply_debuff(debuff, self.debuff_duration[debuff])

    def take_damage(self, damage, target_crit_hit):
        if damage <= 0:
            damage_received = 5  # Minimum 5 damage when damage is 0 or less
            if target_crit_hit:
                damage_received = round(damage_received * 1.5)
                print(f"CRITICAL HIT! {self.name} took {damage_received} damage!")
                draw_text(f"CRITICAL HIT! {self.name} took {damage_received} damage!", text_font3, (255, 255, 255), 10,
                          550)
            else:
                print(f"{self.name} took {damage_received} damage!")
                draw_text(f"{self.name} (Level {self.level}) took {damage_received} damage!", text_font3,
                          (255, 255, 255), 10, 550)
        else:
            if target_crit_hit:
                damage = round(damage * 1.5)
                print(f"CRITICAL HIT! {self.name} took {damage} damage!")
                draw_text(f"CRITICAL HIT! {self.name} took {damage} damage!", text_font3, (255, 255, 255), 10, 550)
            else:
                print(f"{self.name} took {damage} damage!")
                draw_text(f"{self.name} (Level {self.level}) took {damage} damage!", text_font3, (255, 255, 255), 10,
                          550)

            self.current_health -= damage
            self.current_health = max(self.current_health, 0)

class Imperial_Spirit:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_health = random.randint(5 * level, 7 * level)
        self.current_health = self.max_health
        self.defence = random.randint(2 * level, 3 * level)
        self.damage = random.randint(2 * level, 3 * level)
        self.speed = random.randint(2 * self.level, 5 * self.level)
        self.moves = {'Spectral Dash': {'damage': self.damage + 30,
                                      'description': ""
                                                     ""
            , 'debuff': None},
                      'Haunting Wail': {'damage': self.damage // 2,
                                         'description': ""
                                                        ""
                                                        "", 'debuff': 'Slow'},
                      'Ethereal Chains': {'damage': 55,
                                     'description': ""
                                                    "",
                                     'debuff': None}}
        self.moveset = ['Spectral Dash', 'Haunting Wail', 'Ethereal Chains']
        self.alive = True
        self.turn = False
        self.attacking = False
        self.crithit = False
        self.use_taunt = False
        self.debuff_duration = {
            'Stun': 2,  # The number of turns the stun debuff will last
            'Slow': 3
        }
        self.current_debuff = None # basically checking if the boss gets stunned or hit by other debuffs
        self.debuff_timer = 0

    def attack(self, target, target1, target_defence, move_name, crit, random_chance):
        self.crithit = False
        if self.current_debuff != None:
            print(f"{self.name} (Level {self.level}) is taunted and is unable to attack!")
            draw_text(f"{self.name} (Level {self.level}) is taunted and is unable to attack!", text_font3,
                      (255, 255, 255), 10, 500)
        else:
            if move_name:
                draw_text(f"{self.name} (Level {self.level}) attacks {target} with {move_name}!", text_font3,
                          (255, 255, 255), 10, 500)
                move = self.moves[move_name]
                damage = move['damage'] - target_defence
                if crit == 1:
                    damage = move['damage'] * 1.5 - target_defence
                    self.crithit = True
                if random_chance in [1, 2, 3, 4]:
                    debuff = move['debuff']
                    if debuff is not None:
                        target1.apply_debuff(debuff, self.debuff_duration[debuff])

    def apply_debuff(self, debuff, duration):
        draw_text(f"{self.name} (Level {self.level}) was hit by {debuff} that lasts {duration} turns", text_font3, (255, 255, 255), 10, 450)
        self.current_debuff = debuff
        self.debuff_timer = duration

    def update_debuff(self):
        if self.debuff_timer > 0:
            self.debuff_timer -= 1
            draw_text(f"{self.name} (Level {self.level}) is still {self.current_debuff}ed for {self.debuff_timer}!", text_font3,(255, 255, 255), 10, 450)
        else:
            self.current_debuff = None

    def is_stunned(self):
        return self.current_debuff == 'Stun'

    def take_damage(self, damage, target_crit_hit):
        if damage <= 0:
            damage_received = 5  # Minimum 5 damage when damage is 0 or less
            if target_crit_hit:
                damage_received = round(damage_received * 1.5)
                print(f"CRITICAL HIT! {self.name} took {damage_received} damage!")
                draw_text(f"CRITICAL HIT! {self.name} took {damage_received} damage!", text_font3, (255, 255, 255), 10,
                          550)
            else:
                print(f"{self.name} took {damage_received} damage!")
                draw_text(f"{self.name} (Level {self.level}) took {damage_received} damage!", text_font3,
                          (255, 255, 255), 10, 550)
        else:
            if target_crit_hit:
                damage = round(damage * 1.5)
                print(f"CRITICAL HIT! {self.name} took {damage} damage!")
                draw_text(f"CRITICAL HIT! {self.name} took {damage} damage!", text_font3, (255, 255, 255), 10, 550)
            else:
                print(f"{self.name} took {damage} damage!")
                draw_text(f"{self.name} (Level {self.level}) took {damage} damage!", text_font3, (255, 255, 255), 10,
                          550)

            self.current_health -= damage
            self.current_health = max(self.current_health, 0)

# Get the turn order for every round
def calculate_turn_order(*entities):
    entity_list = []
    for entity in entities:
        name, speed = entity
        entity_list.append({"name": name, "speed": speed})
    entity_list.sort(key=lambda x: x["speed"], reverse=True)
    turn_order = []
    previous_speed = None
    for entity in entity_list:
        if entity["speed"] == previous_speed:
            coin_flip = random.choice([True, False])
            if coin_flip:
                turn_order.insert(0, entity["name"])  # Insert at the beginning
            else:
                turn_order.append(entity["name"])  # Append at the end
        else:
            turn_order.append(entity["name"])
        previous_speed = entity["speed"]
    return turn_order

def change_music(new_location):
    global current_music
    pygame.mixer.music.stop()  # Stop the current music
    current_music = Background_tracks[new_location]  # Get the new music file
    pygame.mixer.music.load(current_music)  # Load the new music
    pygame.mixer.music.play(-1)


def animate(frames, position, frame_duration):
    num_frames = len(frames)
    current_frame = 0
    frame_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        frame_timer += clock.get_time() / 1000.0  # Convert milliseconds to seconds
        if frame_timer >= frame_duration:
            current_frame = (current_frame + 1) % num_frames
            frame_timer = 0

        # Clear the window
        screen.fill((255, 255, 255))

        # Draw the current frame
        screen.blit(frames[current_frame], position)

        # Update the display
        pygame.display.flip()

        # Set the FPS
        clock.tick(60)

# This is for the slash sound effect
def play_sound_effect1():
    sound_effect1.set_volume(0.6)
    sound_effect1.play()

def Explore_Go():
    pygame.init()
    click = False
    while True:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin, (0, 0))
        screen.blit(surface, (rect_x, rect_y))
        draw_text("Let's start the adventure now.", text_font, (0, 0, 0), 10, 500)
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        if button1.collidepoint((mx, my)):
            if click:
                goingforest()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

def bag_screen2(screen, inventory): # Second bag screen for the second checkpoint
    pygame.init()
    running = True
    counter = 1
    click = False
    while running:
        screen.fill((196, 164, 132))
        screen.blit(begin3, (0, 0))
        button1 = screen.blit(exit_img, (750, 5))
        draw_text('Stats', Stats_font, (255, 255, 255), 420, 5)
        draw_text('Health: ' + str(stats['Health']), Stats_font2, (255, 255, 255), 380, 80)
        draw_text('Speed: ' + str(stats['Speed']), Stats_font2, (255, 255, 255), 380, 120)
        draw_text('Defence: ' + str(stats['Defence']), Stats_font2, (255, 255, 255), 380, 160)
        draw_text('Attack: ' + str(stats['Attack']), Stats_font2, (255, 255, 255), 380, 200)
        draw_text('Intelligence: ' + str(stats['Intelligence']), Stats_font2, (255, 255, 255), 380, 240)
        draw_text('Mana: ' + str(stats['Mana']), Stats_font2, (255, 255, 255), 380, 280)
        draw_text('Level: ' + str(stats['Level']), Stats_font2, (255, 255, 255), 380, 320)
        draw_text('EXP: ' + str(stats['Exp gained']) + ' / ' + str(stats['Exp required']), Stats_font2, (255, 255, 255), 380, 360)
        draw_text('Cash: ' + str(stats['Cash']), Stats_font2, (255, 255, 255), 380, 400)
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                Second_Checkpoint()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        for index in range(len(items)):
            if index % 4 == 0 and index != 0:
                counter += 1
            screen.blit(items[index], (10 + (index % 4) * 50, 5 + (index // 4) * 70 + 10 * counter))
        pygame.display.flip()
    clock.tick(30)

def bag_screen(screen, inventory): # The bag screen for the first checckpoint
    pygame.init()
    running = True
    counter = 1
    click = False
    while running:
        screen.fill((196, 164, 132))
        screen.blit(begin3, (0, 0))
        button1 = screen.blit(exit_img, (750, 5))
        draw_text('Stats', Stats_font, (255, 255, 255), 420, 5)
        draw_text('Health: ' + str(stats['Health']), Stats_font2, (255, 255, 255), 380, 80)
        draw_text('Speed: ' + str(stats['Speed']), Stats_font2, (255, 255, 255), 380, 120)
        draw_text('Defence: ' + str(stats['Defence']), Stats_font2, (255, 255, 255), 380, 160)
        draw_text('Attack: ' + str(stats['Attack']), Stats_font2, (255, 255, 255), 380, 200)
        draw_text('Intelligence: ' + str(stats['Intelligence']), Stats_font2, (255, 255, 255), 380, 240)
        draw_text('Mana: ' + str(stats['Mana']), Stats_font2, (255, 255, 255), 380, 280)
        draw_text('Level: ' + str(stats['Level']), Stats_font2, (255, 255, 255), 380, 320)
        draw_text('EXP: ' + str(stats['Exp gained']) + ' / ' + str(stats['Exp required']), Stats_font2, (255, 255, 255), 380, 360)
        draw_text('Cash: ' + str(stats['Cash']), Stats_font2, (255, 255, 255), 380, 400)
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                First_checkpoint()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        for index in range(len(items)):
            if index % 4 == 0 and index != 0:
                counter += 1
            screen.blit(items[index], (10 + (index % 4) * 50, 5 + (index // 4) * 70 + 10 * counter))
        pygame.display.flip()
    clock.tick(30)


def last_instructions(): # Last of the text in the bag tutorial part
    pygame.init()
    running = True
    counter = 1
    click = False
    while running:
        screen.fill((196, 164, 132))
        screen.blit(begin3, (0, 0))
        screen.blit(surface, (rect_x, rect_y))
        button1 = screen.blit(exit_img, (750, 5))
        draw_text('Stats', Stats_font, (255, 255, 255), 420, 5)
        draw_text('Health: ' + str(stats['Health']), Stats_font2, (255, 255, 255), 380, 80)
        draw_text('Speed: ' + str(stats['Speed']), Stats_font2, (255, 255, 255), 380, 120)
        draw_text('Defence: ' + str(stats['Defence']), Stats_font2, (255, 255, 255), 380, 160)
        draw_text('Attack: ' + str(stats['Attack']), Stats_font2, (255, 255, 255), 380, 200)
        draw_text('Intelligence: ' + str(stats['Intelligence']), Stats_font2, (255, 255, 255), 380, 240)
        draw_text('Mana: ' + str(stats['Mana']), Stats_font2, (255, 255, 255), 380, 280)
        draw_text('Level: ' + str(stats['Level']), Stats_font2, (255, 255, 255), 380, 320)
        draw_text('EXP: ' + str(stats['Exp gained']) + ' / ' + str(stats['Exp required']), Stats_font2, (255, 255, 255), 380, 360)
        draw_text('Cash: ' + str(stats['Cash']), Stats_font2, (255, 255, 255), 380, 400)
        draw_text("Ok I heard you! Enough talking for now... ", text_font, (0, 0, 0), 10, 500)
        draw_text("Click on the X button at the top right corner to exit the inventory.", text_font, (0, 0, 0), 10, 550)
        mx, my = pygame.mouse.get_pos()
        for index in range(len(items)):
            if index % 4 == 0 and index != 0:
                counter += 1
            screen.blit(items[index], (10 + (index % 4) * 50, 5 + (index // 4) * 70 + 10 * counter))
        pygame.display.flip()
        if button1.collidepoint((mx, my)):
            if click:
                Explore_Go()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        pygame.display.update()
        clock.tick(30)



def Equip_instructions(): # bag instructions part 1
    pygame.init()
    running = True
    counter = 1
    click = False
    while running:
        screen.fill((196, 164, 132))
        screen.blit(begin3, (0, 0))
        screen.blit(surface, (rect_x, rect_y))
        draw_text('Stats', Stats_font, (255, 255, 255), 420, 5)
        draw_text('Health: ' + str(stats['Health']), Stats_font2, (255, 255, 255), 380, 80)
        draw_text('Speed: ' + str(stats['Speed']), Stats_font2, (255, 255, 255), 380, 120)
        draw_text('Defence: ' + str(stats['Defence']), Stats_font2, (255, 255, 255), 380, 160)
        draw_text('Attack: ' + str(stats['Attack']), Stats_font2, (255, 255, 255), 380, 200)
        draw_text('Intelligence: ' + str(stats['Intelligence']), Stats_font2, (255, 255, 255), 380, 240)
        draw_text('Mana: ' + str(stats['Mana']), Stats_font2, (255, 255, 255), 380, 280)
        draw_text('Level: ' + str(stats['Level']), Stats_font2, (255, 255, 255), 380, 320)
        draw_text('EXP: ' + str(stats['Exp gained']) + ' / ' + str(stats['Exp required']), Stats_font2, (255, 255, 255), 380, 360)
        draw_text('Cash: ' + str(stats['Cash']), Stats_font2, (255, 255, 255), 380, 400)
        draw_text("Your stats are shown here.", text_font, (0, 0, 0), 10, 500)
        draw_text("As you fight, you will gain more cash.", text_font, (0, 0, 0), 10, 550)
        button1 = screen.blit(arrow_img, (700, 500))
        mx, my = pygame.mouse.get_pos()
        print(items)
        for index in range(len(items)):
            if index % 4 == 0 and index != 0:
                counter += 1
            screen.blit(items[index], (10 + (index % 4) * 50, 5 + (index // 4) * 70 + 10 * counter))
        pygame.display.flip()
        if button1.collidepoint((mx, my)):
            if click:
                last_instructions()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        pygame.display.update()
        clock.tick(30)

def invtutorial(screen, inventory): #Teaching people to click the bag
    pygame.init()
    click = False
    running = True  # Add a flag to control the loop
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin, (0, 0))
        screen.blit(surface, (rect_x, rect_y)) # make a semi transparent white box to put the text
        draw_text("Click the Bag at the top right side", text_font, (0, 0, 0), 10, 500)
        button1 = screen.blit(StarterBag, (700, 10))
        screen.blit(guide_img, (600, 50))
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            screen.blit(OpenStarterBag, (700, 10))
            if click:
                Equip_instructions()
                running = False  # Set the flag to False to exit the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.update()
        clock.tick(30)

def Selected_sword():
    pygame.init()
    click = False
    honk = True
    while True:
        screen.fill((0, 0, 0))
        screen.blit(Sword_selection_img, (50, 200))
        stats.update({'Attack': 20})
        stats.update({'Health': 120})
        draw_text("Selected sword", text_font, (255, 255, 255), 50, 350)
        draw_text("Received:", text_font, (255, 255, 255), 50, 400)
        draw_text("x1 Basic Sword", text_font, (255, 255, 255), 50, 450)
        if honk:
            items.append(Basic_Sword_img)
            player.add_attack("Slash")
            Attacks.append(Slash_button_img)
            player.update_stats(1)
            honk = False
        chose = 'Basic Sword'
        button1 = screen.blit(arrow_img, (700, 500))
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                invtutorial(screen, inventory)
        pygame.display.update()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(30)

def Selected_wand():
    pygame.init()
    click = False
    honk = True
    while True:
        screen.fill((0, 0, 0))
        screen.blit(Wand_selection_img, (250, 200))
        stats.update({'Mana': 20})
        stats.update({'Intelligence': 20})
        draw_text("Selected Wand", text_font, (255, 255, 255), 50, 350)
        draw_text("Received:", text_font, (255, 255, 255), 50, 400)
        draw_text("x1 Basic Wand", text_font, (255, 255, 255), 50, 450)
        if honk:
            player.add_attack("Energy Ball")
            items.append(Basic_Wand_img)
            Attacks.append(Energy_Ball_img)
            player.update_stats(1)
            honk = False
        print(items)
        chose = 'Basic Glove'
        button1 = screen.blit(arrow_img, (700, 500))
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                invtutorial(screen, inventory)
        pygame.display.update()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(30)

def Selected_glove():
    pygame.init()
    click = False
    update = True
    while True:
        screen.fill((0, 0, 0))
        screen.blit(Glove_selection_img, (450, 200))
        stats.update({'Speed': 20}) # increase speed stat to 20
        stats.update({'Attack': 20})
        draw_text("Selected Glove", text_font, (255, 255, 255), 50, 350)
        draw_text("Received:", text_font, (255, 255, 255), 50, 400)
        draw_text("x1 Basic Glove", text_font, (255, 255, 255), 50, 450)
        if update: # Make sure that this only run once
            player.add_attack("Strong Punch")
            items.append(Basic_Glove_img)
            Attacks.append(Strong_Punch_img)
            player.update_stats(1)
            update = False
        chose = 'Basic Glove'
        button1 = screen.blit(arrow_img, (700, 500))
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                invtutorial(screen, inventory)
        pygame.display.update()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(30)

def Selection(): # Selection of weapon
    pygame.init()
    click = False
    while True:
        screen.fill((0, 0, 0))
        button1 = screen.blit(Sword_selection_img, (50, 200))
        button2 = screen.blit(Wand_selection_img, (250, 200))
        button3 = screen.blit(Glove_selection_img, (450, 200))
        draw_text("Pick a weapon by clicking on one of the images", text_font, WHITE, 50, 350)
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                Selected_sword()
        elif button2.collidepoint((mx, my)):
            if click:
                Selected_wand()
        elif button3.collidepoint((mx, my)):
            if click:
                Selected_glove()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click2 = True
        # Update player position, handle collisions, etc.
        pygame.display.update()
        clock.tick(30)
def Before_selcction(): # Right before selecting a weapon
    pygame.init()
    current_event = Before_selcction
    click = False
    while True:
        screen.fill((0, 0, 0))
        screen.blit(begin, (0, 0))
        # Add your gameplay logic here
        screen.blit(surface, (rect_x, rect_y))
        draw_text("Let's equip ourselves.", text_font, (0, 0, 0), 10, 500)
        button1 = screen.blit(arrow_img, (700, 500))
        pygame.display.flip()
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                Selection()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # Update player position, handle collisions, etc.
        pygame.display.update()
        clock.tick(30)

def beginnertown():
    current_event = beginnertown
    click = False
    change_music('Town')
    while True:
        screen.fill((0, 0, 0))
        screen.blit(begin, (0, 0))
        # Add your gameplay logic here
        screen.blit(surface, (rect_x, rect_y))
        draw_text("*PLOP* Here you go.", text_font, (0, 0, 0), 10, 500)
        draw_text("Welcome to the town shop.", text_font, (0, 0, 0), 10, 550)
        draw_text("Emerald Village", text_font2, (255, 255, 255), 300, 50)
        button1 = screen.blit(arrow_img, (700, 500))
        pygame.display.flip()
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                Before_selcction()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # To quit pygame
                exit() # To exit the python system
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # Update player position, handle collisions, etc.
        pygame.display.update()
        clock.tick(30)

def Instructions_manual():
    pygame.init()
    click = False
    while True:
        screen.fill((0, 0, 0))
        draw_text("INSTRUCTION MANUAL:", text_font, (255, 255, 255), 20, 20)
        draw_text("1. Click the blue arrow button to move to the next screen!", text_font, (255, 255, 255), 20, 70)
        screen.blit(arrow_img, (20, 40))
        draw_text("2. After clicking the attack button, click on the enemy to attack!", text_font, (255, 255, 255), 20, 140)
        draw_text("Example: click the attack button then click the slime to attack", text_font, (255, 255, 255), 20, 190)
        draw_text("3. Click the bag icon to access your inventory and stats!", text_font, (255, 255, 255), 20, 240)
        screen.blit(StarterBag, (20, 215))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        if button1.collidepoint((mx, my)):
            if click:
                main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(30)

def main_menu():
    pygame.init()
    click = False
    current_event = 'Opening'
    current_music = Background_tracks[current_event]
    pygame.mixer.music.load(current_music)
    pygame.mixer.music.play(-1) # This is to play the music forever
    stats.update({'Health': 100}) #This is to reset all the stats to ensure that it doesnt bring over from the last round
    stats.update({'Speed': 10})
    stats.update({'Attack': 10})
    stats.update({'Defence': 10})
    stats.update({'Intelligence': 10})
    stats.update({'Mana': 10})
    stats.update({'Cash': 0})
    stats.update({'Level': 1})
    stats.update({'Exp required': 10})
    stats.update({'Exp gained': 0})
    items.clear()
    while True:
        screen.blit(begin7, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(start_img, (250, 430))
        button2 = screen.blit(Instruction_Guide_img, (500, 460))
        if button1.collidepoint((mx, my)):
            if click:
                startgame()
        if button2.collidepoint((mx, my)):
            if click:
                Instructions_manual()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(30)


def afterglitch():
    click = False
    while True:
        screen.fill((0, 0, 0))
        draw_text('This is the Tower of Azuris. You will meet monsters of all kind!', text_font, (255, 255, 255), 20, 390)
        draw_text('Your goal is to gain as much cash as possible!', text_font, (255, 255, 255), 20, 450)
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        if button1.collidepoint((mx, my)):
            if click:
                beginnertown()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(30)


# game loop
def startgame():
    pygame.init()
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        button1 = screen.blit(arrow_img, (700, 500))
        if button1.collidepoint((mx, my)):
            if click:
                afterglitch()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
        draw_text('Welcome Adventurer!', text_font, (255, 255, 255), 265, 390)
        pygame.display.update()
        clock.tick(30)






def Imperial_Boss_Fight():
    current_event = Imperial_Boss_Fight
    change_music('Battle 3')
    print('no')
    click = False
    killed = False
    not_done = True
    not_done2 = True
    not_done3 = True
    Turn = []
    counter = 0
    round_counter = 1
    still_turn = True
    not_over = True
    attack_clicked = False
    debuff_clicked = False
    select = False
    selected_opp = None
    honk = True
    once = True
    play = True
    play1 = True
    updateonce = True
    updateonce2 = True
    game_over = False
    win = False
    print(counter)
    imperial_spirit = Imperial_Spirit('Imperial Spirit', random.randint(15, 20)) # set the level and the name for the boss
    enemies = [imperial_spirit]
    entities = [('Player', player.speed)]
    for enemy in enemies:
        entities.append((enemy.name, enemy.speed))
    command = False
    while not_over:
        turn_order = calculate_turn_order(('Imperial Spirit', imperial_spirit.speed), ('Player', player.speed))
        draw_text("Reminder: To attack, click on a move before selecting an opponent!", text_font3, (255, 255, 255), 10,150)
        pygame.display.flip()
        pygame.display.update()
        time.sleep(1)
        print('1')

        def screenis():
            screen.fill((0, 0, 0))
            screen.blit(begin4, (0, 0))
            imperial_spirit_img = screen.blit(Imperial_spirit_img, (200, 190))
            draw_text('Imperial Spirit LVL ' + str(imperial_spirit.level), text_font, (255, 255, 255), 200, 250)
            draw_text(f"Health: {imperial_spirit.current_health} / {imperial_spirit.max_health}", text_font,
                      (255, 255, 255), 200, 300)
            draw_text(f"Player's Health: {player.current_health} / {player.max_health}", text_font,
                      (255, 255, 255), 500, 40)

        print('2')
        not_done = True
        not_done2 = True
        not_done3 = True
        screen.fill((0, 0, 0))
        screen.blit(begin4, (0, 0))
        imperial_spirit_img = screen.blit(Imperial_spirit_img, (200, 170))
        draw_text('Imperial Spirit LVL ' + str(imperial_spirit.level), text_font, (255, 255, 255), 200, 250)
        draw_text(f"Health: {imperial_spirit.current_health} / {imperial_spirit.max_health}", text_font,
                  (255, 255, 255), 200, 300)
        draw_text(f"Player's Health: {player.current_health} / {player.max_health}", text_font,
                  (255, 255, 255), 500, 40)
        if once:
            pygame.display.flip()
            pygame.display.update()
            clock.tick(30)
            once = False
        if game_over:
            break
        if honk:
            print(turn_order)
            print(imperial_spirit.speed)
            print(player.speed)
            honk = False
        for entity_name in turn_order:
            if entity_name == 'Player':
                if player.current_health <= 0:
                    if play1:
                        game_over = True
                        not_done2 = False
                        not_done = False
                        play1 = False
                    break
                while not_done:
                    draw_text("Player's turn: ", Stats_font2, (255, 255, 255), 20, 20)
                    button1 = screen.blit(Attacks[0], (30, 500))
                    mx, my = pygame.mouse.get_pos()
                    pygame.display.flip()
                    pygame.display.update()
                    clock.tick(30)
                    if player.current_debuff != None and player.current_debuff == 'Slow':
                        if updateonce:
                            player.update_debuff()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            pygame.time.delay(1000)
                            screenis()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            updateonce = False
                    elif player.current_debuff != None:
                        if updateonce:
                            player.update_debuff()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            pygame.time.delay(1000)
                            updateonce = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if button1.collidepoint((mx, my)):
                                    attack_clicked = True
                                    selected_opp = None
                                    select = False
                                if imperial_spirit_img.collidepoint((mx, my)):
                                    if attack_clicked:
                                        selected_opp = imperial_spirit
                                        select = True
                                        print('Selected Imperial Spirit')
                                        print(attack_clicked)
                        if event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                if attack_clicked and select:
                                    if selected_opp == imperial_spirit:
                                        attackchosen = player.attacks[0]
                                        player.attack('Imperial Spirit', imperial_spirit, imperial_spirit.defence, attackchosen,
                                                      random.randint(1, 10), random.randint(1, 10))
                                        play_sound_effect1()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        imperial_spirit.take_damage(player.moves[attackchosen]['damage'], player.crithit)
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        screenis()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        clock.tick(30)
                                        attack_clicked = False
                                        selected_opp = None
                                    attack_clicked = False
                                    selected_opp = None
                                    not_done = False
                                elif debuff_clicked and select:
                                    if selected_opp == imperial_spirit:
                                        player.attack('Imperial Spirit', imperial_spirit, imperial_spirit.defence, 'Stun',
                                                      random.randint(1, 10),
                                                      random.randint(1, 10))
                                        play_sound_effect1()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        debuff_clicked = False
                                        selected_opp = None
                                        not_done = False
            elif entity_name == 'Imperial Spirit':
                if imperial_spirit.current_health <= 0:
                    turn_order.remove('Imperial Spirit')
                    print("Imperial Spirit has been defeated!")
                    if play:
                        killed = True
                        not_done2 = False
                        play = False
                if player.current_health <= 0:
                    if play1:
                        game_over = True
                        not_done2 = False
                        not_done = False
                        play1 = False
                    break
                while not_done2:
                    print("Imperial Spirit's turn: ")
                    draw_text("Imperial Spirit's turn: ", Stats_font2, (255, 255, 255), 20, 20)
                    pygame.display.flip()
                    pygame.display.update()
                    if imperial_spirit.current_debuff != None and imperial_spirit.current_debuff == "Stun": # Checking if the boss is currently stunned
                        imperial_spirit.update_debuff()
                        pygame.display.flip()
                        pygame.display.update()
                        pygame.time.delay(1000)
                        screenis() # reset the screen
                        pygame.display.flip()
                        pygame.display.update()
                        clock.tick(30)
                    elif imperial_spirit.current_debuff != None:
                        imperial_spirit.update_debuff()
                        pygame.display.flip()
                        pygame.display.update()
                        time.sleep(1)
                    movechosen = random.choice(imperial_spirit.moveset)
                    imperial_spirit.attack('Player', player, player.defence, movechosen, random.randint(1, 10),
                                      random.randint(1, 10))
                    play_sound_effect1()
                    pygame.display.flip()
                    pygame.display.update()
                    pygame.time.delay(1000)
                    player.take_damage(imperial_spirit.moves[movechosen]['damage'], imperial_spirit.crithit)
                    pygame.display.update()
                    pygame.time.delay(1000)
                    screenis()
                    pygame.display.flip()
                    pygame.display.update()
                    clock.tick(30)
                    not_done2 = False
            if player.current_health <= 0:
                game_over = True
                break
        if killed:
            win = True
            break
    if win:
        Victoryscreen()
    elif game_over:
        Losescreen()



def Genocide_or_Pacifist():
    pygame.init()
    current_event = Genocide_or_Pacifist
    click = False
    running = True
    dice = random.randint(1, 2)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin11, (0, 0))
        mx, my = pygame.mouse.get_pos()
        screen.blit(surface, (rect_x, rect_y))
        button1 = screen.blit(Fight_Him_img, (400, 350))
        draw_text("Get ready your weapon in preparation against the Spirit!", text_font, (0, 0, 0), 10, 500)
        draw_text("READY, WALLOP!", text_font, (0, 0, 0), 10, 550)
        if button1.collidepoint((mx, my)):
            if click:
                Imperial_Boss_Fight()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

def Walk_Into_Ruinspart4():
    pygame.init()
    current_event = Walk_Into_Ruinspart4
    click = False
    running = True
    dice = random.randint(1, 2)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin11, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        screen.blit(surface, (rect_x, rect_y))
        draw_text("It stares at you with its eyes blazing with a fierce light. Out of nowhere,", text_font, (0, 0, 0), 10, 500)
        draw_text("the imperial spirit dashes at inhuman speeds at you!", text_font, (0, 0, 0), 10, 550)
        if button1.collidepoint((mx, my)):
            if click:
                Genocide_or_Pacifist()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Walk_Into_Ruinspart3():
    pygame.init()
    current_event = Walk_Into_Ruinspart3
    click = False
    running = True
    dice = random.randint(1, 2)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin11, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        screen.blit(surface, (rect_x, rect_y))
        draw_text("Materializing from the flames, the Imperial Spirit emerged. It flickered", text_font, (0, 0, 0), 10, 500)
        draw_text("with a haunting radiance, a testament to it's deep-rooted anger.", text_font, (0, 0, 0), 10, 550)
        if button1.collidepoint((mx, my)):
            if click:
                Walk_Into_Ruinspart4()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Walk_Into_Ruinspart2():
    pygame.init()
    current_event = Walk_Into_Ruinspart2
    click = False
    running = True
    dice = random.randint(1, 2)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin11, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        screen.blit(surface, (rect_x, rect_y))
        draw_text("The air crackled with ethereal energy and a faint melody came from", text_font, (0, 0, 0), 10, 500)
        draw_text("within the ruins.", text_font, (0, 0, 0), 10, 550)
        if button1.collidepoint((mx, my)):
            if click:
                Walk_Into_Ruinspart3()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Walk_Into_Ruinspart1():
    pygame.init()
    current_event = Walk_Into_Ruinspart1
    click = False
    running = True
    dice = random.randint(1, 2)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin11, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        screen.blit(surface, (rect_x, rect_y))
        draw_text("As your foot touched the ruins, mystical flames spewed from it ...", text_font, (0, 0, 0), 10, 500)
        if button1.collidepoint((mx, my)):
            if click:
                Walk_Into_Ruinspart2()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)





def Second_Checkpoint():
    pygame.init()
    current_event = Second_Checkpoint
    repeat = True
    running = True
    click = False
    while running:
        screen.fill((0, 0, 0))
        screen.blit(begin4, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(Return_To_Shop_img, (150, 350))
        button2 = screen.blit(Continuing_Fight_img, (450, 350))
        button3 = screen.blit(StarterBag, (700, 10))
        draw_text("Congrats! You have make it to the final round!", text_font3, (255, 255, 255), 20, 500)
        draw_text("You may want to visit the shop to boost your stats before the fight.", text_font3, (255, 255, 255), 20, 550)
        if button1.collidepoint((mx, my)):
            if click:
                Emerald_shop()
        if button2.collidepoint((mx, my)):
            if click:
                Walk_Into_Ruinspart1()
        if button3.collidepoint((mx, my)):
            screen.blit(OpenStarterBag, (700, 10))
            if click:
                bag_screen2(screen, inventory)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Advance_forward2():
    pygame.init()
    current_event = Advance_forward2
    change_music('Town')
    click = False
    stat_increase = 0
    repeat = True
    running = True
    while running:
        screen.fill((0, 0, 0))
        button1 = screen.blit(arrow_img, (700, 500))
        mx, my = pygame.mouse.get_pos()
        draw_text("YOU WIN!", Stats_font2, (255, 255, 255), 280, 50)

        if repeat:
            exp_gained = random.randint(50, 100)  # Random exp gained
            player.exp += exp_gained
            cash_gained = random.randint(200, 350)
            player.cash += cash_gained
            repeat = False

        if player.exp >= player.exp_needed:  # Use an if statement instead of while loop
            player.exp -= player.exp_needed
            player.exp_needed += 5  # Scale up exp_needed
            # Update player's stats based on level increase (if needed)
            pygame.time.delay(200)
            randomstat = random.choice(['Health', 'Speed', 'Attack', 'Defence'])
            stat_increase = random.randint(20, 30)
            stats.update({randomstat: stats[randomstat] + stat_increase})
            stats.update({'Level': player.level+1})
            stats.update({'Exp gained': player.exp})
            stats.update({'Exp required': player.exp_needed})
            stats.update({'Cash': player.cash})
            player.update_stats(player.level)

        draw_text(f"Adventurer gained {exp_gained} exp! {player.exp} / {player.exp_needed}", text_font3,
                  (255, 255, 255), 20, 400)

        if player.previouslevel != player.level:
            draw_text(f"Adventurer has leveled up to {player.level}! A random stat has increased!", text_font3,
                      (255, 255, 255), 20, 450)
            draw_text(f"Adventurer gained {cash_gained} cash!", text_font3, (255, 255, 255), 20, 500)
            draw_text("You can see the stat changes in the inventory", text_font3, (255, 255, 255), 20, 550)
        else:
            draw_text(f"Adventurer gained {cash_gained} cash!", text_font3, (255, 255, 255), 20, 450)
            draw_text("You can see the stat changes in the inventory", text_font3, (255, 255, 255), 20, 500)

        pygame.display.update()
        clock.tick(30)
        if button1.collidepoint((mx, my)):
            if click:
                Second_Checkpoint()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def FightingBear(): # Have not change it yet
    current_event = FightingBear
    change_music('Battle 2')
    print('no')
    click = False
    killed = False
    not_done = True
    not_done2 = True
    not_done3 = True
    Turn = []
    counter = 0
    round_counter = 1
    still_turn = True
    not_over = True
    attack_clicked = False
    debuff_clicked = False
    heal_clicked = False
    select = False
    selected_opp = None
    honk = True
    once = True
    play = True
    play1 = True
    updateonce = True
    updateonce2 = True
    game_over = False
    win = False
    print(counter)
    Grass_bear = GrassBear('Grass Bear', random.randint(8, 10))
    enemies = [Grass_bear]
    entities = [('Player', player.speed)]
    for enemy in enemies:
        entities.append((enemy.name, enemy.speed))
    command = False
    while not_over:
        turn_order = calculate_turn_order(('Grass Bear', Grass_bear.speed), ('Player', player.speed))
        draw_text("Reminder: To attack, click on a move before selecting an opponent!", text_font3, (255, 255, 255), 10, 150)
        pygame.display.flip()
        pygame.display.update()
        time.sleep(1)
        print('1')

        def screenis():
            screen.fill((0, 0, 0))
            screen.blit(begin4, (0, 0))
            grass_bear_opp = screen.blit(Grass_Bear_img, (350, 325))
            draw_text('Grass Bear LVL ' + str(Grass_bear.level), text_font, (255, 255, 255), 300, 200)
            draw_text(f"Health: {Grass_bear.current_health} / {Grass_bear.max_health}", text_font,
                      (255, 255, 255), 300, 250)
            draw_text(f"Player's Health: {player.current_health} / {player.max_health}", text_font,
                      (255, 255, 255), 500, 40)

        print('2')
        not_done = True
        not_done2 = True
        not_done3 = True
        screen.fill((0, 0, 0))
        screen.blit(begin4, (0, 0))
        grass_bear_opp = screen.blit(Grass_Bear_img, (300, 325))
        draw_text('Grass Bear LVL ' + str(Grass_bear.level), text_font, (255, 255, 255), 300, 200)
        draw_text(f"Health: {Grass_bear.current_health} / {Grass_bear.max_health}", text_font,
                  (255, 255, 255), 300, 250)
        draw_text(f"Player's Health: {player.current_health} / {player.max_health}", text_font,
                  (255, 255, 255), 500, 40)
        if once:
            pygame.display.flip()
            pygame.display.update()
            clock.tick(30)
            once = False
        if game_over:
            break
        if honk:
            print(turn_order)
            print(Grass_bear.speed)
            print(player.speed)
            honk = False
        for entity_name in turn_order:
            if entity_name == 'Player':
                if player.current_health <= 0:
                    if play1:
                        game_over = True
                        not_done2 = False
                        not_done = False
                        play1 = False
                    break
                while not_done:
                    draw_text("Player's turn: ", Stats_font2, (255, 255, 255), 20, 20)
                    button1 = screen.blit(Attacks[0], (30, 500))
                    mx, my = pygame.mouse.get_pos()
                    pygame.display.flip()
                    pygame.display.update()
                    clock.tick(30)
                    if player.current_debuff != None and player.current_debuff == 'Slow':
                        if updateonce:
                            player.update_debuff()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            pygame.time.delay(1000)
                            screenis()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            updateonce = False
                    elif player.current_debuff != None:
                        if updateonce:
                            player.update_debuff()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            pygame.time.delay(1000)
                            updateonce = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if button1.collidepoint((mx, my)):
                                    attack_clicked = True
                                    selected_opp = None
                                    select = False
                                if grass_bear_opp.collidepoint((mx, my)):
                                    if attack_clicked:
                                        selected_opp = Grass_bear
                                        select = True
                                        print('Selected Grass Bear')
                                        print(attack_clicked)
                                    elif debuff_clicked:
                                        selected_opp = Grass_bear
                                        select = True
                                        print('Selected Grass Bear')
                                        print(debuff_clicked)
                        if event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                if attack_clicked and select:
                                    if selected_opp == Grass_bear:
                                        attackchosen = player.attacks[0]
                                        player.attack('Grass Bear', Grass_bear, Grass_bear.defence, attackchosen,
                                                      random.randint(1, 10), random.randint(1, 10))
                                        play_sound_effect1()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        Grass_bear.take_damage(player.moves[attackchosen]['damage'], player.crithit)
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        screenis()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        clock.tick(30)
                                        attack_clicked = False
                                        selected_opp = None
                                    attack_clicked = False
                                    selected_opp = None
                                    not_done = False
                                elif debuff_clicked and select:
                                    if selected_opp == Grass_bear:
                                        player.attack('Grass Bear', Grass_bear, Grass_bear.defence, 'Stun', random.randint(1, 10),
                                                      random.randint(1, 10))
                                        play_sound_effect1()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        debuff_clicked = False
                                        selected_opp = None
                                        not_done = False
                                elif heal_clicked:
                                        player.heal()
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        screenis()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        clock.tick(30)
                                        heal_clicked = False  # Reset the heal_clicked flag after healing
                                        not_done = False
                updateonce = True
            elif entity_name == 'Grass Bear':
                if Grass_bear.current_health <= 0:
                    turn_order.remove('Grass Bear')
                    print("Grass Bear has been defeated!")
                    if play:
                        killed = True
                        not_done2 = False
                        play = False
                if player.current_health <= 0:
                    if play:
                        game_over = True
                        not_done2 = False
                        play = False
                    break
                while not_done2:
                    print("Grass Bear's turn: ")
                    draw_text("Grass Bear's turn: ", Stats_font2, (255, 255, 255), 20, 20)
                    pygame.display.flip()
                    pygame.display.update()
                    if Grass_bear.current_debuff != None and Grass_bear.current_debuff == "Stun":
                        Grass_bear.update_debuff()
                        pygame.display.flip()
                        pygame.display.update()
                        pygame.time.delay(1000)
                        screenis()
                        pygame.display.flip()
                        pygame.display.update()
                        clock.tick(30)
                    elif Grass_bear.current_debuff != None:
                        Grass_bear.update_debuff()
                        pygame.display.flip()
                        pygame.display.update()
                        time.sleep(1)
                    movechosen = random.choice(Grass_bear.moveset)
                    Grass_bear.attack('Player', player, player.defence, movechosen, random.randint(1, 10),
                                  random.randint(1, 10))
                    play_sound_effect1()
                    pygame.display.flip()
                    pygame.display.update()
                    pygame.time.delay(1000)
                    player.take_damage(Grass_bear.moves[movechosen]['damage'], Grass_bear.crithit)
                    pygame.display.update()
                    pygame.time.delay(1000)
                    screenis()
                    pygame.display.flip()
                    pygame.display.update()
                    clock.tick(30)
                    not_done2 = False
            if player.current_health <= 0:
                game_over = True
                not_done2 = False
                break
        if killed:
            win = True
            break
    if win:
        Advance_forward2()
    elif game_over:
        Losescreen()
def confrontmonster():
    pygame.init()
    current_event = confrontmonster
    click = False
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin4, (0, 0))
        screen.blit(surface, (rect_x, rect_y))
        draw_text("Oh no! A wild grass bear jumps out from nowhere!", text_font, (0, 0, 0), 10, 500)
        draw_text("Get ready for a fight! WALLOP!", text_font, (0, 0, 0), 10, 550)
        button1 = screen.blit(arrow_img, (700, 500))
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                FightingBear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

def slimemet():
    pygame.init()
    current_event = slimemet
    click = False
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin4, (0, 0))
        screen.blit(surface, (rect_x, rect_y))
        draw_text("Ahhhhh! Beware of the slime ahead! Get ready to fight!", text_font, (0, 0, 0), 10, 500)
        draw_text("READY, WALLOP!", text_font, (0, 0, 0), 10, 550)
        button1 = screen.blit(arrow_img, (700, 500))
        mx, my = pygame.mouse.get_pos()
        if button1.collidepoint((mx, my)):
            if click:
                command = True
                print('yes')
                slimeattacks()
                running = False
        button1 = screen.blit(arrow_img, (700, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

def Losescreen():
    pygame.init()
    current_event = Losescreen
    change_music('Losing')
    running = True
    click = False
    while running:
        screen.blit(begin6, (0, 0))
        mx, my = pygame.mouse.get_pos()
        draw_text(f"Difficulty 1 ", text_font3, (255, 255, 255), 250, 300)
        draw_text("Unfortunately, you lost all your cash!", text_font3, (255, 255, 255), 250, 350)
        draw_text("GOOD TRY!", text_font3, (255, 255, 255), 250, 400)
        button1 = screen.blit(arrow_img, (700, 500))
        if button1.collidepoint((mx, my)):
            if click:
                main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Victoryscreen():
    pygame.init()
    current_event = Losescreen
    change_music('Victory')
    running = True
    click = False
    while running:
        screen.blit(begin5, (0, 0))
        mx, my = pygame.mouse.get_pos()
        draw_text(f"Difficulty {difficulty_multiplier} ", text_font3, (255, 255, 255), 250, 300)
        draw_text(f"TOTAL CASH GAINED: {player.cash}", text_font3, (255, 255, 255), 250, 350)
        draw_text("GOOD TRY!", text_font3, (255, 255, 255), 250, 400)
        button1 = screen.blit(arrow_img, (700, 500))
        if button1.collidepoint((mx, my)):
            if click:
                main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Bought_speed_rune():
    pygame.init()
    current_event = Bought_speed_rune
    repeat = True
    running = True
    updateonce = True
    click = False
    dice = random.randint(1, 100)  # Generating a random number between 1 and 100
    effectiveness = {2: 'Legendary', 10: 'Epic', 20: 'Rare', 58: 'Common'}
    buffamount = {'Legendary': 50, 'Epic': 25, 'Rare': 15, 'Common': 10}
    while running:
        screen.fill((0, 0, 0))
        screen.blit(begin, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        # Getting the drop type based on the randomly generated number
        drop_type = None
        for percentage, rarity in effectiveness.items():
            if dice <= percentage:
                drop_type = rarity
                break
        if drop_type is None:
            drop_type = 'Common'  # Default to 'Common' if the random number is greater than 58

        draw_text(f"Received {drop_type} speed rune!", text_font3, (255, 255, 255), 20, 500)
        draw_text(f"Your speed stat has increased to {buffamount[drop_type]}", text_font3, (255, 255, 255), 20, 550)
        amount = buffamount[drop_type]
        if updateonce:
            stats.update({'Cash': player.cash - 100})
            stats.update({'Speed': player.speed+amount})
            player.update_stats(player.level)
            updateonce = False

        player.update_stats(player.level)
        if button1.collidepoint((mx, my)):
            if click:
                Emerald_shop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Bought_health_rune():
    pygame.init()
    current_event = Bought_health_rune
    repeat = True
    running = True
    updateonce = True
    click = False
    dice = random.randint(1, 100)  # Generating a random number between 1 and 100
    effectiveness = {2: 'Legendary', 10: 'Epic', 20: 'Rare', 58: 'Common'}
    buffamount = {'Legendary': 50, 'Epic': 25, 'Rare': 15, 'Common': 10}
    while running:
        screen.fill((0, 0, 0))
        screen.blit(begin, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        # Getting the drop type based on the randomly generated number
        drop_type = None
        for percentage, rarity in effectiveness.items():
            if dice <= percentage:
                drop_type = rarity
                break
        if drop_type is None:
            drop_type = 'Common'  # Default to 'Common' if the random number is greater than 58

        draw_text(f"Received {drop_type} health rune!", text_font3, (255, 255, 255), 20, 500)
        draw_text(f"Your health stat has increased to {buffamount[drop_type]}", text_font3, (255, 255, 255), 20, 550)
        amount = buffamount[drop_type]
        if updateonce:
            stats.update({'Cash': player.cash - 100})
            stats.update({'Health': player.max_health+amount})
            player.update_stats(player.level)
            updateonce = False

        player.update_stats(player.level)
        if button1.collidepoint((mx, my)):
            if click:
                Emerald_shop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

def Bought_defence_rune():
    pygame.init()
    current_event = Bought_defence_rune
    repeat = True
    running = True
    updateonce = True
    click = False
    dice = random.randint(1, 100)  # Generating a random number between 1 and 100
    effectiveness = {2: 'Legendary', 10: 'Epic', 20: 'Rare', 58: 'Common'}
    buffamount = {'Legendary': 50, 'Epic': 25, 'Rare': 15, 'Common': 10}
    while running:
        screen.fill((0, 0, 0))
        screen.blit(begin, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        # Getting the drop type based on the randomly generated number
        drop_type = None
        for percentage, rarity in effectiveness.items():
            if dice <= percentage:
                drop_type = rarity
                break
        if drop_type is None:
            drop_type = 'Common'  # Default to 'Common' if the random number is greater than 58

        draw_text(f"Received {drop_type} defence rune!", text_font3, (255, 255, 255), 20, 500)
        draw_text(f"Your defence stat has increased to {buffamount[drop_type]}", text_font3, (255, 255, 255), 20, 550)
        amount = buffamount[drop_type]
        if updateonce:
            stats.update({'Cash': player.cash-100})
            stats.update({'Defence': player.defence+amount})
            player.update_stats(player.level)
            updateonce = False
        player.update_stats(player.level)
        if button1.collidepoint((mx, my)):
            if click:
                Emerald_shop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Bought_attack_rune():
    pygame.init()
    current_event = Bought_attack_rune
    repeat = True
    click = False
    running = True
    updateonce = True
    dice = random.randint(1, 100)  # Generating a random number between 1 and 100
    effectiveness = {2: 'Legendary', 10: 'Epic', 20: 'Rare', 58: 'Common'}
    buffamount = {'Legendary': 50, 'Epic': 25, 'Rare': 15, 'Common': 10}
    while running:
        screen.fill((0, 0, 0))
        screen.blit(begin, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        # Getting the drop type based on the randomly generated number
        drop_type = None
        for percentage, rarity in effectiveness.items():
            if dice <= percentage:
                drop_type = rarity
                break
        if drop_type is None:
            drop_type = 'Common'  # Default to 'Common' if the random number is greater than 58

        draw_text(f"Received {drop_type} attack rune!", text_font3, (255, 255, 255), 20, 500)
        draw_text(f"Your attack stat has increased to {buffamount[drop_type]}", text_font3, (255, 255, 255), 20, 550)
        amount = buffamount[drop_type]
        if updateonce:
            stats.update({'Cash': player.cash-100})
            stats.update({'Attack': player.strength+amount})
            player.update_stats(player.level)
            updateonce = False
        if button1.collidepoint((mx, my)):
            if click:
                Emerald_shop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def Emerald_shop():
    pygame.init()
    current_event = Emerald_shop
    repeat = True
    click = False
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(begin, (0, 0))
        mx, my = pygame.mouse.get_pos()
        draw_text(f"Cash amount: {player.cash}", text_font, (0, 0, 0), 350, 40)
        draw_text("Each rune costs 100 cash", text_font, (0, 0, 0), 350, 100)
        button1 = screen.blit(Buying_attack_rune, (100, 200))
        button2 = screen.blit(Buying_speed_rune, (500, 400))
        button3 = screen.blit(Buying_defence_rune, (500, 200))
        button4 = screen.blit(Buying_health_rune, (100, 400))
        button5 = screen.blit(exit_img, (750, 20))
        if player.cash < 100:
            draw_text("Adventurer does not have enough cash to buy runes! ", text_font, (255, 255, 255), 20, 500)
            time.sleep(2)
            Second_Checkpoint()
        if button1.collidepoint((mx, my)):
            if click:
                Bought_attack_rune()
        if button2.collidepoint((mx, my)):
            if click:
                Bought_speed_rune()
        if button3.collidepoint((mx, my)):
            if click:
                Bought_defence_rune()
        if button4.collidepoint((mx, my)):
            if click:
                Bought_health_rune()
        if button5.collidepoint((mx, my)):
            if click:
                Second_Checkpoint()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def First_checkpoint():
    pygame.init()
    current_event = First_checkpoint
    repeat = True
    running = True
    click = False
    while running:
        screen.fill((0, 0, 0))
        screen.blit(begin4, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(Continuing_Fight_img, (350, 400))
        button2 = screen.blit(StarterBag, (700, 10))
        if button1.collidepoint((mx, my)):
            if click:
                confrontmonster()
        if button2.collidepoint((mx, my)):
            screen.blit(OpenStarterBag, (700, 10))
            if click:
                bag_screen(screen, inventory)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

Forest_Events = [slimemet]

player = Player('Adventurer', stats['Level'])
def Advance_forward():
    pygame.init()
    current_event = Advance_forward
    change_music('Town')
    click = False
    stat_increase = 0
    repeat = True
    running = True
    count = 0
    while running:
        screen.fill((0, 0, 0))
        button1 = screen.blit(arrow_img, (700, 500))
        mx, my = pygame.mouse.get_pos()
        draw_text("YOU WIN!", Stats_font2, (255, 255, 255), 280, 50)

        if repeat:
            exp_gained = random.randint(50, 100)  # Random exp gained
            player.exp += exp_gained
            cash_gained = random.randint(200, 350)
            player.cash += cash_gained
            repeat = False

        if player.exp >= player.exp_needed:  # Use an if statement instead of while loop
            player.exp -= player.exp_needed
            player.exp_needed += 5  # Scale up exp_needed
            # Update player's stats based on level increase (if needed)
            pygame.time.delay(200)
            randomstat = random.choice(['Health', 'Speed', 'Attack', 'Defence'])
            stat_increase = random.randint(20, 30)
            stats.update({randomstat: stats[randomstat] + stat_increase})
            stats.update({'Level': player.level+1})
            stats.update({'Exp gained': player.exp})
            stats.update({'Exp required': player.exp_needed})
            stats.update({'Cash': player.cash})
            player.update_stats(player.level)

        draw_text(f"Adventurer gained {exp_gained} exp! {player.exp} / {player.exp_needed}", text_font3,
                  (255, 255, 255), 20, 400)

        if player.previouslevel != player.level:
            draw_text(f"Adventurer has leveled up to {player.level}! A random stat has increased!", text_font3,
                      (255, 255, 255), 20, 450)
            draw_text(f"Adventurer gained {cash_gained} cash!", text_font3, (255, 255, 255), 20, 500)
            draw_text("You can see the stat changes in the inventory", text_font3, (255, 255, 255), 20, 550)
        else:
            draw_text(f"Adventurer gained {cash_gained} cash!", text_font3, (255, 255, 255), 20, 450)
            draw_text("You can see the stat changes in the inventory", text_font3, (255, 255, 255), 20, 500)
        pygame.display.update()
        clock.tick(30)
        if button1.collidepoint((mx, my)):
            if click:
                First_checkpoint()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
def slimeattacks():
    change_music('Battle 1')
    current_event = slimeattacks
    print('no')
    click = False
    killed = False
    not_done = True
    not_done2 = True
    Turn = []
    counter = 0
    round_counter = 1
    still_turn = True
    not_over = True
    attack_clicked = False
    debuff_clicked = False
    heal_clicked = False
    select = False
    selected_slime = None
    honk = True
    once = True
    play = True
    play1 = True
    updateonce = True
    updateonce2 = True
    print(counter)
    Slime1 = Slime('Slime 1', random.randint(3, 5))
    enemies = [Slime1]
    entities = [('Player', player.speed)]
    for enemy in enemies:
        entities.append((enemy.name, enemy.speed))
    command = False
    while not_over:
        turn_order = calculate_turn_order(('Slime 1', Slime1.speed), ('Player', player.speed))
        draw_text("Reminder: To attack, click on a move before selecting a slime!", text_font3, (255, 255, 255), 20, 150)
        pygame.display.flip()
        pygame.display.update()
        time.sleep(1)
        print('1')
        def screenis():
            screen.fill((0, 0, 0))
            screen.blit(begin4, (0, 0))
            slime1 = screen.blit(Slime_img, (270, 230))
            draw_text('Slime LVL ' + str(Slime1.level), text_font, (255, 255, 255), 300, 200)
            draw_text(f"Health: {Slime1.current_health} / {Slime1.max_health}", text_font,
                      (255, 255, 255), 300, 250)
            draw_text(f"Player's Health: {player.current_health} / {player.max_health}", text_font,
                      (255, 255, 255), 500, 40)
        print('2')
        not_done = True
        not_done2 = True
        screen.fill((0, 0, 0))
        screen.blit(begin4, (0, 0))
        slime1 = screen.blit(Slime_img, (270, 260))
        draw_text('Slime LVL ' + str(Slime1.level), text_font, (255, 255, 255), 300, 200)
        draw_text(f"Health: {Slime1.current_health} / {Slime1.max_health}", text_font,
                  (255, 255, 255), 300, 250)
        draw_text(f"Player's Health: {player.current_health} / {player.max_health}", text_font,
                  (255, 255, 255), 500, 40)
        if once:
            pygame.display.flip()
            pygame.display.update()
            clock.tick(30)
            once = False
        if honk:
            print(turn_order)
            print(Slime1.speed)
            print(player.speed)
            honk = False
        for entity_name in turn_order:
            if entity_name == 'Player':
                click = False
                while not_done:
                    draw_text("Player's turn: ", Stats_font2, (255, 255, 255), 20, 20)
                    button1 = screen.blit(Attacks[0], (30, 500))
                    mx, my = pygame.mouse.get_pos()
                    pygame.display.flip()
                    pygame.display.update()
                    clock.tick(30)
                    if player.current_debuff != None and player.current_debuff == 'Slow':
                        if updateonce:
                            player.update_debuff()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            pygame.time.delay(1000)
                            screenis()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            updateonce = False
                    elif player.current_debuff != None:
                        if updateonce:
                            player.update_debuff()
                            pygame.display.flip()
                            pygame.display.update()
                            clock.tick(30)
                            pygame.time.delay(1000)
                            updateonce = False
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if button1.collidepoint((mx, my)):
                                    attack_clicked = True
                                    selected_slime = None
                                    select = False
                                if slime1.collidepoint((mx, my)):
                                    if attack_clicked:
                                        selected_slime = Slime1
                                        select = True
                                        print('Selected Slime 1')
                                        print(attack_clicked)
                                    elif debuff_clicked:
                                        selected_slime = Slime1
                                        select = True
                                        print('Selected Slime 1')
                                        print(debuff_clicked)
                        if event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                if attack_clicked and select:
                                    if selected_slime == Slime1:
                                        attackchosen = player.attacks[0]
                                        player.attack('Slime 1', Slime1, Slime1.defence, attackchosen, random.randint(1, 10), random.randint(1, 10))
                                        play_sound_effect1()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        Slime1.take_damage(player.moves[attackchosen]['damage'], player.crithit)
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        screenis()
                                        pygame.display.flip()
                                        pygame.display.update()
                                        clock.tick(30)
                                        attack_clicked = False
                                        selected_slime = None
                                    attack_clicked = False
                                    selected_slime = None
                                    not_done = False
                                elif debuff_clicked and select:
                                    if selected_slime == Slime1:
                                        player.attack('Slime 1', Slime1, Slime1.defence, 'Stun', random.randint(1, 10), random.randint(1, 10))
                                        pygame.display.flip()
                                        pygame.display.update()
                                        pygame.time.delay(1000)
                                        debuff_clicked = False
                                        selected_slime = None
                                        not_done = False
                updateonce = True
            elif entity_name == 'Slime 1':
                if Slime1.current_health <= 0:
                    turn_order.remove('Slime 1')
                    print("Slime 1 has been defeated!")
                    if play:
                        killed = True
                        not_done2 = False
                        play = False
                while not_done2:
                    print("Slime 1's turn: ")
                    draw_text("Slime 1's turn: ", Stats_font2, (255, 255, 255), 20, 20)
                    pygame.display.flip()
                    pygame.display.update()
                    if Slime1.current_debuff != None and Slime1.current_debuff == "Stun":
                        Slime1.update_debuff()
                        pygame.display.flip()
                        pygame.display.update()
                        pygame.time.delay(1000)
                        screenis()
                        pygame.display.flip()
                        pygame.display.update()
                        clock.tick(30)
                    elif Slime1.current_debuff != None:
                        Slime1.update_debuff()
                        pygame.display.flip()
                        pygame.display.update()
                        time.sleep(1)
                    movechosen = random.choice(Slime1.moveset)
                    Slime1.attack('Player', player,  player.defence, movechosen, random.randint(1, 10), random.randint(1, 10))
                    play_sound_effect1()
                    pygame.display.flip()
                    pygame.display.update()
                    pygame.time.delay(1000)
                    player.take_damage(Slime1.moves[movechosen]['damage'], Slime1.crithit)
                    # player.take_damage((Slime1.moves[movechosen['damage']], Slime1.crithit))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    screenis()
                    pygame.display.flip()
                    pygame.display.update()
                    clock.tick(30)
                    not_done2 = False
            if player.current_health <= 0:
                game_over = True
                not_done2 = False
                break
        if killed:
            win = True
            break
    if win:
        Advance_forward()
    elif game_over:
        Losescreen()



def EnterForest():
    pygame.init()
    current_event = EnterForest
    click = False
    running = True
    dice = random.randint(1, 2)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin4, (0, 0))
        draw_text("Enchanted Forest", text_font2, (255, 255, 255), 300, 50)
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        if button1.collidepoint((mx, my)):
            if click:
                event = random.choice(Forest_Events)
                event()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)






def ChoseGoForest():
    pygame.init()
    click = False
    while True:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin, (0, 0))
        screen.blit(surface, (rect_x, rect_y))
        draw_text("You: Let's go!", text_font, (0, 0, 0), 10, 500)
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(arrow_img, (700, 500))
        if button1.collidepoint((mx, my)):
            if click:
                EnterForest()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)


def goingforest():
    pygame.init()
    click = False
    while True:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin, (0, 0))
        button1 = screen.blit(Go_Forect_img, (250, 350))
        mx, my = pygame.mouse.get_pos()
        screen.blit(surface, (rect_x, rect_y))
        if button1.collidepoint((mx, my)):
            if click:
                ChoseGoForest()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit Pygame properly
                exit()
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
                    exit()
                    return  # Exit the function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

main_menu()
#call the main_menu function

