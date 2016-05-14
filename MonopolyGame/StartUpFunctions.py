# Descrip: This is a list of functions that load the properties, Chance and Community Cards into seperate dictionaries
# Note: The 'loadChanceCards' and 'loadCommunityCards' functions each set their respective 'cardaction' functions from their respective imported
        # 'CardActions' py files to a variable that is passed to each card obj and is stored in a 'do_action' function that executes
        # the function passed in through the variable
        
import RailRoadClass
import PropertyClass
import UtilityClass
import ChanceCardsClass
import CommunityChestClass
import ChanceCardsClass
import ChanceCardActions
import CommunityCardActions
import pickle

def loadProperties():
    # Descrip: Loads the property dictionary from the 'GlobalPropDict' file
    
    # Determines if 'inFile' is empty
    IsEmpty= True

    inFile= open("GlobalPropDict.txt", 'rb')

    try:
        GlobalPropDict= pickle.load(inFile)
        IsEmpty= False

    except EOFError:
        IsEmpty= True

    inFile.close()

    # If the 'inFile' is empty, go and write property values to an obj and write to a file
    if IsEmpty == True:
        
        GlobalPropDict= {}

        Railobj1= RailRoadClass.RailRoad()
        Railobj1.set_name('Reading Railroad')
        Railobj1.set_color('Rail')
        Railobj1.set_price(200)
        Railobj1.set_morgage_val(100)

        GlobalPropDict['Reading Railroad']= Railobj1

        Railobj2= RailRoadClass.RailRoad()
        Railobj2.set_name('Short Line')
        Railobj2.set_color('Rail')
        Railobj2.set_price(200)
        Railobj2.set_morgage_val(100)

        GlobalPropDict['Short Line']= Railobj2

        Railobj3= RailRoadClass.RailRoad()
        Railobj3.set_name('B. & O. Railroad')
        Railobj3.set_color('Rail')
        Railobj3.set_price(200)
        Railobj3.set_morgage_val(100)

        GlobalPropDict['B. & O. Railroad']= Railobj3

        Railobj4= RailRoadClass.RailRoad()
        Railobj4.set_name('Pennsylvania Railroad')
        Railobj4.set_color('Rail')
        Railobj4.set_price(200)
        Railobj4.set_morgage_val(100)

        GlobalPropDict['Pennsylvania Railroad']= Railobj4



        Utilityobj1= UtilityClass.Utility()
        Utilityobj1.set_name('Water Works')
        Utilityobj1.set_color('Utility')
        Utilityobj1.set_price(150)
        Utilityobj1.set_morgage_val(75)

        GlobalPropDict['Water Works']= Utilityobj1

        Utilityobj2= UtilityClass.Utility()
        Utilityobj2.set_name('Electric Company')
        Utilityobj2.set_color('Utility')
        Utilityobj2.set_price(150)
        Utilityobj2.set_morgage_val(75)

        GlobalPropDict['Electric Company']= Utilityobj2



        Propobj1= PropertyClass.PropertyDeed()
        Propobj1.set_name('Mediterranean Avenue')
        Propobj1.set_color('Violet')
        Propobj1.set_price(60)
        Propobj1.set_rent(2)
        Propobj1.set_house1(10)
        Propobj1.set_house2(30)
        Propobj1.set_house3(90)
        Propobj1.set_house4(160)
        Propobj1.set_hotel(250)
        Propobj1.set_morgage_val(30)
        Propobj1.set_house_Cost(50)

        GlobalPropDict['Mediterranean Avenue']= Propobj1

        Propobj2= PropertyClass.PropertyDeed()
        Propobj2.set_name('Baltic Avenue')
        Propobj2.set_color('Violet')
        Propobj2.set_price(60)
        Propobj2.set_rent(4)
        Propobj2.set_house1(20)
        Propobj2.set_house2(60)
        Propobj2.set_house3(180)
        Propobj2.set_house4(320)
        Propobj2.set_hotel(450)
        Propobj2.set_morgage_val(30)
        Propobj2.set_house_Cost(50)

        GlobalPropDict['Baltic Avenue']= Propobj2

        Propobj3= PropertyClass.PropertyDeed()
        Propobj3.set_name('Oriental Avenue')
        Propobj3.set_color('Light Blue')
        Propobj3.set_price(100)
        Propobj3.set_rent(6)
        Propobj3.set_house1(30)
        Propobj3.set_house2(90)
        Propobj3.set_house3(270)
        Propobj3.set_house4(400)
        Propobj3.set_hotel(550)
        Propobj3.set_morgage_val(50)
        Propobj3.set_house_Cost(50)

        GlobalPropDict['Oriental Avenue']= Propobj3

        Propobj4= PropertyClass.PropertyDeed()
        Propobj4.set_name('Vermont Avenue')
        Propobj4.set_color('Light Blue')
        Propobj4.set_price(100)
        Propobj4.set_rent(6)
        Propobj4.set_house1(30)
        Propobj4.set_house2(90)
        Propobj4.set_house3(270)
        Propobj4.set_house4(400)
        Propobj4.set_hotel(550)
        Propobj4.set_morgage_val(50)
        Propobj4.set_house_Cost(50)

        GlobalPropDict['Vermont Avenue']= Propobj4

        Propobj5= PropertyClass.PropertyDeed()
        Propobj5.set_name('Connecticut Avenue')
        Propobj5.set_color('Light Blue')
        Propobj5.set_price(120)
        Propobj5.set_rent(8)
        Propobj5.set_house1(40)
        Propobj5.set_house2(100)
        Propobj5.set_house3(300)
        Propobj5.set_house4(450)
        Propobj5.set_hotel(600)
        Propobj5.set_morgage_val(60)
        Propobj5.set_house_Cost(50)

        GlobalPropDict['Connecticut Avenue']= Propobj5

        Propobj6= PropertyClass.PropertyDeed()
        Propobj6.set_name('St. Charles Place')
        Propobj6.set_color('Purple')
        Propobj6.set_price(140)
        Propobj6.set_rent(10)
        Propobj6.set_house1(50)
        Propobj6.set_house2(150)
        Propobj6.set_house3(450)
        Propobj6.set_house4(625)
        Propobj6.set_hotel(750)
        Propobj6.set_morgage_val(70)
        Propobj6.set_house_Cost(100)

        GlobalPropDict['St. Charles Place']= Propobj6

        Propobj7= PropertyClass.PropertyDeed()
        Propobj7.set_name('States Avenue')
        Propobj7.set_color('Purple')
        Propobj7.set_price(140)
        Propobj7.set_rent(10)
        Propobj7.set_house1(50)
        Propobj7.set_house2(150)
        Propobj7.set_house3(450)
        Propobj7.set_house4(625)
        Propobj7.set_hotel(750)
        Propobj7.set_morgage_val(70)
        Propobj7.set_house_Cost(100)

        GlobalPropDict['States Avenue']= Propobj7

        Propobj8= PropertyClass.PropertyDeed()
        Propobj8.set_name('Virginia Avenue')
        Propobj8.set_color('Purple')
        Propobj8.set_price(160)
        Propobj8.set_rent(12)
        Propobj8.set_house1(60)
        Propobj8.set_house2(180)
        Propobj8.set_house3(500)
        Propobj8.set_house4(700)
        Propobj8.set_hotel(900)
        Propobj8.set_morgage_val(80)
        Propobj8.set_house_Cost(100)

        GlobalPropDict['Virginia Avenue']= Propobj8

        Propobj9= PropertyClass.PropertyDeed()
        Propobj9.set_name('St. James Place')
        Propobj9.set_color('Orange')
        Propobj9.set_price(180)
        Propobj9.set_rent(14)
        Propobj9.set_house1(70)
        Propobj9.set_house2(200)
        Propobj9.set_house3(550)
        Propobj9.set_house4(750)
        Propobj9.set_hotel(950)
        Propobj9.set_morgage_val(90)
        Propobj9.set_house_Cost(100)

        GlobalPropDict['St. James Place']= Propobj9

        Propobj10= PropertyClass.PropertyDeed()
        Propobj10.set_name('Tennessee Avenue')
        Propobj10.set_color('Orange')
        Propobj10.set_price(180)
        Propobj10.set_rent(14)
        Propobj10.set_house1(70)
        Propobj10.set_house2(20)
        Propobj10.set_house3(550)
        Propobj10.set_house4(750)
        Propobj10.set_hotel(950)
        Propobj10.set_morgage_val(90)
        Propobj10.set_house_Cost(100)

        GlobalPropDict['Tennessee Avenue']= Propobj10

        Propobj11= PropertyClass.PropertyDeed()
        Propobj11.set_name('New York Avenue')
        Propobj11.set_color('Orange')
        Propobj11.set_price(200)
        Propobj11.set_rent(16)
        Propobj11.set_house1(80)
        Propobj11.set_house2(220)
        Propobj11.set_house3(600)
        Propobj11.set_house4(800)
        Propobj11.set_hotel(1000)
        Propobj11.set_morgage_val(100)
        Propobj11.set_house_Cost(100)

        GlobalPropDict['New York Avenue']= Propobj11

        Propobj12= PropertyClass.PropertyDeed()
        Propobj12.set_name('Kentucky Avenue')
        Propobj12.set_color('Red')
        Propobj12.set_price(220)
        Propobj12.set_rent(18)
        Propobj12.set_house1(90)
        Propobj12.set_house2(250)
        Propobj12.set_house3(700)
        Propobj12.set_house4(875)
        Propobj12.set_hotel(1050)
        Propobj12.set_morgage_val(110)
        Propobj12.set_house_Cost(150)

        GlobalPropDict['Kentucky Avenue']= Propobj12

        Propobj13= PropertyClass.PropertyDeed()
        Propobj13.set_name('Indiana Avenue')
        Propobj13.set_color('Red')
        Propobj13.set_price(220)
        Propobj13.set_rent(18)
        Propobj13.set_house1(90)
        Propobj13.set_house2(250)
        Propobj13.set_house3(700)
        Propobj13.set_house4(875)
        Propobj13.set_hotel(1050)
        Propobj13.set_morgage_val(110)
        Propobj13.set_house_Cost(150)

        GlobalPropDict['Indiana Avenue']= Propobj13

        Propobj14= PropertyClass.PropertyDeed()
        Propobj14.set_name('Illinois Avenue')
        Propobj14.set_color('Red')
        Propobj14.set_price(240)
        Propobj14.set_rent(20)
        Propobj14.set_house1(100)
        Propobj14.set_house2(300)
        Propobj14.set_house3(750)
        Propobj14.set_house4(925)
        Propobj14.set_hotel(1100)
        Propobj14.set_morgage_val(120)
        Propobj14.set_house_Cost(150)

        GlobalPropDict['Illinois Avenue']= Propobj14

        Propobj15= PropertyClass.PropertyDeed()
        Propobj15.set_name('Atlantic Avenue')
        Propobj15.set_color('Yellow')
        Propobj15.set_price(260)
        Propobj15.set_rent(22)
        Propobj15.set_house1(110)
        Propobj15.set_house2(330)
        Propobj15.set_house3(800)
        Propobj15.set_house4(975)
        Propobj15.set_hotel(1150)
        Propobj15.set_morgage_val(130)
        Propobj15.set_house_Cost(150)

        GlobalPropDict['Atlantic Avenue']= Propobj15

        Propobj16= PropertyClass.PropertyDeed()
        Propobj16.set_name('Ventor Avenue')
        Propobj16.set_color('Yellow')
        Propobj16.set_price(260)
        Propobj16.set_rent(22)
        Propobj16.set_house1(110)
        Propobj16.set_house2(330)
        Propobj16.set_house3(800)
        Propobj16.set_house4(975)
        Propobj16.set_hotel(1150)
        Propobj16.set_morgage_val(130)
        Propobj16.set_house_Cost(150)

        GlobalPropDict['Ventor Avenue']= Propobj16

        Propobj17= PropertyClass.PropertyDeed()
        Propobj17.set_name('Marvin Gardens')
        Propobj17.set_color('Yellow')
        Propobj17.set_price(280)
        Propobj17.set_rent(24)
        Propobj17.set_house1(120)
        Propobj17.set_house2(360)
        Propobj17.set_house3(850)
        Propobj17.set_house4(975)
        Propobj17.set_hotel(1025)
        Propobj17.set_morgage_val(140)
        Propobj17.set_house_Cost(150)

        GlobalPropDict['Marvin Gardens']= Propobj17

        Propobj18= PropertyClass.PropertyDeed()
        Propobj18.set_name('Pacific Avenue')
        Propobj18.set_color('Green')
        Propobj18.set_price(300)
        Propobj18.set_rent(26)
        Propobj18.set_house1(130)
        Propobj18.set_house2(390)
        Propobj18.set_house3(900)
        Propobj18.set_house4(1100)
        Propobj18.set_hotel(1275)
        Propobj18.set_morgage_val(150)
        Propobj18.set_house_Cost(200)

        GlobalPropDict['Pacific Avenue']= Propobj18

        Propobj19= PropertyClass.PropertyDeed()
        Propobj19.set_name('North Carolina Avenue')
        Propobj19.set_color('Green')
        Propobj19.set_price(300)
        Propobj19.set_rent(26)
        Propobj19.set_house1(130)
        Propobj19.set_house2(390)
        Propobj19.set_house3(900)
        Propobj19.set_house4(1100)
        Propobj19.set_hotel(1275)
        Propobj19.set_morgage_val(150)
        Propobj19.set_house_Cost(200)

        GlobalPropDict['North Carolina Avenue']= Propobj19

        Propobj20= PropertyClass.PropertyDeed()
        Propobj20.set_name('Pennsylvania Avenue')
        Propobj20.set_color('Green')
        Propobj20.set_price(320)
        Propobj20.set_rent(28)
        Propobj20.set_house1(150)
        Propobj20.set_house2(450)
        Propobj20.set_house3(1000)
        Propobj20.set_house4(1200)
        Propobj20.set_hotel(1400)
        Propobj20.set_morgage_val(160)
        Propobj20.set_house_Cost(200)

        GlobalPropDict['Pennsylvania Avenue']= Propobj20

        Propobj21= PropertyClass.PropertyDeed()
        Propobj21.set_name('Park Place')
        Propobj21.set_color('Dark Blue')
        Propobj21.set_price(350)
        Propobj21.set_rent(35)
        Propobj21.set_house1(175)
        Propobj21.set_house2(500)
        Propobj21.set_house3(1100)
        Propobj21.set_house4(1300)
        Propobj21.set_hotel(1500)
        Propobj21.set_morgage_val(175)
        Propobj21.set_house_Cost(200)

        GlobalPropDict['Park Place']= Propobj21

        Propobj22= PropertyClass.PropertyDeed()
        Propobj22.set_name('Boardwalk')
        Propobj22.set_color('Dark Blue')
        Propobj22.set_price(400)
        Propobj22.set_rent(50)
        Propobj22.set_house1(200)
        Propobj22.set_house2(600)
        Propobj22.set_house3(1400)
        Propobj22.set_house4(1700)
        Propobj22.set_hotel(2000)
        Propobj22.set_morgage_val(200)
        Propobj22.set_house_Cost(200)

        GlobalPropDict['Boardwalk']= Propobj22

        outFile= open("GlobalPropDict.txt", 'wb')
        pickle.dump(GlobalPropDict, outFile)
        outFile.close()

        print('Board Properties written to file.')
        
        # Return the dictionary of properties for game use
    return GlobalPropDict


def loadChanceCards(play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background):
        
    GlobalChanceCardsDict= {}
    
    x1= ChanceCardActions.Card1Action

    ChanceCardobj1= ChanceCardsClass.Chance_Cards(x1, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj1.set_card_number(1)
    ChanceCardobj1.set_message('Advance to St. Charles Place. If you pass GO, collect $200')
    

    GlobalChanceCardsDict[1]= ChanceCardobj1

    x2= ChanceCardActions.Card2Action
    ChanceCardobj2= ChanceCardsClass.Chance_Cards(x2, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj2.set_card_number(2)
    ChanceCardobj2.set_message('Advance to GO, collect $200')

    GlobalChanceCardsDict[2]= ChanceCardobj2

    x3= ChanceCardActions.Card3Action
    ChanceCardobj3= ChanceCardsClass.Chance_Cards(x3, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj3.set_card_number(3)
    ChanceCardobj3.set_message('Go directly to JAIL. Do not collect $200')

    GlobalChanceCardsDict[3]= ChanceCardobj3

    x4= ChanceCardActions.Card4Action
    ChanceCardobj4= ChanceCardsClass.Chance_Cards(x4, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj4.set_card_number(4)
    ChanceCardobj4.set_message('Bank pays you a Dividend of $50')

    GlobalChanceCardsDict[4]= ChanceCardobj4

    x5= ChanceCardActions.Card5Action
    ChanceCardobj5= ChanceCardsClass.Chance_Cards(x5, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj5.set_card_number(5)
    ChanceCardobj5.set_message('Advance token to BOARDWALK!')

    GlobalChanceCardsDict[5]= ChanceCardobj5

    x6= ChanceCardActions.Card6Action
    ChanceCardobj6= ChanceCardsClass.Chance_Cards(x6, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj6.set_card_number(6)
    ChanceCardobj6.set_message('Advance token to Illinois Ave.')

    GlobalChanceCardsDict[6]= ChanceCardobj6
    
    x7= ChanceCardActions.Card7Action
    ChanceCardobj7= ChanceCardsClass.Chance_Cards(x7, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj7.set_card_number(7)
    ChanceCardobj7.set_message('Your building and loan matures. Collect $150')

    GlobalChanceCardsDict[7]= ChanceCardobj7

    x8= ChanceCardActions.Card8Action
    ChanceCardobj8= ChanceCardsClass.Chance_Cards(x8, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj8.set_card_number(8)
    ChanceCardobj8.set_message('Go back three spaces')

    GlobalChanceCardsDict[8]= ChanceCardobj8

    x9= ChanceCardActions.Card9Action
    ChanceCardobj9= ChanceCardsClass.Chance_Cards(x9, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj9.set_card_number(9)
    ChanceCardobj9.set_message('Get out of Jail FREE! This card may be kept or sold')

    GlobalChanceCardsDict[9]= ChanceCardobj9

    x10= ChanceCardActions.Card10Action
    ChanceCardobj10= ChanceCardsClass.Chance_Cards(x10, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj10.set_card_number(10)
    ChanceCardobj10.set_message('Pay POOR tax of $15')

    GlobalChanceCardsDict[10]= ChanceCardobj10

    x11= ChanceCardActions.Card11Action
    ChanceCardobj11= ChanceCardsClass.Chance_Cards(x11, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj11.set_card_number(11)
    ChanceCardobj11.set_message('Make general repairs on ALL of your property. $25 for EACH house, $100 for EACH hotel')

    GlobalChanceCardsDict[11]= ChanceCardobj11

    x12= ChanceCardActions.Card12Action
    ChanceCardobj12= ChanceCardsClass.Chance_Cards(x12, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj12.set_card_number(12)
    ChanceCardobj12.set_message('Take a ride on the Reading. If you pass GO, collect $200')

    GlobalChanceCardsDict[12]= ChanceCardobj12

    x13= ChanceCardActions.Card13Action
    ChanceCardobj13= ChanceCardsClass.Chance_Cards(x13, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj13.set_card_number(13)
    ChanceCardobj13.set_message('Advance to the nearest Railroad and pay double the rent')

    GlobalChanceCardsDict[13]= ChanceCardobj13

    x14= ChanceCardActions.Card14Action
    ChanceCardobj14= ChanceCardsClass.Chance_Cards(x14, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj14.set_card_number(14)
    ChanceCardobj14.set_message('Advance to the nearest Utility, roll dice and pay 10x the value of the roll')

    GlobalChanceCardsDict[14]= ChanceCardobj14

    x15= ChanceCardActions.Card15Action
    ChanceCardobj15= ChanceCardsClass.Chance_Cards(x15, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj15.set_card_number(15)
    ChanceCardobj15.set_message('Advance to the nearest Railroad and pay double the rent')

    GlobalChanceCardsDict[15]= ChanceCardobj15

    x16= ChanceCardActions.Card16Action
    ChanceCardobj16= ChanceCardsClass.Chance_Cards(x16, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    ChanceCardobj16.set_card_number(16)
    ChanceCardobj16.set_message('You have been elected Chairman of the board, Pay EACH player $50')

    GlobalChanceCardsDict[16]= ChanceCardobj16
    
    return GlobalChanceCardsDict


def loadCommunityCards(play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background):

    GlobalCommunityDict= {}

    x1= CommunityCardActions.Card1Action
    CommunityCardobj1= CommunityChestClass.Comminity_Chest(x1, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj1.set_card_number(1)
    CommunityCardobj1.set_message('You are assessed for street repairs. $40 per HOUSE, $115 per HOTEL')
    
    GlobalCommunityDict[1]= CommunityCardobj1

    x2= CommunityCardActions.Card2Action
    CommunityCardobj2= CommunityChestClass.Comminity_Chest(x2, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj2.set_card_number(2)
    CommunityCardobj2.set_message('Grand Opera Opening! Collect $50 from each player')
    
    GlobalCommunityDict[2]= CommunityCardobj2

    x3= CommunityCardActions.Card3Action
    CommunityCardobj3= CommunityChestClass.Comminity_Chest(x3, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj3.set_card_number(3)
    CommunityCardobj3.set_message('Life Insurance matures, collect $100')
    
    GlobalCommunityDict[3]= CommunityCardobj3

    x4= CommunityCardActions.Card4Action
    CommunityCardobj4= CommunityChestClass.Comminity_Chest(x4, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj4.set_card_number(4)
    CommunityCardobj4.set_message('Advance to GO, collect $200')
    
    GlobalCommunityDict[4]= CommunityCardobj4

    x5= CommunityCardActions.Card5Action
    CommunityCardobj5= CommunityChestClass.Comminity_Chest(x5, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj5.set_card_number(5)
    CommunityCardobj5.set_message('You have won second Prize in a Beauty contest, collect $10')
    
    GlobalCommunityDict[5]= CommunityCardobj5

    x6= CommunityCardActions.Card6Action
    CommunityCardobj6= CommunityChestClass.Comminity_Chest(x6, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj6.set_card_number(6)
    CommunityCardobj6.set_message('Pay hospital $100')
    
    GlobalCommunityDict[6]= CommunityCardobj6

    x7= CommunityCardActions.Card7Action
    CommunityCardobj7= CommunityChestClass.Comminity_Chest(x7, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj7.set_card_number(7)
    CommunityCardobj7.set_message('Bank error in YOUR favor, collect $200')
    
    GlobalCommunityDict[7]= CommunityCardobj7

    x8= CommunityCardActions.Card8Action
    CommunityCardobj8= CommunityChestClass.Comminity_Chest(x8, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj8.set_card_number(8)
    CommunityCardobj8.set_message('GO TO JAIL')
    
    GlobalCommunityDict[8]= CommunityCardobj8

    x9= CommunityCardActions.Card9Action
    CommunityCardobj9= CommunityChestClass.Comminity_Chest(x9, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj9.set_card_number(9)
    CommunityCardobj9.set_message('Get out of JAIL free card. This card may be kept or sold')
    
    GlobalCommunityDict[9]= CommunityCardobj9

    x10= CommunityCardActions.Card10Action
    CommunityCardobj10= CommunityChestClass.Comminity_Chest(x10, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj10.set_card_number(10)
    CommunityCardobj10.set_message("Doctor's fee. Pay $50")
    
    GlobalCommunityDict[10]= CommunityCardobj10

    x11= CommunityCardActions.Card11Action
    CommunityCardobj11= CommunityChestClass.Comminity_Chest(x11, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj11.set_card_number(11)
    CommunityCardobj11.set_message('From sale of Stock you get $45')
    
    GlobalCommunityDict[11]= CommunityCardobj11

    x12= CommunityCardActions.Card12Action
    CommunityCardobj12= CommunityChestClass.Comminity_Chest(x12, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj12.set_card_number(12)
    CommunityCardobj12.set_message('Xmas fund matures, collect $100')
    
    GlobalCommunityDict[12]= CommunityCardobj12

    x13= CommunityCardActions.Card13Action
    CommunityCardobj13= CommunityChestClass.Comminity_Chest(x13, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj13.set_card_number(13)
    CommunityCardobj13.set_message('Income tax refund, collect $20')
    
    GlobalCommunityDict[13]= CommunityCardobj13

    x14= CommunityCardActions.Card14Action
    CommunityCardobj14= CommunityChestClass.Comminity_Chest(x14, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj14.set_card_number(14)
    CommunityCardobj14.set_message('Pay school tax of $150')
    
    GlobalCommunityDict[14]= CommunityCardobj14

    x15= CommunityCardActions.Card15Action
    CommunityCardobj15= CommunityChestClass.Comminity_Chest(x15, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj15.set_card_number(15)
    CommunityCardobj15.set_message('Receive for Services $25')
    
    GlobalCommunityDict[15]= CommunityCardobj15

    x16= CommunityCardActions.Card16Action
    CommunityCardobj16= CommunityChestClass.Comminity_Chest(x16, play, Danny, Jane, screen, hattoken, cartoken, cattoken, BoardxPoints, BoardyPoints, background)
    CommunityCardobj16.set_card_number(16)
    CommunityCardobj16.set_message('You inherit $100')
    
    GlobalCommunityDict[16]= CommunityCardobj16

    return GlobalCommunityDict
