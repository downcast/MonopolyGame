# This class holds the computer info
import tkinter
import tkinter.messagebox

class Computer:
    def __init__(self, name):
        
        self.__name= name
        self.__money= 1500
        self.__token= ''
        self.__property_Dict= {}
        self.__location= 0
        self.__jail_Bird= False
        self.__Out_of_Jail_Card= False
        self.__railCount= 0

    def addProperty(self, name, obj):
        obj.set_owner(self.get_name())
        self.__property_Dict[name]= obj

    def get_PropertyDict(self):
        return self.__property_Dict

    def getPropListasString(self):
        target= ''
        for key in self.__property_Dict:
            obj= self.__property_Dict[key]
            # Set name of property to string
            string= obj.get_name()
            # Concatenate strings to form a long list of strings
            target = target + '\n' + string
        return target
            
    def displayProp(self):
        for key in self.__property_Dict:
            obj= self.__property_Dict[key]
            print(obj.get_name())

    def specifyLocation(self, value):
        self.__location= value

        
    def setLocation(self, value):
        self.__location += value
        if self.getLocation() >= 40:
            self.__location -= 40
            # Passing Go adds 200
            self.__money += 200

    def getLocation(self):
        return self.__location

    def set_name(self, name):
        self.__name= name
        # Erorr check the char number

    def get_name(self):
        return self.__name

    def set_money(self, value):
        self.__money = value
        
    def get_money(self):
        return self.__money

    def set_token(self, tok):
        self.__token= tok

    def get_token(self):
        return self.__token

    def set_jail_Bird(self, answer):
        self.__jail_Bird = answer

    def get_jail_Bird(self):
        return self.__jail_Bird

    def set_Out_of_Jail_Card(self, anwer):
        self.__Out_of_Jail_Card= anwer

    def get_Out_of_Jail_Card(self):
        return self.__Out_of_Jail_Card
    
    def get_railCount(self):
        return self.__railCount

    def check_Rail_Count(self):
        self.__railCount= 0
        value= self.__property_Dict.get('Reading Railroad', 'Entry not found')
        if value != 'Entry not found':
            self.__railCount+= 1
            value1= self.__property_Dict.get('Pennsylvania Railroad', 'Entry not found')
            if value1 != 'Entry not found':
                self.__railCount+= 1
                value2= self.__property_Dict.get('B. & O. Railroad', 'Entry not found')
                if value2 != 'Entry not found':
                    self.__railCount+= 1
                    value3= self.__property_Dict.get('Short Line', 'Entry not found')
                    if value3 != 'Entry not found':
                        self.__railCount+= 1

