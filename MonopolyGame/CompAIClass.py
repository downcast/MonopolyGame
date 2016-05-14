# This class is the AI for the computer class
from time import sleep
import random
import tkinter
import tkinter.messagebox

class ComputerAI:
    def __init__(self, GlobalPropDict, computer, Property_LocationDict):
        
        self.__diceValue = 0
        self.PropDict= GlobalPropDict
        self.__Computer= computer
        self.__PropLocationDict= Property_LocationDict
        self.__jailTimeCount= 0


    def setDiceValue(self, value):
        self.__diceValue = value

    def getDiceValue(self):
        return self.__diceValue


    def RollDice(self):
        print('Rolling...')
        sleep(2)
        d1= random.randint(1, 6)
        d2= random.randint(1, 6)
        if d1 == d2:
            self.setDiceValue(d1+d2)
            print(self.__Computer.get_name(), 'rolled double,', d1)
            sleep(2)
            return True
        else:
            self.setDiceValue(d1+d2)
            print(self.__Computer.get_name(), 'rolled', self.getDiceValue())
            sleep(2)
            return False

    def BuyProp(self):
        # Get the location of the comp 
        location= self.__Computer.getLocation()
        # Use the location as a key to get the property name of the space
        key= self.__PropLocationDict[location]
        if key == 'Chance' or key == 'Community Chest':
            return
        elif key == 'GO' or key == 'Income Tax':
            return
        elif key == 'Just Visiting' or key == 'Free Parking':
            return
        elif key == 'Go To Jail' or key == 'Luxury Tax':
            return
        else:
            # Get the property obj of the property
            obj= self.PropDict[key]
            x= self.__Computer.get_money() - obj.get_price()
            if x < 0:
                return
            else:
                if obj.get_owner() != 'Free':
                    return
                else:
                    # Send the obj property to the comp property dictionary
                    self.__Computer.addProperty(obj.get_name(), obj)
                    # Change the owner of the property to the comp
                    obj.set_owner(self.__Computer.get_name())
                    self.PropDict[key]= obj
                    self.__Computer.set_money(x)


    def JailBird(self, jailTimeCount):
        prib
    def ViewProp(self):
        print(self.__Computer.get_name(), 'owns: ')
        self.__Computer.displayProp()
