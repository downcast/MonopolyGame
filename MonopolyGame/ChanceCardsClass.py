# Name: ChanceCardClass
# Descrip: Represents each Chance Card. It has a number to designate which card it is, it has a message that is displayed to the player,
           # it has a 'do_action' method to perform the action of the card based on the obj's card number

import pygame, sys
from pygame.locals import *

pygame.init()

class Chance_Cards():
    def __init__(self, funct, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background):
        
        # Holds the card number; It is used to determine what card is plucked and if it will return a value
        self.__card_number= 0
        # Holds card message to deisplay to player
        self.__message= ''
        # Holds the card action that is unique to each card obj
        self.__action= funct
        # Holds a copy of the player obj in order to pass back to 'main'
        self.__Player= play
        # Holds a copy of the comp Danny obj in order to pass back to 'main'
        self.__Danny= Danny
        # Holds a copy of the comp Jane obj in order to pass back to 'main'
        self.__Jane= Jane
        # Holds a reference of the pygame display
        self.__screen= screen
        # Holds the image that represent the token for the players
        self.__hattoken= hattoken
        self.__cattoken= cattoken
        self.__cartoken= cartoken
        # Holds a list of x-coordinate points that is used with 'self.__screen' to blit the tokens
        self.__BoardxPoints= BoardxPoints
        # Holds a list of y-coordinate points that is used with 'self.__screen' to blit the tokens
        self.__BoardyPoints= BoardyPoints
        # Holds the image that is blitted to 'self.__screen' as the monopoly board
        self.__background= background


    # ----------S E T T E R S   &   G E T T E R S----------------------Start
    def set_card_number(self, n):
        # Setter of the card number
        self.__card_number= n

    def get_card_number(self):
        # Getter of the card number
        return self.__card_number


    def set_message(self, m):
        # Setter of the message
        self.__message= m

    def get_message(self):
        # Getter of the message
        return self.__message
    # ----------S E T T E R S   &   G E T T E R S----------------------End

    # ------------------------M E T H O D S----------------------------Start
    def do_action(self, who, play, Danny, Jane):
        # Descrip: Performs the action specific to each card obj
        # Note: Certain cards return an index for the blitting, as such, different blit methods are needed and are called based on who plucked the card
        
        if self.__Player.get_name() == who:
            # If the card number is 4,7,9,10,11 or 16 then call normal blit; they do not involve player moving from current location
            if self.get_card_number() == 4 or self.get_card_number() == 7:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            elif self.get_card_number() == 9 or self.get_card_number() == 10:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            elif self.get_card_number() == 11 or self.get_card_number() == 16:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            else:
                index, self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.PlayerCardScreenBlit(index)
                return self.__Player, self.__Danny, self.__Jane
                
        elif self.__Danny.get_name() == who:
            # If the card number is 4,7,9,10,11 or 16 then call normal blit; they do not involve comp moving from current location
            if self.get_card_number() == 4 or self.get_card_number() == 7:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            elif self.get_card_number() == 9 or self.get_card_number() == 10:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            elif self.get_card_number() == 11 or self.get_card_number() == 16:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            else:
                index, self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.DannyCardScreenBlit(index)
                return self.__Player, self.__Danny, self.__Jane

        elif self.__Jane.get_name() == who:
            # If the card number is 4,7,9,10,11 or 16 then call normal blit; they do not involve comp moving from current location
            if self.get_card_number() == 4 or self.get_card_number() == 7:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            elif self.get_card_number() == 9 or self.get_card_number() == 10:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            elif self.get_card_number() == 11 or self.get_card_number() == 16:
                self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane
            
            else:
                index, self.__Player, self.__Danny, self.__Jane= self.__action(play, Danny, Jane, who)
                self.JaneCardScreenBlit(index)
                return self.__Player, self.__Danny, self.__Jane


    def ScreenBlit(self):
        # Descrip: Prints the background, player and comp names and money, tokens to the pygame screen
        # Note: Blit prints over existing pixels, therefore all aspects of the screen must be blittted together

        # Get the player board location and use to get pixel screen location to move player
        index = self.__Player.getLocation()
        # Use the index to find the corrosponding pixel location
        valuex = self.__BoardxPoints[index]
        valuey = self.__BoardyPoints[index]

        # Blit the background to the screen
        self.__screen.blit(self.__background, (0,0))

        # Create font obj
        font = pygame.font.Font(None, 36)
        # Set comp name to the font obj and assign to variable
        text1= font.render(self.__Danny.get_name(), 1, (255, 255, 255))
        # Blit variable to screen
        self.__screen.blit(text1, (655,20))
        # Get comp money and assign to vari
        num1 = font.render(format(self.__Danny.get_money(), ',d'), 1, (255, 255, 255))
        # Blit vari to screen
        self.__screen.blit(num1, (673, 70))

        text2= font.render(self.__Jane.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text2, (8,14))
        num2 = font.render(format(self.__Jane.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num2, (8, 67))
        
        text = font.render(self.__Player.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text, (642,555))
        num = font.render(format(self.__Player.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num, (470, 572))
        

        if self.__Player.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Player.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Player.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))


        location = self.__Danny.getLocation()
        valuex = self.__BoardxPoints[location]
        valuey = self.__BoardyPoints[location]

        if self.__Danny.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Danny.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Danny.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))


        location = self.__Jane.getLocation()
        valuex = self.__BoardxPoints[location]
        valuey = self.__BoardyPoints[location]

        if self.__Jane.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Jane.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Jane.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))
        pygame.display.update()

        
    def PlayerCardScreenBlit(self, index):
        
        valuex = self.__BoardxPoints[index]
        valuey = self.__BoardyPoints[index]
        
        self.__screen.blit(self.__background, (0,0))

        #print text
        font = pygame.font.Font(None, 36)
        text1= font.render(self.__Danny.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text1, (655,20))
        num1 = font.render(format(self.__Danny.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num1, (673, 70))

        text2= font.render(self.__Jane.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text2, (8,14))
        num2 = font.render(format(self.__Jane.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num2, (8, 67))
        
        text = font.render(self.__Player.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text, (642,555))
        num = font.render(format(self.__Player.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num, (470, 572))
        #print text

        

        if self.__Player.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Player.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Player.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))


        location = self.__Danny.getLocation()
        valuex = self.__BoardxPoints[location]
        valuey = self.__BoardyPoints[location]

        if self.__Danny.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Danny.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Danny.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))


        location = self.__Jane.getLocation()
        valuex = self.__BoardxPoints[location]
        valuey = self.__BoardyPoints[location]

        if self.__Jane.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Jane.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Jane.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))
        pygame.display.update()


    def DannyCardScreenBlit(self, index):
        
        location = self.__Player.getLocation()
        valuex = self.__BoardxPoints[location]
        valuey = self.__BoardyPoints[location]
        
        self.__screen.blit(self.__background, (0,0))

        #print text
        font = pygame.font.Font(None, 36)
        text1= font.render(self.__Danny.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text1, (655,20))
        num1 = font.render(format(self.__Danny.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num1, (673, 70))

        text2= font.render(self.__Jane.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text2, (8,14))
        num2 = font.render(format(self.__Jane.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num2, (8, 67))
        
        text = font.render(self.__Player.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text, (642,555))
        num = font.render(format(self.__Player.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num, (470, 572))
        #print text

        

        if self.__Player.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Player.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Player.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))
            

        valuex = self.__BoardxPoints[index]
        valuey = self.__BoardyPoints[index]

        if self.__Danny.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Danny.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Danny.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))


        location = self.__Jane.getLocation()
        valuex = self.__BoardxPoints[location]
        valuey = self.__BoardyPoints[location]

        if self.__Jane.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Jane.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Jane.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))
        pygame.display.update()


    def JaneCardScreenBlit(self, index):
        
        location = self.__Player.getLocation()
        valuex = self.__BoardxPoints[location]
        valuey = self.__BoardyPoints[location]
        
        self.__screen.blit(self.__background, (0,0))

        #print text
        font = pygame.font.Font(None, 36)
        text1= font.render(self.__Danny.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text1, (655,20))
        num1 = font.render(format(self.__Danny.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num1, (673, 70))

        text2= font.render(self.__Jane.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text2, (8,14))
        num2 = font.render(format(self.__Jane.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num2, (8, 67))
        
        text = font.render(self.__Player.get_name(), 1, (255, 255, 255))
        self.__screen.blit(text, (642,555))
        num = font.render(format(self.__Player.get_money(), ',d'), 1, (255, 255, 255))
        self.__screen.blit(num, (470, 572))
        #print text

        

        if self.__Player.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Player.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Player.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))
            
        location= self.__Danny.getLocation()
        valuex = self.__BoardxPoints[location]
        valuey = self.__BoardyPoints[location]

        if self.__Danny.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Danny.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Danny.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))

        valuex = self.__BoardxPoints[index]
        valuey = self.__BoardyPoints[index]

        if self.__Jane.get_token() == 'Hat':
            self.__screen.blit(self.__hattoken, (valuex,valuey))
            
        elif self.__Jane.get_token() == 'Cat':
            self.__screen.blit(self.__cattoken, (valuex,valuey))
            
        elif self.__Jane.get_token() == 'Car':
            self.__screen.blit(self.__cartoken, (valuex,valuey))
        pygame.display.update()

    # ------------------------M E T H O D S----------------------------End

# Prog: Smith
