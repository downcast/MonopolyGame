# These functions perform the actions of a specific card. Each function is passed to the Chance_Cards class
# and is then called when the player lands on a specified location. Actions performed is based on who
# called the function; it is determined by the who variable
#-------------------------------------------------------------------------------------

import random
import tkinter
import tkinter.messagebox

def Card1Action(play, Danny, Jane, who):
    print('Plucking Card 1')
    # who determines who called this card and the blitting and stuff is done accordingly
    print('Advance to St. Charles Place. If you pass GO, collect $200.')
    if who == play.get_name():
        if play.getLocation() < 11:
            play.set_money(play.get_money() + 200)
            play.specifyLocation(11)
            return 11, play, Danny, Jane
        else:
            return 11, play, Danny, Jane
    elif who == Danny.get_name():
        if Danny.getLocation() < 11:
            Danny.set_money(Danny.get_money() + 200)
            Danny.specifyLocation(11)
            return 11, play, Danny, Jane
        else:
            return 11, play, Danny, Jane
    elif who == Jane.get_name():
        if Jane.getLocation() < 11:
            Jane.set_money(Jane.get_money() + 200)
            Jane.specifyLocation(11)
            return 11, play, Danny, Jane
        else:
            return 11, play, Danny, Jane

def Card2Action(play, Danny, Jane, who):
    print('Plucking Card 2')
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

def Card3Action(play, Danny, Jane, who):
    print('Plucking Card 3')
    print('Go directly to JAIL. Do not collect $200.')
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

def Card4Action(play, Danny, Jane, who):
    print('Plucking Card 4')
    print('Bank pays you a Dividend of $50.')
    if who == play.get_name():
        play.set_money(play.get_money() + 50)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 50)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 50)
        return play, Danny, Jane

def Card5Action(play, Danny, Jane, who):
    print('Plucking Card 5')
    print('Advance token to BOARDWALK!')
    if who == play.get_name():
        play.specifyLocation(39)
        return 39, play, Danny, Jane
    elif who == Danny.get_name():
        Danny.specifyLocation(39)
        return 39, play, Danny, Jane
    elif who == Jane.get_name():
        Jane.specifyLocation(39)
        return 39, play, Danny, Jane

def Card6Action(play, Danny, Jane, who):
    print('Plucking Card 6')
    print('Advance token to Illinois Ave.')
    if who == play.get_name():
        play.specifyLocation(24)
        return 24, play, Danny, Jane
    elif who == Danny.get_name():
        Danny.specifyLocation(24)
        return 24, play, Danny, Jane
    elif who == Jane.get_name():
        Jane.specifyLocation(24)
        return 24, play, Danny, Jane

def Card7Action(play, Danny, Jane, who):
    print('Plucking Card 7')
    print('Your building and loan matures. Collect $150.')
    if who == play.get_name():
        play.set_money(play.get_money() + 150)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 150)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 150)
        return play, Danny, Jane

def Card8Action(play, Danny, Jane, who):
    print('Plucking Card 8')
    print('Go back three spaces.')
    if who == play.get_name():
        x= play.getLocation() - 3
        play.specifyLocation(x)
        return x, play, Danny, Jane
    elif who == Danny.get_name():
        x= Danny.getLocation() - 3
        Danny.specifyLocation(x)
        return x, play, Danny, Jane
    elif who == Jane.get_name():
        x= Jane.getLocation() - 3
        Jane.specifyLocation(x)
        return x, play, Danny, Jane

def Card9Action(play, Danny, Jane, who):
    print('Plucking Card 9')
    print('Get out of Jail FREE! This card may be kept or sold.')
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
    print('Pay POOR tax of $15.')
    if who == play.get_name():
        play.set_money(play.get_money() + 15)
        return play, Danny, Jane
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() + 15)
        return play, Danny, Jane
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() + 15)
        return play, Danny, Jane

def Card11Action(play, Danny, Jane, who):
    print('Plucking Card 11')
    print('Make general repairs on ALL of your property. $25 for EACH house, $100 for EACH hotel.')
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
                    total += 100
                elif obj2.get_have_house1() == True:
                    total += 25
                    if obj2.get_have_house2() == True:
                        total += 25
                    if obj2.get_have_house3() == True:
                        total += 25
                    if obj2.get_have_house4() == True:
                        total += 25


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
                    total += 100
                elif obj2.get_have_house1() == True:
                    total += 25
                    if obj2.get_have_house2() == True:
                        total += 25
                    if obj2.get_have_house3() == True:
                        total += 25
                    if obj2.get_have_house4() == True:
                        total += 25

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
                    total += 100
                elif obj2.get_have_house1() == True:
                    total += 25
                    if obj2.get_have_house2() == True:
                        total += 25
                    if obj2.get_have_house3() == True:
                        total += 25
                    if obj2.get_have_house4() == True:
                        total += 25

        remain= Jane.get_money() - total
        Jane.set_money(remain)
        print(total, "has been deducted from Jane's account.")
        return play, Danny, Jane

def Card12Action(play, Danny, Jane, who):
    print('Plucking Card 12')
    print('Take a ride on the Reading. If you pass GO, collect $200.')
    if who == play.get_name():
        if play.getLocation() < 5:
            play.specifyLocation(5)
            return 5, play, Danny, Jane
        elif play.getLocation() > 5:
            play.specifyLocation(5)
            play.set_money(play.get_money() + 200)
            return 5, play, Danny, Jane
    elif who == Danny.get_name():
        if Danny.getLocation() < 5:
            Danny.specifyLocation(5)
            return 5, play, Danny, Jane
        elif Danny.getLocation() > 5:
            Danny.specifyLocation(5)
            Danny.set_money(Danny.get_money() + 200)
            return 5, play, Danny, Jane
    elif who == Jane.get_name():
        if Jane.getLocation() < 5:
            Jane.specifyLocation(5)
            return 5, play, Danny, Jane
        elif Jane.getLocation() > 5:
            Jane.specifyLocation(5)
            Jane.set_money(Jane.get_money() + 200)
            return 5, play, Danny, Jane


def Card13Action(play, Danny, Jane, who):
    print('Plucking Card 13')
    print('Advance to the nearest Railroad and pay double the rent.')
    if who == play.get_name():
        if play.getLocation() < 5:
            play.specifyLocation(5)
            playDict= play.get_PropertyDict()
            value= playDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own Reading Railroad.')
                return 5, play, Danny, Jane

        elif play.getLocation() < 15:
            play.specifyLocation(15)
            playDict= play.get_PropertyDict()
            value= playDict.get('Pennsylvania Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Pennsylvania Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Pennsylvania Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nPennsylvania Railroad is not owned.\n')
                        return 15, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 15, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 15, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own Pennsylvania Railroad.')
                return 15, play, Danny, Jane

        elif play.getLocation() < 25:
            play.specifyLocation(25)
            playDict= play.get_PropertyDict()
            value= playDict.get('B. & O. Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('B. & O. Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('B. & O. Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nB. & O. Railroad is not owned.\n')
                        return 25, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 25, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 25, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own B. & O. Railroad.')
                return 25, play, Danny, Jane

        elif play.getLocation() < 35:
            play.specifyLocation(35)
            playDict= play.get_PropertyDict()
            value= playDict.get('Short Line', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Short Line', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Short Line', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nShort Line is not owned.\n')
                        return 35, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 35, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 35, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own Short Line.')
                return 35, play, Danny, Jane

        elif play.getLocation() > 35:
            play.specifyLocation(5)
            playDict= play.get_PropertyDict()
            value= playDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own Reading Railroad.')
                return 5, play, Danny, Jane
    # ------------------------------        
    elif who == Danny.get_name():
        if Danny.getLocation() < 5:
            Danny.specifyLocation(5)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 5, play, Danny, Jane

        elif Danny.getLocation() < 15:
            Danny.specifyLocation(15)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Pennsylvania Railroad', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Pennsylvania Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Pennsylvania Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nPennsylvania Railroad is not owned.\n')
                        return 15, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 15, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 15, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 15, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 15, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 15, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 15, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 15, play, Danny, Jane

        elif Danny.getLocation() < 25:
            Danny.specifyLocation(25)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('B. & O. Railroad', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('B. & O. Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('B. & O. Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nB. & O. Railroad is not owned.\n')
                        return 25, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 25, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 25, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 25, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 25, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 25, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 25, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 25, play, Danny, Jane

        elif Danny.getLocation() < 35:
            Danny.specifyLocation(35)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Short Line', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Short Line', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Short Line', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nShort Line is not owned.\n')
                        return 35, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 35, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 35, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 35, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 35, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 35, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 35, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 35, play, Danny, Jane

        elif Danny.getLocation() > 35:
            Danny.specifyLocation(5)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 5, play, Danny, Jane

    # --------------------------------------
    elif who == Jane.get_name():
        if Jane.getLocation() < 5:
            Jane.specifyLocation(5)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 5, play, Danny, Jane

        elif Jane.getLocation() < 15:
            Jane.specifyLocation(15)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Pennsylvania Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Pennsylvania Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('Pennsylvania Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nPennsylvania Railroad is not owned.\n')
                        return 15, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 15, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 15, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 15, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 15, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 15, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 15, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 15, play, Danny, Jane

        elif Jane.getLocation() < 25:
            Jane.specifyLocation(25)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('B. & O. Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('B. & O. Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('B. & O. Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nB. & O. Railroad is not owned.\n')
                        return 25, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 25, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 25, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 25, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 25, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 25, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 25, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 25, play, Danny, Jane

        elif Jane.getLocation() < 35:
            Jane.specifyLocation(35)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Short Line', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Short Line', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('Short Line', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nShort Line is not owned.\n')
                        return 35, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 35, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 35, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 35, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 35, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 35, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 35, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 35, play, Danny, Jane

        elif Jane.getLocation() > 35:
            Jane.specifyLocation(5)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 5, play, Danny, Jane


def Card14Action(play, Danny, Jane, who):
    print('Plucking Card 14')
    print('Advance to the nearest Utility, roll dice and pay 10x the value of the roll.')
    if who == play.get_name():
        if play.getLocation() < 12:
            play.specifyLocation(12)
            playDict= play.get_PropertyDict()
            value= playDict.get('Electric Company', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Electric Company', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Electric Company', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nElectric Company is not owned.\n')
                        return 12, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        play.set_money(play.get_money() - x1)
                        Jane.set_money(Jane.get_money() + x1)
                        return 12, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    play.set_money(play.get_money() - x1)
                    Danny.set_money(Danny.get_money() + x1)
                    return 12, play, Danny, Jane
            else:
                # Player owns nearest util
                print('You own Electric Company.')
                return 12, play, Danny, Jane

        elif play.getLocation() < 28:
            play.specifyLocation(28)
            playDict= play.get_PropertyDict()
            value= playDict.get('Water Works', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Water Works', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Water Works', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nWater Works is not owned.\n')
                        return 28, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        play.set_money(play.get_money() - x1)
                        Jane.set_money(Jane.get_money() + x1)
                        return 28, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    play.set_money(play.get_money() - x1)
                    Danny.set_money(Danny.get_money() + x1)
                    return 28, play, Danny, Jane
            else:
                # Player owns nearest util
                print('You own Water Works.')
                return 28, play, Danny, Jane

        elif play.getLocation() > 28:
            play.specifyLocation(12)
            playDict= play.get_PropertyDict()
            value= playDict.get('Electric Company', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Electric Company', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Electric Company', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nElectric Company is not owned.\n')
                        return 12, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        play.set_money(play.get_money() - x1)
                        Jane.set_money(Jane.get_money() + x1)
                        return 12, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    play.set_money(play.get_money() - x1)
                    Danny.set_money(Danny.get_money() + x1)
                    return 12, play, Danny, Jane
            else:
                # Player owns nearest util
                print('You own Electric Company.')
                return 12, play, Danny, Jane
    # -----------------------------------------------
    
    elif who == Danny.get_name():
        if Danny.getLocation() < 12:
            Danny.specifyLocation(12)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Electric Company', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Electric Company', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Electric Company', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nElectric Company is not owned.\n')
                        return 12, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        Danny.set_money(Danny.get_money() - x1)
                        Jane.set_money(Jane.get_money() + x1)
                        return 12, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    Danny.set_money(Danny.get_money() - x1)
                    play.set_money(play.get_money() + x1)
                    return 12, play, Danny, Jane
            else:
                # Dan owns nearest util
                return 12, play, Danny, Jane

        elif Danny.getLocation() < 28:
            Danny.specifyLocation(28)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Water Works', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Water Works', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Water Works', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nWater Works is not owned.\n')
                        return 28, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        Danny.set_money(Danny.get_money() - x1)
                        Jane.set_money(Jane.get_money() + x1)
                        return 28, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    Danny.set_money(Danny.get_money() - x1)
                    Danny.set_money(Danny.get_money() + x1)
                    return 28, play, Danny, Jane
            else:
                # Dan owns nearest util
                return 28, play, Danny, Jane

        elif Danny.getLocation() > 28:
            Danny.specifyLocation(12)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Electric Company', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Electric Company', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Electric Company', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nElectric Company is not owned.\n')
                        return 12, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        Danny.set_money(Danny.get_money() - x1)
                        Jane.set_money(Jane.get_money() + x1)
                        return 12, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    Danny.set_money(Danny.get_money() - x1)
                    play.set_money(play.get_money() + x1)
                    return 12, play, Danny, Jane
            else:
                # Dan owns nearest util
                return 12, play, Danny, Jane
            
    elif who == Jane.get_name():
        if Jane.getLocation() < 12:
            Jane.specifyLocation(12)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Electric Company', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Electric Company', 'Entry not found')
                if value1 == 'Entry not found':
                    DanDict= Danny.get_PropertyDict()
                    value2= DanDict.get('Electric Company', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nElectric Company is not owned.\n')
                        return 12, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        Jane.set_money(Jane.get_money() - x1)
                        Danny.set_money(Danny.get_money() + x1)
                        return 12, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    Jane.set_money(Jane.get_money() - x1)
                    play.set_money(play.get_money() + x1)
                    return 12, play, Danny, Jane
            else:
                # Jane owns nearest util
                return 12, play, Danny, Jane

        elif Jane.getLocation() < 28:
            Jane.specifyLocation(28)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Water Works', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Water Works', 'Entry not found')
                if value1 == 'Entry not found':
                    DanDict= Danny.get_PropertyDict()
                    value2= DanDict.get('Water Works', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nWater Works is not owned.\n')
                        return 28, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        Jane.set_money(Jane.get_money() - x1)
                        Danny.set_money(Danny.get_money() + x1)
                        return 28, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    Jane.set_money(Jane.get_money() - x1)
                    play.set_money(play.get_money() + x1)
                    return 28, play, Danny, Jane
            else:
                # Jane owns nearest util
                return 28, play, Danny, Jane

        elif Jane.getLocation() > 28:
            Jane.specifyLocation(12)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Electric Company', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Electric Company', 'Entry not found')
                if value1 == 'Entry not found':
                    DanDict= Danny.get_PropertyDict()
                    value2= DanDict.get('Electric Company', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nElectric Company is not owned.\n')
                        return 12, play, Danny, Jane
                    else:
                        x= random.randint(1, 12)
                        x1 = x * 10
                        Jane.set_money(Jane.get_money() - x1)
                        Danny.set_money(Danny.get_money() + x1)
                        return 12, play, Danny, Jane
                else:
                    x= random.randint(1, 12)
                    x1 = x * 10
                    Jane.set_money(Jane.get_money() - x1)
                    play.set_money(play.get_money() + x1)
                    return 12, play, Danny, Jane
            else:
                # Jane owns nearest util
                return 12, play, Danny, Jane

def Card15Action(play, Danny, Jane, who):
    print('Plucking Card 15')
    print('Advance to the nearest Railroad and pay double the rent.')
    if who == play.get_name():
        if play.getLocation() < 5:
            play.specifyLocation(5)
            playDict= play.get_PropertyDict()
            value= playDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own Reading Railroad.')
                return 5, play, Danny, Jane

        elif play.getLocation() < 15:
            play.specifyLocation(15)
            playDict= play.get_PropertyDict()
            value= playDict.get('Pennsylvania Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Pennsylvania Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Pennsylvania Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nPennsylvania Railroad is not owned.\n')
                        return 15, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 15, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 15, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own Pennsylvania Railroad.')
                return 15, play, Danny, Jane

        elif play.getLocation() < 25:
            play.specifyLocation(25)
            playDict= play.get_PropertyDict()
            value= playDict.get('B. & O. Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('B. & O. Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('B. & O. Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nB. & O. Railroad is not owned.\n')
                        return 25, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 25, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 25, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own B. & O. Railroad.')
                return 25, play, Danny, Jane

        elif play.getLocation() < 35:
            play.specifyLocation(35)
            playDict= play.get_PropertyDict()
            value= playDict.get('Short Line', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Short Line', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Short Line', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nShort Line is not owned.\n')
                        return 35, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 35, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 35, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own Short Line.')
                return 35, play, Danny, Jane

        elif play.getLocation() > 35:
            play.specifyLocation(5)
            playDict= play.get_PropertyDict()
            value= playDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            play.set_money(play.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            play.set_money(play.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            play.set_money(play.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            play.set_money(play.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        play.set_money(play.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        play.set_money(play.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        play.set_money(play.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        play.set_money(play.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Player owns nearest Rail
                print('You own Reading Railroad.')
                return 5, play, Danny, Jane
    # ------------------------------        
    elif who == Danny.get_name():
        if Danny.getLocation() < 5:
            Danny.specifyLocation(5)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 5, play, Danny, Jane

        elif Danny.getLocation() < 15:
            Danny.specifyLocation(15)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Pennsylvania Railroad', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Pennsylvania Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Pennsylvania Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nPennsylvania Railroad is not owned.\n')
                        return 15, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 15, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 15, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 15, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 15, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 15, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 15, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 15, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 15, play, Danny, Jane

        elif Danny.getLocation() < 25:
            Danny.specifyLocation(25)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('B. & O. Railroad', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('B. & O. Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('B. & O. Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nB. & O. Railroad is not owned.\n')
                        return 25, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 25, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 25, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 25, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 25, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 25, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 25, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 25, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 25, play, Danny, Jane

        elif Danny.getLocation() < 35:
            Danny.specifyLocation(35)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Short Line', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Short Line', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Short Line', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nShort Line is not owned.\n')
                        return 35, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 35, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 35, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 35, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 35, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 35, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 35, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 35, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 35, play, Danny, Jane

        elif Danny.getLocation() > 35:
            Danny.specifyLocation(5)
            DanDict= Danny.get_PropertyDict()
            value= DanDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                playDict= play.get_PropertyDict()
                value1= playDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    JaneDict= Jane.get_PropertyDict()
                    value2= JaneDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        Jane.check_Rail_Count()
                        if Jane.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Danny.set_money(Danny.get_money() - 50)
                            Jane.set_money(Jane.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 2:
                            Danny.set_money(Danny.get_money() - 100)
                            Jane.set_money(Jane.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 3:
                            Danny.set_money(Danny.get_money() - 200)
                            Jane.set_money(Jane.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif Jane.get_railCount() == 4:
                            Danny.set_money(Danny.get_money() - 400)
                            Jane.set_money(Jane.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    play.check_Rail_Count()
                    if play.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Danny.set_money(Danny.get_money() - 50)
                        play.set_money(play.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 2:
                        Danny.set_money(Danny.get_money() - 100)
                        play.set_money(play.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 3:
                        Danny.set_money(Danny.get_money() - 200)
                        play.set_money(play.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif play.get_railCount() == 4:
                        Danny.set_money(Danny.get_money() - 400)
                        play.set_money(play.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Dan owns nearest Rail
                return 5, play, Danny, Jane

    # --------------------------------------
    elif who == Jane.get_name():
        if Jane.getLocation() < 5:
            Jane.specifyLocation(5)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 5, play, Danny, Jane

        elif Jane.getLocation() < 15:
            Jane.specifyLocation(15)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Pennsylvania Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Pennsylvania Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('Pennsylvania Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nPennsylvania Railroad is not owned.\n')
                        return 15, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 15, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 15, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 15, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 15, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 15, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 15, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 15, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 15, play, Danny, Jane

        elif Jane.getLocation() < 25:
            Jane.specifyLocation(25)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('B. & O. Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('B. & O. Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('B. & O. Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nB. & O. Railroad is not owned.\n')
                        return 25, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 25, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 25, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 25, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 25, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 25, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 25, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 25, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 25, play, Danny, Jane

        elif Jane.getLocation() < 35:
            Jane.specifyLocation(35)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Short Line', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Short Line', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('Short Line', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nShort Line is not owned.\n')
                        return 35, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 35, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 35, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 35, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 35, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 35, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 35, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 35, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 35, play, Danny, Jane

        elif Jane.getLocation() > 35:
            Jane.specifyLocation(5)
            JaneDict= Jane.get_PropertyDict()
            value= JaneDict.get('Reading Railroad', 'Entry not found')
            if value == 'Entry not found':
                DanDict= Danny.get_PropertyDict()
                value1= DanDict.get('Reading Railroad', 'Entry not found')
                if value1 == 'Entry not found':
                    playDict= play.get_PropertyDict()
                    value2= playDict.get('Reading Railroad', 'Entry not found')
                    if value2 == 'Entry not found':
                        print('\nReading Railroad is not owned.\n')
                        return 5, play, Danny, Jane
                    else:
                        # Count how many railroad the person has
                        play.check_Rail_Count()
                        if play.get_railCount() == 0:
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 1:
                            # What if they don't have enough money -------------------
                            Jane.set_money(Jane.get_money() - 50)
                            play.set_money(play.get_money() + 50)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 2:
                            Jane.set_money(Jane.get_money() - 100)
                            play.set_money(play.get_money() + 100)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 3:
                            Jane.set_money(Jane.get_money() - 200)
                            play.set_money(play.get_money() + 200)
                            return 5, play, Danny, Jane
                        elif play.get_railCount() == 4:
                            Jane.set_money(Jane.get_money() - 400)
                            play.set_money(play.get_money() + 400)
                            return 5, play, Danny, Jane
                else:
                    Danny.check_Rail_Count()
                    if Danny.get_railCount() == 0:
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 1:
                        # What if they don't have enough money -------------------
                        Jane.set_money(Jane.get_money() - 50)
                        Danny.set_money(Danny.get_money() + 50)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 2:
                        Jane.set_money(Jane.get_money() - 100)
                        Danny.set_money(Danny.get_money() + 100)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 3:
                        Jane.set_money(Jane.get_money() - 200)
                        Danny.set_money(Danny.get_money() + 200)
                        return 5, play, Danny, Jane
                    elif Danny.get_railCount() == 4:
                        Jane.set_money(Jane.get_money() - 400)
                        Danny.set_money(Danny.get_money() + 400)
                        return 5, play, Danny, Jane
            else:
                # Jane owns nearest Rail
                return 5, play, Danny, Jane

def Card16Action(play, Danny, Jane, who):
    print('Plucking Card 16')
    print('You have been elected Chairman of the board, Pay EACH player $50.')
    if who == play.get_name():
        play.set_money(play.get_money() - 100)
        Danny.set_money(Danny.get_money() + 50)
        Jane.set_money(Jane.get_money() + 50)
        return play, Danny, Jane
        
    elif who == Danny.get_name():
        Danny.set_money(Danny.get_money() - 100)
        play.set_money(play.get_money() + 50)
        Jane.set_money(Jane.get_money() + 50)
        return play, Danny, Jane
        
    elif who == Jane.get_name():
        Jane.set_money(Jane.get_money() - 100)
        Danny.set_money(Danny.get_money() + 50)
        play.set_money(play.get_money() + 50)
        return play, Danny, Jane
