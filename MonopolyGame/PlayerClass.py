# This class holds the player info
import tkinter
import tkinter.messagebox

class Player:
    def __init__(self):
        
        self.__name= ''
        self.__money= 1500
        self.__token= ''
        self.__property_Dict= {}
        self.__location=0
        self.__jail_Bird= False
        self.__Out_of_Jail_Card= False
        self.__railCount= 0

    def get_railCount(self):
        return self.__railCount

    def set_propertyDict(self, propdict):
        self.__property_Dict= propdict

    def getPropListasString(self):
        target= ''
        for key in self.__property_Dict:
            obj= self.__property_Dict[key]
            # Set name of property to string
            string= obj.get_name()
            # Concatenate strings to form a long list of strings
            target = target + '\n' + string
        return target
    
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


    def set_jail_Bird(self, answer):
        self.__jail_Bird = answer

    def get_jail_Bird(self):
        return self.__jail_Bird
    
    def addProperty(self, name, obj):
        if name in self.__property_Dict:
            print('already in')
        else:
            obj.set_owner(self.get_name())
            self.__property_Dict[name]= obj

    def get_PropertyDict(self):
        return self.__property_Dict

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
        

    def get_name(self):
        return self.__name

    def set_money(self, value):
        self.__money = value
        
    def get_money(self):
        return self.__money

    def get_token(self):
        return self.__token

    def set_Out_of_Jail_Card(self, anwer):
        self.__Out_of_Jail_Card= anwer

    def get_Out_of_Jail_Card(self):
        return self.__Out_of_Jail_Card

    def StartingGUI(self):
        
        # This is Pop up window that allows the user to enter name and choose token. 
        self.inputWindow= tkinter.Tk(className=' Monopoly - Entry Window')
        self.inputWindow.minsize(300, 125)

        # Top frame --------------
        self.top_frame= tkinter.Frame()
        self.mid_frame= tkinter.Frame()
        self.bot_frame= tkinter.Frame()

        # Calls nameCharCount every time a character is entered
        checkName= (self.inputWindow.register(self.nameCharCount), '%P')
        
        self.nameLabel= tkinter.Label(self.top_frame, text='Enter your name. (Max chars 11):')
        self.nameEntry= tkinter.Entry(self.top_frame, validate='key', validatecommand= checkName, width=11)

        self.nameLabel.pack(side='left')
        self.nameEntry.pack(side='left')
        # Top frame --------------
        
        # Mid Frame --------------
        self.radio_var= tkinter.IntVar()

        self.radio_var.set(1)

        self.rb1= tkinter.Radiobutton(self.mid_frame, text='Hat', variable=self.radio_var, value=1)
        self.rb2= tkinter.Radiobutton(self.mid_frame, text='Cat', variable=self.radio_var, value=2)
        self.rb3= tkinter.Radiobutton(self.mid_frame, text='Car', variable=self.radio_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        # Mid Frame --------------

        # Bottom Frame -----------
        self.Confirm_button= tkinter.Button(self.bot_frame, text='Continue', command=self.confirmEntry)
        
        self.Confirm_button.pack()
        # Bottom Frame------------
        
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        tkinter.mainloop()

    def nameCharCount(self, P):
        # Allow only if the total length of the name is <= 11
        return (len(P) <= 11)
    
    def getToken(self):
        print(self.__token)
        
    def confirmEntry(self):

        self.__name= self.nameEntry.get()
        
        if str(self.radio_var.get()) == '1':
            self.__token= 'Hat'
        elif str(self.radio_var.get()) == '2':
            self.__token= 'Cat'
        elif str(self.radio_var.get()) == '3':
            self.__token= 'Car'

        self.inputWindow.destroy()

# Remove this gui
    def gui(self):

        #Pop up window that display all of the Player info
        self.PlayerStats= tkinter.Tk(className=' Player Information')
        self.PlayerStats.minsize(225, 75)

        self.name_Label= tkinter.Label(self.PlayerStats, text='Name: ' + self.__name)
        self.money_Label= tkinter.Label(self.PlayerStats, text='Money: ' + str(self.__money))

        self.roll_but= tkinter.Button(self.PlayerStats, text='Confirm', command=self.txt)

        self.name_Label.pack()
        self.money_Label.pack()
        self.roll_but.pack()

        tkinter.mainloop()
    
    def txt(self):
        self.PlayerStats.destroy()

