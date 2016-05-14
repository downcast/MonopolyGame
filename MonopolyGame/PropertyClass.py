# This class is a base class for the properties

class PropertyDeed:
    def __init__(self):
        self.__name= ''
        self.__owner= 'Free'
        self.__color=''
        self.__price= 0
        self.__rent= 0
        # Price of rent when 1 house is placed on prop
        self.__house1= 0
        self.__haveHouse1= False
        self.__house2= 0
        self.__haveHouse2= False
        self.__house3= 0
        self.__haveHouse3= False
        self.__house4= 0
        self.__haveHouse4= False
        self.__hotel= 0
        self.__haveHotel= False
        self.__morgagevalue= 0
        self.__didMorgage= False
        # Cost of each house
        self.__houseCost= 0

    
    def set_name(self, n):
        self.__name= n

    def get_name(self):
        return self.__name


    def set_owner(self, own):
        self.__owner= own

    def get_owner(self):
        return self.__owner


    def set_color(self, col):
        self.__color= col

    def get_color(self):
        return self.__color


    def set_price(self, p):
        self.__price= p

    def get_price(self):
        return self.__price


    def set_rent(self, r):
        self.__rent= r

    def get_rent(self):
        return self.__rent
    

    def set_house1(self, cost):
        self.__house1= cost

    def get_house1(self):
        return self.__house1

    def set_have_house1(self, answer):
        self.__haveHouse1= answer

    def get_have_house1(self):
        return self.__haveHouse1
    

    def set_house2(self, cost):
        self.__house2= cost

    def get_house2(self):
        return self.__house2

    def set_have_house2(self, answer):
        self.__haveHouse2= answer

    def get_have_house2(self):
        return self.__haveHouse2


    def set_house3(self, cost):
        self.__house3= cost

    def get_house3(self):
        return self.__house3

    def set_have_house3(self, answer):
        self.__haveHouse3= answer

    def get_have_house3(self):
        return self.__haveHouse3
    

    def set_house4(self, cost):
        self.__house4= cost

    def get_house4(self):
        return self.__house4

    def set_have_house4(self, answer):
        self.__haveHouse4= answer

    def get_have_house4(self):
        return self.__haveHouse4


    def set_hotel(self, cost):
        self.__hotel= cost

    def get_hotel(self):
        return self.__hotel

    def set_have_hotel(self, answer):
        self.__haveHotel= answer

    def get_have_hotel(self):
        return self.__haveHotel


    def set_morgage_val(self, v):
        self.__morgagevalue= v

    def get_morgage_val(self):
        return self.__morgagevalue
    

    def set_did_Morgage(self, answer):
        self.__didMorgage= answer

    def get_did_Morgage(self):
        return self.__didMorgage
    

    def set_house_Cost(self, cost):
        self.__houseCost= cost

    def get_house_Cost(self):
        return self.__houseCost
