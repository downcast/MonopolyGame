# This class is for Community Chest Cards
# During the object's creation, pass it the action function the card will complete
# set it equal to the self.__action vari. Call it when the player picks its card number

import pygame, sys
from pygame.locals import *

pygame.init()

class Comminity_Chest():
    def __init__(self, funct, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background):
        self.__card_number= 0
        self.__message= ''
        self.__action= funct
        self.__Player= play
        self.__Danny= Danny
        self.__Jane= Jane
        self.__screen= screen
        self.__hattoken= hattoken
        self.__cattoken= cattoken
        self.__cartoken= cartoken
        self.__BoardxPoints= BoardxPoints
        self.__BoardyPoints= BoardyPoints
        self.__background= background

    def set_card_number(self, n):
        self.__card_number= n

    def get_card_number(self):
        return self.__card_number


    def set_message(self, m):
        self.__message= m

    def get_message(self):
        return self.__message

    # Action to be performed that is passed in
    def do_action(self, who, play, Danny, Jane):
        # card number determines which card is called, if the card number is a range of specific values, it will return
        # an index
        if self.__Player.get_name() == who:
            if self.get_card_number() == 4 or self.get_card_number() == 8:
                index, self.__Player, self.__Danny, self.__Jane= self.__action(self.__Player, self.__Danny, self.__Jane, who)
                self.PlayerCardScreenBlit(index)
                return self.__Player, self.__Danny, self.__Jane

            else:
                self.__Player, self.__Danny, self.__Jane= self.__action(self.__Player, self.__Danny, self.__Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane

        elif self.__Danny.get_name() == who:
            if self.get_card_number() == 4 or self.get_card_number() == 8:
                index, self.__Player, self.__Danny, self.__Jane= self.__action(self.__Player, self.__Danny, self.__Jane, who)
                self.DannyCardScreenBlit(index)
                return self.__Player, self.__Danny, self.__Jane

            else:
                self.__Player, self.__Danny, self.__Jane= self.__action(self.__Player, self.__Danny, self.__Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane

        elif self.__Jane.get_name() == who:
            if self.get_card_number() == 4 or self.get_card_number() == 8:
                index, self.__Player, self.__Danny, self.__Jane= self.__action(self.__Player, self.__Danny, self.__Jane, who)
                self.JaneCardScreenBlit(index)
                return self.__Player, self.__Danny, self.__Jane

            else:
                self.__Player, self.__Danny, self.__Jane= self.__action(self.__Player, self.__Danny, self.__Jane, who)
                self.ScreenBlit()
                return self.__Player, self.__Danny, self.__Jane


    def ScreenBlit(self):
        
        index = self.__Player.getLocation()
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
        
