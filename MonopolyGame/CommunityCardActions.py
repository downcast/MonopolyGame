# These functions perform the actions of a specific card. Each function is passed to the Chance_Cards class
# and is then called when the player lands on a specified location. Actions performed is based on who
# called the function; it is determined by the who variable
#-------------------------------------------------------------------------------------

import random
import tkinter
import tkinter.messagebox

def Card1Action(play, Danny, Jane, who):
    print('Plucking Card 1')
    print('You are assessed for street repairs. $40 per HOUSE, $115 per HOTEL.')
    if who == play.get_name():
        playProp= play.get_PropertyDict()
        total= 0
        go = 0
        for x in playProp:
            print(x)
            if x == 'Reading Railroad' or x == 'Pennsylvania Railroad':
                go = 1
            elif x == 'B. & O. Railroad' or x == 'Short Line':
                go= 1
            elif x == 'Electric Company' or x == 'Water Works':
                go = 1
            else:
                obj2= playProp[x]
                if obj2.get_have_hotel() == True:
                    total += 115
                elif obj2.get_have_house1() == True:
                    total += 40
                    if obj2.get_have_house2() == True:
                        total += 40
                    if obj2.get_have_house3() == True:
                        total += 40
                    if obj2.get_have_house4() == True:
                        total += 40


        remain= play.get_money() - total
        tries= 0
        while remain < 0 and tries < 3:
            gui= tkinter.Tk()
            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money for repairs. Mortgage some of property.')
            tkinter.messagebox.showinfo('Information!', 'Look to the Python shell for further instruction.')
            gui.destroy()

            propName= input('Enter the name of the property you would like to morgage: ')
            if propName in playProp:
                obj= playProp[propName]
                if obj.get_did_Morgage() == False:
                    obj.set_did_Morgage(True)
                    play.set_money(obj.get_morgage_val() + play.get_money())
                    remain= play.get_money() - total
                    tries= 0
                    print('prop mortgaged')
                    
                elif obj.get_did_Morgage() == True:
                    print('Player----')
                    print('This property is already mortgaged.')
                    tries +=1
            else:
                print(propName, 'is not owned by you.')
                tries +=1

        if tries >= 3:
            answer= input('Would you like to end the game?: ')
            if answer == 'Yes':
                pygame.quit()
                sys.exit()
                # Do the end of game stuff and call the sys exit
        play.set_money(remain)
        print(total, 'has been deducted from player account.')
        return play, Danny, Jane
            
    elif who == Danny.get_name():
        DanProp= Danny.get_PropertyDict()
        total= 0
        go = 0
        for x in DanProp:
            if x == 'Reading Railroad' or x == 'Pennsylvania Railroad':
                go = 1
            elif x == 'B. & O. Railroad' or x == 'Short Line':
                go= 1
            elif x == 'Electric Company' or x == 'Water Works':
                go = 1
            else:
                obj2= DanProp[x]
                if obj2.get_have_hotel() == True:
                    total += 115
                elif obj2.get_have_house1() == True:
                    total += 40
                    if obj2.get_have_house2() == True:
                        total += 40
                    if obj2.get_have_house3() == True:
                        total += 40
                    if obj2.get_have_house4() == True:
                        total += 40

        remain= Danny.get_money() - total
        Danny.set_money(remain)
        print(total, "has been deducted from Danny's account.")
        return play, Danny, Jane
    
    elif who == Jane.get_name():
        JanProp= Jane.get_PropertyDict()
        total= 0
        go = 0
        for x in JanProp:
            if x == 'Reading Railroad' or x == 'Pennsylvania Railroad':
                go = 1
            elif x == 'B. & O. Railroad' or x == 'Short Line':
                go= 1
            elif x == 'Electric Company' or x == 'Water Works':
                go = 1
            else:
                obj2= JanProp[x]
                if obj2.get_have_hotel() == True:
                    total += 115
                elif obj2.get_have_house1() == True:
                    total += 40
                    if obj2.get_have_house2() == True:
                        total += 40
                    if obj2.get_have_house3() == True:
                        total += 40
                    if obj2.get_have_house4() == True:
                        total += 40

        remain= Jane.get_money() - total
        Jane.set_money(remain)
        print(total, "has been deducted from Jane's account.")
        return play, Danny, Jane

def Card2Action(play, Danny, Jane, who):
    print('Plucking Card 2')
    print('Grand Opera Opening! Collect $50 from each player.')
    if who == play.get_name():
        play.set_money(play.get_money() + 100)
        Danny.set_money(Danny.get_money() - 50)
        Jane.set_money(Jane.get_money() - 50)
        return play, Danny, Jane
        
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 100)
        play.set_money(play.get_money() - 50)
        Jane.set_money(Jane.get_money() - 50)
        return play, Danny, Jane
        
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 100)
        Danny.set_money(Danny.get_money() - 50)
        play.set_money(play.get_money() - 50)
        return play, Danny, Jane

def Card3Action(play, Danny, Jane, who):
    print('Plucking Card 3')
    print('Life Insurance matures, collect $100.')
    if who == play.get_name():
        play.set_money(play.get_money() + 100)
        return play, Danny, Jane
        
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 100)
        return play, Danny, Jane
    
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 100)
        return play, Danny, Jane
        
def Card4Action(play, Danny, Jane, who):
    print('Plucking Card 4')
    print('Advance to GO, collect $200.')
    if who == play.get_name():
        play.specifyLocation(0)
        play.set_money(play.get_money() + 200)
        return 0, play, Danny, Jane
    elif who == Danny.get_name():
        Danny.specifyLocation(0)
        Danny.set_money(Danny.get_money() + 200)
        return 0, play, Danny, Jane
    elif who == Jane.get_name():
        Jane.specifyLocation(0)
        Jane.set_money(Jane.get_money() + 200)
        return 0, play, Danny, Jane

def Card5Action(play, Danny, Jane, who):
    print('Plucking Card 5')
    print('You have won second Prize in a Beauty contest, collect $10.')
    if who == play.get_name():
        play.set_money(play.get_money() + 10)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 10)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 10)
        return play, Danny, Jane


def Card6Action(play, Danny, Jane, who):
    print('Plucking Card 6')
    print('Pay hospital $100.')
    if who == play.get_name():
        play.set_money(play.get_money() - 100)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() - 100)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() - 100)
        return play, Danny, Jane

def Card7Action(play, Danny, Jane, who):
    print('Plucking Card 7')
    print('Bank error in YOUR favor, collect $200.')
    if who == play.get_name():
        play.set_money(play.get_money() + 200)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 200)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 200)
        return play, Danny, Jane

def Card8Action(play, Danny, Jane, who):
    print('Plucking Card 8')
    print('GO TO JAIL.')
    if who == play.get_name():
        play.specifyLocation(10)
        play.set_jail_Bird(True)
        return 10, play, Danny, Jane
    elif who == Danny.get_name():
        Danny.specifyLocation(10)
        Danny.set_jail_Bird(True)
        return 10, play, Danny, Jane
    elif who == Jane.get_name():
        Jane.specifyLocation(10)
        Jane.set_jail_Bird(True)
        return 10, play, Danny, Jane


def Card9Action(play, Danny, Jane, who):
    print('Plucking Card 9')
    print('Get out of JAIL free card. This card may be kept or sold.')
    if who == play.get_name():
        play.set_Out_of_Jail_Card(True)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_Out_of_Jail_Card(True)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_Out_of_Jail_Card(True)
        return play, Danny, Jane

def Card10Action(play, Danny, Jane, who):
    print('Plucking Card 10')
    print("Doctor's fee. Pay $50.")
    if who == play.get_name():
        play.set_money(play.get_money() - 50)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() - 50)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() - 50)
        return play, Danny, Jane

def Card11Action(play, Danny, Jane, who):
    print('Plucking Card 11')
    print('From sale of Stock you get $45.')
    if who == play.get_name():
        play.set_money(play.get_money() + 45)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 45)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 45)
        return play, Danny, Jane


def Card12Action(play, Danny, Jane, who):
    print('Plucking Card 12')
    print('Xmas fund matures, collect $100.')
    if who == play.get_name():
        play.set_money(play.get_money() + 100)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 100)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 100)
        return play, Danny, Jane


def Card13Action(play, Danny, Jane, who):
    print('Plucking Card 13')
    print('Income tax refund, collect $20.')
    if who == play.get_name():
        play.set_money(play.get_money() + 20)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 20)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 20)
        return play, Danny, Jane


def Card14Action(play, Danny, Jane, who):
    print('Plucking Card 14')
    print('Pay school tax of $150.')
    if who == play.get_name():
        play.set_money(play.get_money() - 150)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() - 150)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() - 150)
        return play, Danny, Jane


def Card15Action(play, Danny, Jane, who):
    print('Plucking Card 15')
    print('Receive for Services $25.')
    if who == play.get_name():
        play.set_money(play.get_money() + 25)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 25)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 25)
        return play, Danny, Jane

                        
def Card16Action(play, Danny, Jane, who):
    print('Plucking Card 16')
    print('You inherit $100.')
    if who == play.get_name():
        play.set_money(play.get_money() + 100)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 100)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 100)
        return play, Danny, Jane
