import pygame, sys
from pygame.locals import *
import random
import tkinter
import PlayerClass
import ComputerClass
import CompAIClass
import OptionsClass
import StartUpFunctions
import HelperFunctions
import PlayerTurn
import ComputerTurn
from time import sleep

# Special condition for going back 3 spaces and landing on income tax, Make vari to stop double or triple draw of chance cards when player enters trade
# or leaves it. Blit issue when comps roll doubles

# Put players in list and other things in seperate lists and pass that instead of long list of arguments. (Player, comp1, comp2) (screen, token, background, etc)
# Allow player to choose how many people can play max 4. If player choses 3 there will be comp3 and 4 items in list, ComputerTurn will handle all computers turn.
# The size of the list will determine how many ifs are needed to act as a turn for each computer. Each cycle will be the same except for list.compX

# Two sounds: one for player turn as backgroud music and another for comps

# ---------------------------- S T A R T  U P ---------------------Start
# Initialize all pygame objs
pygame.init()

# Create sound obj from pygame
backMusic= pygame.mixer.music
# Pass the audio to 'load' method
backMusic.load('Monopoly Tycoon.wav')
# Lower the default volume
backMusic.set_volume(.3)
# Play the background music indefinetly
backMusic.play(-1, 0.0)

# Holds the x-coordinate pixel location of each property location
BoardxPoints= [603,551,516,478,442,405,368,333,297,261,212,
               195,195,195,195,195,195,195,195,195,195,
               250,287,322,361,395,431,466,501,538,584,
               598,598,598,598,598,598,598,598,598]

# Holds the y-coordinate pixel location of each property location
BoardyPoints= [471,471,471,471,471,471,471,471,471,471,471,
               419,387,347,310,275,237,199,166,130,77,
               70,70,70,70,70,70,70,70,70,80,
               124,160,197,230,270,304,339,376,413]

# Holds the space/index location of each property
# EX: if the player is on 'GO' the player location will be '0'. The index '0' is used in both 'BoardPoint' list
        # to determine the pixel location of the player token
Property_LocationDict= {0:'GO', 1:'Mediterranean Avenue', 2:'Community Chest', 3:'Baltic Avenue', 4:'Income Tax',
           5:'Reading Railroad', 6:'Oriental Avenue', 7:'Chance', 8:'Vermont Avenue', 9:'Connecticut Avenue',
           10:'Just Visiting', 11:'St. Charles Place', 12:'Electric Company', 13:'States Avenue', 14:'Virginia Avenue',
           15:'Pennsylvania Railroad', 16:'St. James Place', 17:'Community Chest', 18:'Tennessee Avenue', 19:'New York Avenue',
           20:'Free Parking', 21:'Kentucky Avenue', 22:'Chance', 23:'Indiana Avenue', 24:'Illinois Avenue',
           25:'B. & O. Railroad', 26:'Atlantic Avenue', 27:'Ventor Avenue', 28:'Water Works', 29:'Marvin Gardens',
           30:'Go To Jail', 31:'Pacific Avenue', 32:'North Carolina Avenue', 33:'Community Chest', 34:'Pennsylvania Avenue',
           35:'Short Line', 36:'Chance', 37:'Park Place', 38:'Luxury Tax', 39:'Boardwalk'}

# Create player obj
play= PlayerClass.Player()
# Get the player to enter name and choose token
play.StartingGUI()

# Create compter 1 & 2 objs
Danny= ComputerClass.Computer('Danny')
Jane= ComputerClass.Computer('Jane')

# The comp tokens are based on what token the player chooses
if play.get_token() == 'Hat':
    Danny.set_token('Cat')
    print("Danny's token is the 'Cat'.")
    Jane.set_token('Car')
    print("Jane's token is the 'Car'.")
    
elif play.get_token() == 'Cat':
    Danny.set_token('Hat')
    print("Danny's token is the 'hat'.")
    Jane.set_token('Car')
    print("Jane's token is the 'Car'.")
    
elif play.get_token() == 'Car':
    Danny.set_token('Cat')
    print("Danny's token is the 'Cat'.")
    Jane.set_token('Hat')
    print("Janes's token is the 'Hat'.")

turn = 'PlayerTurn'

# Display screen to match the size of the background image
screen = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption('Monopoly Game')

# Get background image, convert it and blit to screen
back='Mod Monopoly board.jpg'
background = pygame.image.load(back).convert()
screen.blit(background, (0,0))

# Create Hat token and blit to screen
hat='MonoHat.jpg'
hattoken= pygame.image.load(hat).convert()
screen.blit(hattoken, (575,450))
    
# Create Cat token and blit to screen
cat='MonoCat.jpg'
cattoken= pygame.image.load(cat).convert()
screen.blit(cattoken, (575,477))
    
# Create Car token and blit to screen
car='MonoCar.jpg'
cartoken= pygame.image.load(car).convert()
screen.blit(cartoken, (607,461))
    
# Blit text
font = pygame.font.Font(None, 36)
text1= font.render(Danny.get_name(), 1, (255, 255, 255))
screen.blit(text1, (655,20))
num1 = font.render(format(Danny.get_money(), ',d'), 1, (255, 255, 255))
screen.blit(num1, (673, 70))

text2= font.render(Jane.get_name(), 1, (255, 255, 255))
screen.blit(text2, (8,14))
num2 = font.render(format(Jane.get_money(), ',d'), 1, (255, 255, 255))
screen.blit(num2, (8, 67))

text = font.render(play.get_name(), 1, (255, 255, 255))
screen.blit(text, (642,555))
num = font.render(format(play.get_money(), ',d'), 1, (255, 255, 255))
screen.blit(num, (470, 572))
# Blit text
      
pygame.display.update()

# Determines if player rolled
playerdidRoll = False
DanrollAgain= True
JanrollAgain= True

# Count the number of turns player has been in jail 4 turns is the max
playjailTimeCount= 0
danjailTimeCount= 0
janjailTimeCount= 0

# Load the Chance and Community Cards and property into dictionaries
GlobalCommunityDict= StartUpFunctions.loadCommunityCards(play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
GlobalChanceCardsDict= StartUpFunctions.loadChanceCards(play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
GlobalPropDict= StartUpFunctions.loadProperties()

Isturn= True

# ---------------------------- S T A R T  U P ---------------------End

# --------------------------- M O N O P O L Y ---------------------Start
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            backMusic.stop()
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("\n------ Player's Turn ------")
            while turn == 'PlayerTurn':
                play, Danny, Jane, GlobalPropDict, Isturn, playerdidRoll, playjailTimeCount= PlayerTurn.startTurn(playerdidRoll, GlobalPropDict, Property_LocationDict, play, Danny, Jane, screen,
                                                                                                                  cattoken, cartoken, hattoken, BoardxPoints,
                                                                                                                  BoardyPoints, background, pygame.display.update,
                                                                                                                  backMusic, playjailTimeCount, GlobalCommunityDict, GlobalChanceCardsDict)
                if Isturn == False:
                    turn= 'Danny'
                        
            while turn == 'Danny':
                play, Danny, Jane, GlobalPropDict, turn, danjailTimeCount, DanrollAgain= ComputerTurn.startDanTurn(GlobalPropDict, Property_LocationDict, play, Danny,
                                                                                                                Jane, screen,cattoken, cartoken, hattoken,
                                                                                                                BoardxPoints, BoardyPoints, background, pygame.display.update,
                                                                                                                danjailTimeCount, turn, DanrollAgain, GlobalCommunityDict, GlobalChanceCardsDict)

            while turn == 'Jane':
                play, Danny, Jane, GlobalPropDict, turn, janjailTimeCount, JanrollAgain= ComputerTurn.startJanTurn(GlobalPropDict, Property_LocationDict, play, Danny,
                                                                                                            Jane, screen,cattoken, cartoken, hattoken,
                                                                                                            BoardxPoints, BoardyPoints, background, pygame.display.update,
                                                                                                            janjailTimeCount, turn, JanrollAgain, GlobalCommunityDict, GlobalChanceCardsDict)
