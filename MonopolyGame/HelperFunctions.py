# Descrip: This file holds the 'EndGame' function and the 'ScreenBlit' function

import PlayerClass
import ComputerClass
import pygame, sys


def EndGame(play, Danny, Jane, sound):
    # Descrip: Function totals the assests of each player and displays the winner
    
    # Get the amount of money each player made
    playMoney= play.get_money()
    DanMoney= Danny.get_money()
    JanMoney= Jane.get_money()
    
    # Total the value of assests
    # --- Each house is worth the cost
    # --- Each prop is worth the mortgage value
    
    playassest= 0
    playdict= play.get_PropertyDict()
    
    for x in playdict:
        propobj= playdict[x]
        if x == 'Reading Railroad' or x == 'Pennsylvania Railroad':
           playassest += propobj.get_morgage_val()
        elif x == 'B. & O. Railroad' or x == 'Short Line':
            playassest += propobj.get_morgage_val()
        elif x == 'Electric Company' or x == 'Water Works':
             playassest += propobj.get_morgage_val()
        elif propobj.get_have_hotel() == True:
            housevalue= propobj.get_house_Cost()
            playassest += 5*housevalue
            playassest += propobj.get_morgage_val()
        elif propobj.get_have_house4() == True:
            playassest += 4*housevalue
            playassest += propobj.get_morgage_val()
        elif propobj.get_have_house3() == True:
            playassest += 3*housevalue
            playassest += propobj.get_morgage_val()
        elif propobj.get_have_house2() == True:
            playassest += 2*housevalue
            playassest += propobj.get_morgage_val()
        elif propobj.get_have_house1() == True:
            playassest += housevalue
            playassest += propobj.get_morgage_val()
        else:
            playassest += propobj.get_morgage_val()

    Danassest= 0
    Dandict= Danny.get_PropertyDict()
    
    for x in Dandict:
        propobj= Dandict[x]
        if x == 'Reading Railroad' or x == 'Pennsylvania Railroad':
           Danassest += propobj.get_morgage_val()
        elif x == 'B. & O. Railroad' or x == 'Short Line':
            Danassest += propobj.get_morgage_val()
        elif x == 'Electric Company' or x == 'Water Works':
             Danassest += propobj.get_morgage_val()
        elif propobj.get_have_hotel() == True:
            housevalue= propobj.get_house_Cost()
            Danassest += 5*housevalue
            Danassest += propobj.get_morgage_val()
        elif propobj.get_have_house4() == True:
            Danassest += 4*housevalue
            Danassest += propobj.get_morgage_val()
        elif propobj.get_have_house3() == True:
            Danassest += 3*housevalue
            Danassest += propobj.get_morgage_val()
        elif propobj.get_have_house2() == True:
            Danassest += 2*housevalue
            Danassest += propobj.get_morgage_val()
        elif propobj.get_have_house1() == True:
            Danassest += housevalue
            Danassest += propobj.get_morgage_val()
        else:
            Danassest += propobj.get_morgage_val()

    Janassest= 0
    Jandict= Jane.get_PropertyDict()
    
    for x in Jandict:
        propobj= Jandict[x]
        if x == 'Reading Railroad' or x == 'Pennsylvania Railroad':
           Janassest += propobj.get_morgage_val()
        elif x == 'B. & O. Railroad' or x == 'Short Line':
            Janassest += propobj.get_morgage_val()
        elif x == 'Electric Company' or x == 'Water Works':
             Janassest += propobj.get_morgage_val()
        elif propobj.get_have_hotel() == True:
            housevalue= propobj.get_house_Cost()
            Janassest += 5*housevalue
            Janassest += propobj.get_morgage_val()
        elif propobj.get_have_house4() == True:
            Janassest += 4*housevalue
            Janassest += propobj.get_morgage_val()
        elif propobj.get_have_house3() == True:
            Janassest += 3*housevalue
            Janassest += propobj.get_morgage_val()
        elif propobj.get_have_house2() == True:
            Janassest += 2*housevalue
            Janassest += propobj.get_morgage_val()
        elif propobj.get_have_house1() == True:
            Janassest += housevalue
            Janassest += propobj.get_morgage_val()
        else:
            Janassest += propobj.get_morgage_val()

    playtotal= playMoney + playassest
    Dantotal= DanMoney + Danassest
    Jantotal= JanMoney + Janassest

    if playtotal > Dantotal and playtotal > Jantotal:
        print(play.get_name(), "'s cash is, ", playMoney, sep='')
        print(play.get_name(), "'s property value is, ", playassest, sep='')
        print(play.get_name(), "'s total value is, ", playtotal, sep='')
        print('==========================================')
        print(Danny.get_name(), "'s cash is, ", DanMoney, sep='')
        print(Danny.get_name(), "'s property value is, ", Danassest, sep='')
        print(Danny.get_name(), "'s total value is, ", Dantotal, sep='')
        print('==========================================')
        print(Jane.get_name(), "'s cash is, ", JanMoney, sep='')
        print(Jane.get_name(), "'s property value is, ", Janassest, sep='')
        print(Jane.get_name(), "'s total value is, ", Jantotal, sep='')
        print('==========================================')
        print('Player is the winner')
    elif Dantotal > playtotal and Dantotal > Jantotal:
        print(play.get_name(), "'s cash is, ", playMoney, sep='')
        print(play.get_name(), "'s property value is, ", playassest, sep='')
        print(play.get_name(), "'s total value is, ", playtotal, sep='')
        print('==========================================')
        print(Danny.get_name(), "'s cash is, ", DanMoney, sep='')
        print(Danny.get_name(), "'s property value is, ", Danassest, sep='')
        print(Danny.get_name(), "'s total value is, ", Dantotal, sep='')
        print('==========================================')
        print(Jane.get_name(), "'s cash is, ", JanMoney, sep='')
        print(Jane.get_name(), "'s property value is, ", Janassest, sep='')
        print(Jane.get_name(), "'s total value is, ", Jantotal, sep='')
        print('==========================================')
        print('Danny is the winner')
    elif Jantotal > playtotal and Jantotal > Dantotal:
        print(play.get_name(), "'s cash is, ", playMoney, sep='')
        print(play.get_name(), "'s property value is, ", playassest, sep='')
        print(play.get_name(), "'s total value is, ", playtotal, sep='')
        print('==========================================')
        print(Danny.get_name(), "'s cash is, ", DanMoney, sep='')
        print(Danny.get_name(), "'s property value is, ", Danassest, sep='')
        print(Danny.get_name(), "'s total value is, ", Dantotal, sep='')
        print('==========================================')
        print(Jane.get_name(), "'s cash is, ", JanMoney, sep='')
        print(Jane.get_name(), "'s property value is, ", Janassest, sep='')
        print(Jane.get_name(), "'s total value is, ", Jantotal, sep='')
        print('==========================================')
        print('Jane is the winner')
    elif playtotal == Dantotal and playtotal == Jantotal:
        print(play.get_name(), "'s cash is, ", playMoney, sep='')
        print(play.get_name(), "'s property value is, ", playassest, sep='')
        print(play.get_name(), "'s total value is, ", playtotal, sep='')
        print('==========================================')
        print(Danny.get_name(), "'s cash is, ", DanMoney, sep='')
        print(Danny.get_name(), "'s property value is, ", Danassest, sep='')
        print(Danny.get_name(), "'s total value is, ", Dantotal, sep='')
        print('==========================================')
        print(Jane.get_name(), "'s cash is, ", JanMoney, sep='')
        print(Jane.get_name(), "'s property value is, ", Janassest, sep='')
        print(Jane.get_name(), "'s total value is, ", Jantotal, sep='')
        print('==========================================')
        print('No winner, all players have equivelent assest values.')
    elif Dantotal == Jantotal:
        print(play.get_name(), "'s cash is, ", playMoney, sep='')
        print(play.get_name(), "'s property value is, ", playassest, sep='')
        print(play.get_name(), "'s total value is, ", playtotal, sep='')
        print('==========================================')
        print(Danny.get_name(), "'s cash is, ", DanMoney, sep='')
        print(Danny.get_name(), "'s property value is, ", Danassest, sep='')
        print(Danny.get_name(), "'s total value is, ", Dantotal, sep='')
        print('==========================================')
        print(Jane.get_name(), "'s cash is, ", JanMoney, sep='')
        print(Jane.get_name(), "'s property value is, ", Janassest, sep='')
        print(Jane.get_name(), "'s total value is, ", Jantotal, sep='')
        print('==========================================')
        print('Danny and Jane have equivelent assest values.')
    elif playtotal == Dantotal:
        print(play.get_name(), "'s cash is, ", playMoney, sep='')
        print(play.get_name(), "'s property value is, ", playassest, sep='')
        print(play.get_name(), "'s total value is, ", playtotal, sep='')
        print('==========================================')
        print(Danny.get_name(), "'s cash is, ", DanMoney, sep='')
        print(Danny.get_name(), "'s property value is, ", Danassest, sep='')
        print(Danny.get_name(), "'s total value is, ", Dantotal, sep='')
        print('==========================================')
        print(Jane.get_name(), "'s cash is, ", JanMoney, sep='')
        print(Jane.get_name(), "'s property value is, ", Janassest, sep='')
        print(Jane.get_name(), "'s total value is, ", Jantotal, sep='')
        print('==========================================')
        print('Player and Danny have equivelent assest values.')
    elif playtotal == Jantotal:
        print(play.get_name(), "'s cash is, ", playMoney, sep='')
        print(play.get_name(), "'s property value is, ", playassest, sep='')
        print(play.get_name(), "'s total value is, ", playtotal, sep='')
        print('==========================================')
        print(Danny.get_name(), "'s cash is, ", DanMoney, sep='')
        print(Danny.get_name(), "'s property value is, ", Danassest, sep='')
        print(Danny.get_name(), "'s total value is, ", Dantotal, sep='')
        print('==========================================')
        print(Jane.get_name(), "'s cash is, ", JanMoney, sep='')
        print(Jane.get_name(), "'s property value is, ", Janassest, sep='')
        print(Jane.get_name(), "'s total value is, ", Jantotal, sep='')
        print('==========================================')
        print('Player and Jane have equivelent assest values.')
    else:
        print(play.get_name(), "'s cash is, ", playMoney, sep='')
        print(play.get_name(), "'s property value is, ", playassest, sep='')
        print(play.get_name(), "'s total value is, ", playtotal, sep='')
        print('==========================================')
        print(Danny.get_name(), "'s cash is, ", DanMoney, sep='')
        print(Danny.get_name(), "'s property value is, ", Danassest, sep='')
        print(Danny.get_name(), "'s total value is, ", Dantotal, sep='')
        print('==========================================')
        print(Jane.get_name(), "'s cash is, ", JanMoney, sep='')
        print(Jane.get_name(), "'s property value is, ", Janassest, sep='')
        print(Jane.get_name(), "'s total value is, ", Jantotal, sep='')
        print('==========================================')
        print('Winner is the one with the highest total value.')
    print('\nThanks for Playing!')
    # Kill the background music
    sound.stop()
    pygame.quit()
    sys.exit()
    
    # Gui the winner and play sound

def ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update):
    # Descrip: Function takes all player and comp information, screen, tokens and coordinates
                # Then copies the needed information to the screen. Main use is to show token
                # movement, money changes and name

    # Get the location of the player according to the board space
    index = play.getLocation()
    # Match location to the x and y pixel location of the space on the screen
    valuex = BoardxPoints[index]
    valuey = BoardyPoints[index]

    # Copy the background to the screen FIRST
    screen.blit(background, (0,0))

    # Create font obj
    font = pygame.font.Font(None, 36)
    # Assign comp name to font obj and assign to vari
    text1= font.render(Danny.get_name(), 1, (255, 255, 255))
    # Copy vari font obj to screen
    screen.blit(text1, (655,20))
    # Assign comp nomey to font obj and assign to vari
    num1 = font.render(format(Danny.get_money(), ',d'), 1, (255, 255, 255))
    # Copy vari font obj to screen
    screen.blit(num1, (673, 70))

    text2= font.render(Jane.get_name(), 1, (255, 255, 255))
    screen.blit(text2, (8,14))
    num2 = font.render(format(Jane.get_money(), ',d'), 1, (255, 255, 255))
    screen.blit(num2, (8, 67))
    
    text = font.render(play.get_name(), 1, (255, 255, 255))
    screen.blit(text, (642,555))
    num = font.render(format(play.get_money(), ',d'), 1, (255, 255, 255))
    screen.blit(num, (470, 572))

    if play.get_token() == 'Hat':
        screen.blit(hattoken, (valuex,valuey))
        
    elif play.get_token() == 'Cat':
        screen.blit(cattoken, (valuex,valuey))
        
    elif play.get_token() == 'Car':
        screen.blit(cartoken, (valuex,valuey))


    index = Danny.getLocation()
    valuex = BoardxPoints[index]
    valuey = BoardyPoints[index]

    if Danny.get_token() == 'Hat':
        screen.blit(hattoken, (valuex,valuey))
        
    elif Danny.get_token() == 'Cat':
        screen.blit(cattoken, (valuex,valuey))
        
    elif Danny.get_token() == 'Car':
        screen.blit(cartoken, (valuex,valuey))


    index = Jane.getLocation()
    valuex = BoardxPoints[index]
    valuey = BoardyPoints[index]

    if Jane.get_token() == 'Hat':
        screen.blit(hattoken, (valuex,valuey))
        
    elif Jane.get_token() == 'Cat':
        screen.blit(cattoken, (valuex,valuey))
        
    elif Jane.get_token() == 'Car':
        screen.blit(cartoken, (valuex,valuey))

    # Refresh the changes to show changes to player
    update()


# Prog: Smith
