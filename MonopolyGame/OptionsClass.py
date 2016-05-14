import tkinter
import tkinter.messagebox
import pygame
import PlayerClass 
import random

class Options:

    def __init__(self, answer, GlobalPropDict, player, Property_LocationDict, Danny, Jane):

        pygame.mixer.init()
        self.__diceValue = 0
        self.__didRoll = answer
        ######
        self.Isturn= True
        self.endGame= False
        #####
        self.PropDict= GlobalPropDict
        self.__Player= player
        self.__Danny= Danny
        self.__Jane= Jane
        self.__PropLocationDict= Property_LocationDict
        self.__jailTimeCount= 0
        self.__TradeList= []


    def getPlayer(self):
        return self.__Player

    def getDanny(self):
        return self.__Danny

    def getJane(self):
        return self.__Jane
    
    def setjailTimeCount(self, count):
        jailTimeCount= count

    def getjailTimeCount(self):
        return jailTimeCount
    
    def setDiceValue(self, value):
        self.__diceValue = value

    def getDiceValue(self):
        return self.__diceValue

    def setdidRoll(self, answer):
        self.__didRoll = answer

    def getdidRoll(self):
        return self.__didRoll

    
    def RollDice(self):
        if self.getdidRoll() == False:
            sound= pygame.mixer.Sound('Dice Roll.wav')
            sound.play()
            
            d1= random.randint(1, 6)
            d2= random.randint(1, 6)
            self.setdidRoll(True)
            if d1 == d2:
                self.setDiceValue(d1 + d2)
                sound.play()
                tkinter.messagebox.showinfo('Results!', 'You rolled double ' + str(d1) + " \nRoll again.")
                self.setdidRoll(False)
                self.gui.destroy()
                
            else:
                x = d1+d2
                self.setDiceValue(x)
                tkinter.messagebox.showinfo('Results', 'You rolled ' + str(x))
                self.gui.destroy()
        else:
            sound2= pygame.mixer.Sound('Denied Sound Effect.wav')
            sound2.play()
            tkinter.messagebox.showinfo('Warning!', 'You already rolled. ')
            
        
    def BuyProp(self):
        # Get the location of the player 
        location= self.__Player.getLocation()
        # Use the location as a key to get the property name of the space
        key= self.__PropLocationDict[location]
        
        if key == 'Chance' or key == 'Community Chest':
            tkinter.messagebox.showinfo('Warning!', "You can't buy this. ")
        elif key == 'GO' or key == 'Income Tax':
            tkinter.messagebox.showinfo('Warning!', "You can't buy this. ")
        elif key == 'Just Visiting' or key == 'Free Parking':
            tkinter.messagebox.showinfo('Warning!', "You can't buy this. ")
        elif key == 'Go To Jail' or key == 'Luxury Tax':
            tkinter.messagebox.showinfo('Warning!', "You can't buy this. ")
        else:
            
            # Get the property obj of the property
            obj= self.PropDict[key]
            # Make sure player has enough money
            x= self.__Player.get_money() - obj.get_price()
            if x < 0:
                tkinter.messagebox.showinfo('Warning!', "Insufficient Funds. ")
            else:
                # Make sure the property is not owned
                if obj.get_owner() != 'Free':
                    tkinter.messagebox.showinfo('Warning!', "Property already owned. ")
                else:
                    # Send the obj property to the player property dictionary
                    self.__Player.addProperty(obj.get_name(), obj)
                    # Change the owner of the property to the player to allow the player to see all available property
                    obj.set_owner(self.__Player.get_name())
                    self.PropDict[key]= obj
                    self.__Player.set_money(x)
                
    
    def TradePropGUI(self):
        # Gui window visible to the player
        self.TradingGUI= tkinter.Tk(className=' Trading Property')

        self.nameLabel= tkinter.Label(self.TradingGUI, text='Who would you like to trade with? ')
        self.nameEntry= tkinter.Entry(self.TradingGUI, width=6)
        self.Confirm_button= tkinter.Button(self.TradingGUI, text='Confirm', command=self.TradeProp)
        
##        tkinter.messagebox.showinfo('Trade Property', 'Follow the directions in the python shell.')
##        self.turn = 'trade'
##        self.gui.destroy()
        self.nameLabel.pack(side='left')
        self.nameEntry.pack(side='left')
        self.Confirm_button.pack()
        
        tkinter.mainloop()

    def PropMoneyReEnter(self):
        # Create new GUI to get how much cash the player wants to give up or get
        self.PropExchangeGUI3= tkinter.Tk(className=' Trading Property')

        # Display message to player
        self.cashLabel= tkinter.Label(self.PropExchangeGUI3, text='How much cash do you want to give?')
        # Get player to enter number
        self.cashEntry= tkinter.Entry(self.PropExchangeGUI3, width=20)
        # Create 'Confirm' button
        self.confirmButton= tkinter.Button(self.PropExchangeGUI3, text='Confirm', command=self.PropExchangeAction)

        # Pack Label, Entry and Button
        self.cashLabel.pack()
        self.cashEntry.pack()

        self.confirmButton.pack()

        tkinter.messagebox.showinfo('Information', "Enter a negative to GET cash from computer.\nEg. -240")
        tkinter.mainloop()
    
    def PropMoneyCheck(self):
        # Get user input from previous gui
        choice= self.choiceEntry.get()

        if choice == 'Yes' or choice == 'No':
            if choice == 'Yes':
                self.PropExchangeGUI3()
        
    def PropExchangeAction(self):
        # Get user input from previous gui
        money= self.cashEntry.get()

        # Destroy previous Gui
        self.PropExchangeGUI3.destroy()
    
        self.__TradeList.append(money)

        # Validate player input and test for negative number
        if money[0] == '-':
            # Slice the string to remove the negative
            substring= money[1:]
            substring= int(substring)
            if self.__Danny.get_money() - substring < 0:
                self.checkScreen= tkinter.Tk()

                # Display message to player
                self.choiceLabel= tkinter.Label(self.checkScreen, text="Enter 'Yes' or 'No':")
                # Get player to enter name
                self.choiceEntry= tkinter.Entry(self.checkScreen, width=3)
                # Create 'Confirm' button
                self.continueButton= tkinter.Button(self.checkScreen, text='Continue', command=self.PropMoneyCheck)

                # Pack Label, Entry and Button
                self.choiceLabel.pack()
                self.choiceEntry.pack()

                self.continueButton.pack()
                
                tkinter.messagebox.showinfo('Warning', "Danny does not have enough money.\nEnter 'Yes' if would want to enter another number.\nEnter 'No' if not.")
                tkinter.mainloop()
            else:
                self.__Danny.set_money(self.__Danny.get_money() - substring)
                self.__Player.set_money(self.__Player.get_money() + substring)
                    
        else:
            money= int(money)
            if self.__Player.get_money() - money > 0:
                self.__Player.set_money(self.__Player.get_money() - money)
                self.__Danny.set_money(self.__Danny.get_money() + money)
                
##            print('pos')
##        print(self.__TradeList)
        
    def PropExchange1(self):
        
        # Create new GUI to get name of properties the player wants
        self.PropExchangeGUI1= tkinter.Tk(className=' Trading Property')

        # Display message to player
        self.propLabel= tkinter.Label(self.PropExchangeGUI1, text='Enter the name of the property you want:')
        # Get player to enter name
        self.propEntry= tkinter.Entry(self.PropExchangeGUI1, width=20)
        # Create 'Confirm' button
        self.confirmButton= tkinter.Button(self.PropExchangeGUI1, text='Confirm', command=self.PropExchange2)

        # Pack Label, Entry and Button
        self.propLabel.pack()
        self.propEntry.pack()

        self.confirmButton.pack()

        tkinter.messagebox.showinfo('Information', "Enter 'None' in any of the property fields to NOT trade for that field.")
        tkinter.mainloop()

    def PropExchange2(self):
        # Get user input from previous gui
        wantProp= self.propEntry.get()

        # Destroy previous Gui
        self.PropExchangeGUI1.destroy()

        # Validate player input
        if wantProp in self.__Danny.get_PropertyDict() or wantProp == 'None':
            self.__TradeList.append(wantProp)
            
            # Create new GUI to get name of properties the player wants to give up
            self.PropExchangeGUI2= tkinter.Tk(className=' Trading Property')

            # Display message to player
            self.propLabel= tkinter.Label(self.PropExchangeGUI2, text='Enter the name of the property you want to give up:')
            # Get player to enter name
            self.propEntry= tkinter.Entry(self.PropExchangeGUI2, width=20)
            # Create 'Confirm' button
            self.confirmButton= tkinter.Button(self.PropExchangeGUI2, text='Confirm', command=self.PropExchange3)

            # Pack Label, Entry and Button
            self.propLabel.pack()
            self.propEntry.pack()

            self.confirmButton.pack()
            tkinter.messagebox.showinfo(self.__Player.get_name() + "'s Property List", self.__Player.get_name() + 's Property List:\n' + self.__Player.getPropListasString())
            print("-- ", self.__Player.get_name(), "'s Property --", sep='')
            print('\n' + self.__Player.getPropListasString())
            tkinter.mainloop()
        else:
            tkinter.messagebox.showinfo('Warning', wantProp + " is not owned by Danny.\nEnter another property.")
            # Call the previous gui again to allow the player to reenter name
            self.PropExchange1()

    def PropExchange3(self):
        # Get the user input fron the previous gui
        giveProp= self.propEntry.get()

        # Destroy previous Gui
        self.PropExchangeGUI2.destroy()

        # Validate player input
        if giveProp in self.__Player.get_PropertyDict() or giveProp == 'None':
            self.__TradeList.append(giveProp)
            
            # Create new GUI to get how much cash the player wants to give up or get
            self.PropExchangeGUI3= tkinter.Tk(className=' Trading Property')
                           
            # Display message to player
            self.cashLabel= tkinter.Label(self.PropExchangeGUI3, text='How much cash do you want to give?')
            # Get player to enter number
            self.cashEntry= tkinter.Entry(self.PropExchangeGUI3, width=20)
            # Create 'Confirm' button
            self.confirmButton= tkinter.Button(self.PropExchangeGUI3, text='Confirm', command=self.PropExchangeAction)

            # Pack Label, Entry and Button
            self.cashLabel.pack()
            self.cashEntry.pack()

            self.confirmButton.pack()

            tkinter.messagebox.showinfo('Information', "Enter a negative to GET cash from computer.\nEg. -240.90")
            tkinter.mainloop()
        else:
            tkinter.messagebox.showinfo('Warning', giveProp + " is not owned by you, squatter.\nEnter a property you LEGALLY own.")
            # Call the previous gui again to allow the player to reenter name
            self.PropExchange2()
        
    def TradeProp(self):
        if self.nameEntry.get() == self.__Danny.get_name() or self.nameEntry.get() == self.__Jane.get_name():
            if self.nameEntry.get() == self.__Danny.get_name():
                # Display list of Danny's properties
                tkinter.messagebox.showinfo("Danny's Property List", "Danny's Property List:\n" + self.__Danny.getPropListasString())
                # Print list in shell just in case
                print("-- Danny's Property --")
                print('\n' + self.__Danny.getPropListasString())
                # Destroy the 'TradingGUI'
                self.TradingGUI.destroy()
                self.PropExchange1()
                
            elif self.nameEntry.get() == self.__Jane.get_name():
                print('sin')
            
        else:
            tkinter.messagebox.showinfo('Warning', self.nameEntry.get() + ' is not a player. \nEnter Danny or Jane.')

    def MorgagePropGUI(self):
        # Enter the name of the prop u want to remove
        # check player prop dict to see if its there, if its there, add morgage value to money and set ismorgage to true
        # add property of rent to check if prop is morgaged
        self.MorgageGui= tkinter.Tk(className=' Mortgage Property')

        self.nameLabel= tkinter.Label(self.MorgageGui, text='Enter the name of your property you would like to mortgage or unmortgage:')
        self.nameEntry= tkinter.Entry(self.MorgageGui, width=20)
        self.Confirm_button= tkinter.Button(self.MorgageGui, text='Continue', command=self.MorgageProp)

        self.nameLabel.pack(side='left')
        self.nameEntry.pack(side='left')
        self.Confirm_button.pack()
        
        tkinter.mainloop()

    def MorgageProp(self):
        propName= self.nameEntry.get()
        if propName in self.__Player.get_PropertyDict():
            dictx= self.__Player.get_PropertyDict()
            x= dictx[propName]
            if x.get_did_Morgage() == False:
                x.set_did_Morgage(True)
                self.__Player.set_money(x.get_morgage_val() + self.__Player.get_money())
                self.DestroyMorgagePropGUI()
            elif x.get_did_Morgage() == True:
                print('This property is mortgaged.')
                x.set_did_Morgage(False)
                self.__Player.set_money(self.__Player.get_money()- x.get_morgage_val())
                print(x.get_name(), 'is now unmortgaged.')
                self.DestroyMorgagePropGUI()
        else:
            print(propName, 'is not owned by you.')
            

    def ViewAvailProp(self):
        for key in self.PropDict:
            obj= self.PropDict[key]
            if obj.get_owner() == 'Free':
                print(obj.get_name())

    def ViewProp(self):
        self.__Player.displayProp()

    def JailEndTurn(self):
        #################333
        self.Isturn= False
        self.gui.destroy()

    def EndTurn(self):
        self.Isturn = False
        self.gui.destroy()

    def DestroyMorgagePropGUI(self):
        self.MorgageGui.destroy()

    def AddHousesGUI1(self):
        self.AddHousesGui1= tkinter.Tk(className=' Add Houses and Hotels')

        self.nameLabel= tkinter.Label(self.AddHousesGui1, text='Enter the name of your property you would like to add Houses and Hotels to:')
        self.nameEntry= tkinter.Entry(self.AddHousesGui1, width=20)
        self.Confirm_button= tkinter.Button(self.AddHousesGui1, text='Continue', command=self.AddHousesGUI2)

        self.nameLabel.pack(side='left')
        self.nameEntry.pack(side='left')
        self.Confirm_button.pack()
        
        tkinter.mainloop()

    def AddHousesGUI2(self):
        self.AddHousesGui2= tkinter.Tk(className=' Add Houses and Hotels')

        self.houseNumLabel= tkinter.Label(self.AddHousesGui2, text='Enter the number of houses you want to buy. (Enter 5 for four houses and a hotel):')
        self.houseNumEntry= tkinter.Entry(self.AddHousesGui2, width= 2)
        self.Confirm_button= tkinter.Button(self.AddHousesGui2, text='Continue', command=self.AddHouses)

        self.houseNumLabel.pack(side='left')
        self.houseNumEntry.pack(side='left')
        self.Confirm_button.pack()
        
        tkinter.mainloop()

    def AddHouses(self):
        # Error----- Add can only add houses if all three colors are owned and uneven house numbers are not allowed
        propName= self.nameEntry.get()
        houseNum= int(self.houseNumEntry.get())
        
        self.AddHousesGui1.destroy()
        self.AddHousesGui2.destroy()
        
        if propName in self.__Player.get_PropertyDict():
            while houseNum <= 0 or houseNum > 5:
                tkinter.messagebox.showinfo('Warning!', "Invalid Entry, re-enter the number of house you would like in the Python shell. ")
                houseNum = input('Number of houses you want to add to', propName)

            dictx= self.__Player.get_PropertyDict()
            x= dictx[propName]
            if x.get_did_Morgage() == False:
                if x.get_have_hotel() == True:
                    tkinter.messagebox.showinfo('Warning!', "You already have a hotel. ")
                elif x.get_have_house4() == True:
                    if houseNum >= 1:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - x.get_house_Cost()
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - x.get_house_Cost())
                            x.set_have_hotel(True)
                            # Set the hotel rent value to the rent
                            x.set_rent(x.get_hotel())
                            tkinter.messagebox.showinfo('Information!', 'You now have a hotel on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')
                elif x.get_have_house3() == True:
                    if houseNum == 1:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - x.get_house_Cost()
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - x.get_house_Cost())
                            x.set_have_house4(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house4())
                            tkinter.messagebox.showinfo('Information!', 'You now have 4 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')
                            
                    elif houseNum >= 2:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 2*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 2*(x.get_house_Cost()))
                            x.set_have_hotel(True)
                            # Set the hotel rent value to the rent
                            x.set_rent(x.get_hotel())
                            tkinter.messagebox.showinfo('Information!', 'You now have a hotel on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')

                elif x.get_have_house2() == True:
                    if houseNum == 1:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - x.get_house_Cost()
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - x.get_house_Cost())
                            x.set_have_house3(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house3())
                            tkinter.messagebox.showinfo('Information!', 'You now have 3 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')

                    elif houseNum == 2:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 2*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 2*(x.get_house_Cost()))
                            x.set_have_house4(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house4())
                            tkinter.messagebox.showinfo('Information!', 'You now have 4 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')
                            
                    elif houseNum >= 3:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 3*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 3*(x.get_house_Cost()))
                            x.set_have_hotel(True)
                            # Set the hotel rent value to the rent
                            x.set_rent(x.get_hotel())
                            tkinter.messagebox.showinfo('Information!', 'You now have a hotel on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')

                elif x.get_have_house1() == True:
                    if houseNum == 1:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - x.get_house_Cost()
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - x.get_house_Cost())
                            x.set_have_house2(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house2())
                            tkinter.messagebox.showinfo('Information!', 'You now have 2 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')

                    elif houseNum == 2:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 2*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 2*(x.get_house_Cost()))
                            x.set_have_house3(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house3())
                            tkinter.messagebox.showinfo('Information!', 'You now have 3 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')
                            
                    elif houseNum == 3:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 3*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 3*(x.get_house_Cost()))
                            x.set_have_house4(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house4())
                            tkinter.messagebox.showinfo('Information!', 'You now have 4 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')

                            
                    elif houseNum == 4:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 4*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 4*(x.get_house_Cost()))
                            x.set_have_hotel(True)
                            # Set the hotel rent value to the rent
                            x.set_rent(x.get_hotel())
                            tkinter.messagebox.showinfo('Information!', 'You now have a hotel on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')

                else:
                    if houseNum == 1:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - x.get_house_Cost()
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - x.get_house_Cost())
                            x.set_have_house1(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house1())
                            del dictx[propName]
                            dictx[propName]= x
                            self.__Player.set_propertyDict(dictx)
                            tkinter.messagebox.showinfo('Information!', 'You now have 1 house on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')

                    elif houseNum == 2:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 2*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 2*(x.get_house_Cost()))
                            x.set_have_house2(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house2())
                            tkinter.messagebox.showinfo('Information!', 'You now have 2 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')
                            
                    elif houseNum == 3:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 3*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 3*(x.get_house_Cost()))
                            x.set_have_house3(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house3())
                            tkinter.messagebox.showinfo('Information!', 'You now have 3 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')

                    elif houseNum == 4:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 4*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 4*(x.get_house_Cost()))
                            x.set_have_house4(True)
                            # Set the house rent value to the rent
                            x.set_rent(x.get_house4())
                            tkinter.messagebox.showinfo('Information!', 'You now have 3 houses on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')
                            
                    elif houseNum == 5:
                        # Check to see if the player has enough money
                        remainMoney= self.__Player.get_money() - 5*(x.get_house_Cost())
                        if remainMoney > 0:
                            # Deduct money
                            self.__Player.set_money(self.__Player.get_money() - 5*(x.get_house_Cost()))
                            x.set_have_hotel(True)
                            # Set the hotel rent value to the rent
                            x.set_rent(x.get_hotel())
                            tkinter.messagebox.showinfo('Information!', 'You now have a hotel on,' + propName)
                        else:
                            tkinter.messagebox.showinfo('Warning!', 'You do not have enough money.')
                    
                    
            elif x.get_did_Morgage() == True:
                print('You cannot add houses to mortgaged property.')
        else:
            print(propName, 'is not owned by you. You cannot add houses')
        
    def EndGame(self):
        self.endGame= True
        self.gui.destroy()
        
        
    def OptionsGUI(self):
        
        #if state == 'PlayerTurn':

        self.gui= tkinter.Tk(className=' Player Options')
        self.gui.minsize(210, 235)

        # Frames ------------------------
        self.AvailablePropframe= tkinter.Frame()
        self.PlayerPropframe= tkinter.Frame()
        self.MorgagePropframe= tkinter.Frame()
        self.TradePropframe= tkinter.Frame()
        self.AddHousesframe= tkinter.Frame()
        self.BuyPropframe= tkinter.Frame()
        self.Rollframe= tkinter.Frame()
        self.EndTurnframe= tkinter.Frame()
        self.EndGameframe= tkinter.Frame()
        # Frames ------------------------

        # Buttons ------------------------
        self.available_prop_but= tkinter.Button(self.AvailablePropframe, text='View Available Property', command=self.ViewAvailProp)
        self.player_prop_but= tkinter.Button(self.PlayerPropframe, text='View Your Property', command=self.ViewProp)
        self.morgage_prop_but= tkinter.Button(self.MorgagePropframe, text='Mortgage Your Property', command=self.MorgagePropGUI)
        self.trade_prop_but= tkinter.Button(self.TradePropframe, text='Trade Your Property', command=self.TradePropGUI)
        self.add_houses_but= tkinter.Button(self.AddHousesframe, text='Add Houses and Hotels', command=self.AddHousesGUI1)
        self.buy_prop_but= tkinter.Button(self.BuyPropframe, text='Buy Property', command=self.BuyProp)
        self.roll_button= tkinter.Button(self.Rollframe, text='Roll Dice', command=self.RollDice)
        self.end_turn_but= tkinter.Button(self.EndTurnframe, text='End Turn', command=self.EndTurn)
        self.end_game_but= tkinter.Button(self.EndGameframe, text='End Game', command= self.EndGame)
        # Buttons ----------------------

        # Pack buttons -----------
        self.available_prop_but.pack()
        self.player_prop_but.pack()
        self.morgage_prop_but.pack()
        self.trade_prop_but.pack()
        self.add_houses_but.pack()
        self.buy_prop_but.pack()
        self.roll_button.pack()
        self.end_turn_but.pack()
        self.end_game_but.pack()
        # Pack buttons -----------

        # Pack frames ----------
        self.AvailablePropframe.pack()
        self.PlayerPropframe.pack()
        self.MorgagePropframe.pack()
        self.TradePropframe.pack()
        self.AddHousesframe.pack()
        self.BuyPropframe.pack()
        self.Rollframe.pack()
        self.EndTurnframe.pack()
        self.EndGameframe.pack()
        # Pack frames -----------
        
        tkinter.mainloop()

##        else:
##            print('Not player turn.')

    def JailGUI(self, jailTimeCount):
        self.setjailTimeCount(jailTimeCount)
        self.gui= tkinter.Tk(className=' JailBird Options')
        self.gui.minsize(210, 180)
        
        if jailTimeCount == 3:
            tkinter.messagebox.showinfo('Free Man!', "You have been release from prison. Collect $100 on your way out. ")
            self.__Player.set_money(self.__Player.get_money() + 100)
            self.__Player.set_jail_Bird(False)
            self.EndTurn()
        else:
            
            # Frames ------------------------
            self.AvailablePropframe= tkinter.Frame()
            self.PlayerPropframe= tkinter.Frame()
            self.MorgagePropframe= tkinter.Frame()
            self.TradePropframe= tkinter.Frame()
            self.PayFineframe= tkinter.Frame()
            self.Rollframe= tkinter.Frame()
            self.EndTurnframe= tkinter.Frame()
            # Frames ------------------------

            # Buttons ------------------------
            self.available_prop_but= tkinter.Button(self.AvailablePropframe, text='View Available Property', command=self.ViewAvailProp)
            self.player_prop_but= tkinter.Button(self.PlayerPropframe, text='View Your Property', command=self.ViewProp)
            self.morgage_prop_but= tkinter.Button(self.MorgagePropframe, text='Mortgage Your Property', command=self.MorgagePropGUI)
            self.trade_prop_but= tkinter.Button(self.TradePropframe, text='Trade Your Property', command=self.TradeProp)
            self.pay_fine_but= tkinter.Button(self.PayFineframe, text='Pay Fine', command=self.PayFine)
            self.roll_button= tkinter.Button(self.Rollframe, text='Roll Dice', command=self.JailRollDice)
            self.end_turn_but= tkinter.Button(self.EndTurnframe, text='End Turn', command=self.EndTurn)
            # Buttons ----------------------

            # Pack buttons -----------
            self.available_prop_but.pack()
            self.player_prop_but.pack()
            self.morgage_prop_but.pack()
            self.trade_prop_but.pack()
            self.pay_fine_but.pack()
            self.roll_button.pack()
            self.end_turn_but.pack()
            # Pack buttons -----------

            # Pack frames ----------
            self.AvailablePropframe.pack()
            self.PlayerPropframe.pack()
            self.MorgagePropframe.pack()
            self.TradePropframe.pack()
            self.PayFineframe.pack()
            self.Rollframe.pack()
            self.EndTurnframe.pack()
            # Pack frames -----------
            
            tkinter.mainloop()

    def JailRollDice(self):
        if self.getdidRoll() == False:
            d1= random.randint(1, 6)
            d2= random.randint(1, 6)
            self.setdidRoll(True)
            if d1 == d2:
                self.setDiceValue(d1 + d2)
                self.__Player.set_jail_Bird(False)
                tkinter.messagebox.showinfo('Free Man!', 'You rolled double ' + str(d1) + " You have been release from prison. Collect $100 on your way out. ")
                self.__Player.set_money(self.__Player.get_money() + 100)
                self.setdidRoll(False)
                self.EndTurn()
            else:
                x = d1+d2
                tkinter.messagebox.showinfo('Results', 'You rolled ' + str(x) + '. Sorry, you are still in prison.')
        else:
            tkinter.messagebox.showinfo('Warning!', 'You already rolled. ')


    def PayFine(self):
        tkinter.messagebox.showinfo('Pay Jail Fines', 'You have paid $150 in jail fines.')
        self.__Player.set_money(self.__Player.get_money() - 150)
        self.__Player.set_jail_Bird(False)
        self.EndTurn()
        
