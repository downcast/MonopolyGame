# This class is the base class for Utilities

class Utility:
    def __init__(self):
        self.__owner= 'Free'
        self.__color= ''
        self.__name= ''
        self.__price= 0
        self.__morgagevalue= 0
        self.__didMorgage= False


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


    def set_morgage_val(self, v):
        self.__morgagevalue= v

    def get_morgage_val(self):
        return self.__morgagevalue
    

    def set_did_Morgage(self, answer):
        self.__didMorgage= answer

    def get_did_Morgage(self):
        return self.__didMorgage
