import pygame
import random
import os
import sys
from SaveLoad import saveloadsystem
import time
import inspect

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
text_font = pygame.font.SysFont('Times New Roman', 25, italic=True)
text_font2 = pygame.font.SysFont('Lobster', 35, italic=True, bold=True)
text_font3 = pygame.font.SysFont('Times New Roman', 25, italic=True, bold=True)
Stats_font = pygame.font.SysFont('Comic Sans MS', 50, italic=True, bold=True)
Stats_font2 = pygame.font.SysFont('Times New Roman', 40, italic=True, bold=True)
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

# button images
start_img = pygame.image.load('start-button.png')
yes_img = pygame.image.load('YES.png')
load_img = pygame.image.load('load.png')
arrow_img = pygame.image.load('arrow.png')
back_arrow_img = pygame.image.load('Back-arrow.png')
home_img = pygame.image.load('home-button.png')
shop_img = pygame.image.load('shop.png')
card_img = pygame.image.load('adventurercard.png')
Sword_selection_img = pygame.image.load('SwordSelection.png')
Wand_selection_img = pygame.image.load('WandSelection.png')
Glove_selection_img = pygame.image.load('GloveSelection.png')
Basic_Sword_img = pygame.image.load('BasicSword.png')
Basic_Wand_img = pygame.image.load('BasicWand.png')
Basic_Glove_img = pygame.image.load('BasicGlove.png')
X_Button_img = pygame.image.load('X_Button.png')
Add_button_img = pygame.image.load('Add_button.png')
Weapon_equip_img = pygame.image.load('Weapon_equip.png')
exit_img = pygame.image.load('Exit button.png')
Village_icon = pygame.image.load('House_img.png')
Location_marker = pygame.image.load('location_marker.png')
Location_marker = pygame.transform.scale(Location_marker, (32, 32))

# functions/Items buttons
StarterBag = pygame.image.load('StarterBag.png')
OpenStarterBag = pygame.image.load('OpeningStartingBag.png')
guide_img = pygame.image.load('guide.png')
Explore_First_img = pygame.image.load('ExploreFirstOption.png')
Go_Forect_img = pygame.image.load('GoForest.png')
Confront_monster_img = pygame.image.load('Confront the monster.png')
Distract_it_img = pygame.image.load('Distract it.png')
Quickly_run_img = pygame.image.load('Quickly run away.png')
Run_Left_img = pygame.image.load('Run to left side.png')
Run_Right_img = pygame.image.load('Run to right side.png')
Run_Middle_img = pygame.image.load('Run to middle.png')
Climb_Tree_img = pygame.image.load('Climb the Tree.png')
Hide_behind_Tree_img = pygame.image.load('Hide behind the tree.png')
Play_dead_img = pygame.image.load('Play dead.png')
Jump_into_hole_img = pygame.image.load('Jump into hole.png')
Oak_Tree_img = pygame.image.load('Oak Tree.png')
Open_Chest_img = pygame.image.load('Open the chest.png')
Avoid_opening_chest_img = pygame.image.load('Avoid opening chest.png')
Enter_ruins_img = pygame.image.load('Enter the ruins.png')
Go_back_village_img = pygame.image.load('Go back to village first.png')
Fight_Him_img = pygame.image.load('Fight against him.png')
Talk_him_out_img = pygame.image.load('Talk him out.png')

item_folder_path = "path/to/item_folder"
attack_folder_path = "path/to/attack_folder"
if not os.path.exists(item_folder_path):
    os.makedirs(item_folder_path)
if not os.path.exists(attack_folder_path):
    os.makedirs(attack_folder_path)

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
Taunt_img = pygame.image.load("Taunt.png")
Energy_Ball_img = pygame.image.load("Energy_Ball.png")
Strong_Punch_img = pygame.image.load("Strong_Punch.png")
Use_Potion_img = pygame.image.load("Use_Potion.png")
Target_img = pygame.image.load("Target .png")

# Items
Slime_knife_img = pygame.image.load("Slime Knife.png")
jiggly_blob_img = pygame.image.load("Slime Jelly.png")
Slimeballs_img = pygame.image.load("Slimeball.png")
Blue_slimeballs_img = pygame.image.load('Blue Slimeball.png')
Slime_Soureign_Circlet = pygame.image.load("Slime Soverign's Circlet.png")

# Sprite_sheets
class Forest_Map:
    def __init__(self):
        self.InForest = False
        self.start = True
        self.area1 = True
        self.area2 = True
        self.area3 = True
        self.area4 = True
        self.area5 = True
        self.area6 = True
        self.area7 = True
        self.area8 = True
        self.area9 = True
        self.area10 = True
        self.area11 = True
        self.area12 = True
        self.explored = []
    def Reset(self):
        self.start = False
        self.area1 = False
        self.area2 = False
        self.area3 = False
        self.area4 = False
        self.area5 = False
        self.area6 = False
        self.area7 = False
        self.area8 = False
        self.area9 = False
        self.area10 = False
        self.area11 = False
        self.area12 = False
    def draw_current_location(self):
        if self.start:
            screen.blit(Location_marker, (378, 480))
        if self.area1:
            screen.blit(Location_marker, (378, 410))
        if self.area2:
            screen.blit(Location_marker, (264, 320))
        if self.area3:
            screen.blit(Location_marker, (378, 320))
        if self.area4:
            screen.blit(Location_marker, (499, 320))
        if self.area5:
            screen.blit(Location_marker, (145, 235))
        if self.area6:
            screen.blit(Location_marker, (264, 235))
        if self.area7:
            screen.blit(Location_marker, (378, 235))
        if self.area8:
            screen.blit(Location_marker, (499, 235))
        if self.area9:
            screen.blit(Location_marker, (615, 235))
        if self.area10:
            screen.blit(Location_marker, (264, 150))
        if self.area11:
            screen.blit(Location_marker, (378, 150))
        if self.area12:
            screen.blit(Location_marker, (499, 150))
    def explored_Area(self, area):
        self.explored.append(area)
forest_map = Forest_Map
def Village_Map():
    pass
def Forest_Map():
    current_event = Open_Map
    click = False
    running = True
    dice = random.randint(1, 2)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin13, (0, 0))
        forest_map().draw_current_location()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update_save()
                pygame.quit()  # Quit Pygame properly
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
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

def Open_Map():
    current_event = Open_Map
    click = False
    running = True
    dice = random.randint(1, 2)
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(begin12, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(Village_icon, (200, 220))
        button2 = screen.blit(Oak_Tree_img, (450, 200))
        if button1.collidepoint((mx, my)):
            if click:
                Village_Map()
        if button2.collidepoint((mx, my)):
            if click:
                Forest_Map()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update_save()
                pygame.quit()  # Quit Pygame properly
                return  # Exit the function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit Pygame properly
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
def update_save():
    click = False
    while True:
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        button1 = screen.blit(yes_img, (150, 400))
        draw_text('Save First?', text_font, (255, 255, 255), 220, 350)
        if button1.collidepoint((mx, my)):
            if click:
                saveload.save_game_data([stats], ["stats"])
                for i, surface in enumerate(items):
                    filename = os.path.join(item_folder_path, f"surface{i}.png")
                    pygame.image.save(surface, filename)
                for i, surface in enumerate(Attacks):
                    filename = os.path.join(attack_folder_path, f"surface{i}.png")
                    pygame.image.save(surface, filename)
                if current_event == None:
                    pass
                else:
                    source_code = inspect.getsource(current_event)
                current_event_file_path = "path/to/save/current_event.py"
                if not os.path.exists(current_event_file_path):
                    os.makedirs(current_event_file_path)
                with open(current_event_file_path, "w") as file:
                    file.write(source_code)
                print('Saved')
                pygame.quit()
                exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(30)
Open_Map()