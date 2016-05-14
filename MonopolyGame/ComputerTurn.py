import CompAIClass
import HelperFunctions
import random
from time import sleep

def startDanTurn(GlobalPropDict, Property_LocationDict, play, Danny, Jane, screen,
              cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background,
              update, danjailTimeCount, turn, DanrollAgain, GlobalCommunityDict, GlobalChanceCardsDict):
    
    if Danny.get_jail_Bird() == True:
        if danjailTimeCount < 2:
            print("\n-- Danny's turn in jail------")
            compController= CompAIClass.ComputerAI(GlobalPropDict, Danny, Property_LocationDict)
            # Roll the dice
            DanrollAgain= compController.RollDice()
            if DanrollAgain == True or Danny.get_Out_of_Jail_Card() == True:
                if Danny.get_Out_of_Jail_Card() == True:
                    Danny.set_Out_of_Jail_Card(False)
                    
                Danny.set_jail_Bird(False)
                Danny.setLocation(compController.getDiceValue())

                index = Danny.getLocation()
                # Determine rent --------
                key= Property_LocationDict[index]
                if key == 'Chance' or key == 'Community Chest':
                    if key == 'Chance':
                        cardNum= random.randint(1, 16)
                        print('Drawing Chance Card')
                        play, Danny, Jane= GlobalChanceCardsDict[cardNum].do_action('Danny', play, Danny, Jane)
                        ## Add special condition for income taxes
                    elif key == 'Community Chest':
                        cardNum= random.randint(1, 16)
                        print('Drawing Community Chest Card')
                        play, Danny, Jane= GlobalCommunityDict[cardNum].do_action('Danny', play, Danny, Jane)
                elif key == 'GO' or key == 'Income Tax':
                    if key == 'Income Tax':
                        ten= Danny.get_money() * .1
                        if ten > 200:
                            print('Taking income tax of $200.')
                            Danny.set_money(Danny.get_money() - 200)
                        else:
                            print('Taking ten percent of', Danny.get_money())
                            Danny.set_money(Danny.get_money() - int(ten))
                elif key == 'Just Visiting' or key == 'Free Parking':
                    if key == 'Just Visiting':
                        print(Danny.get_name(), 'visting Aunt May.')
                    if key == 'Free Parking':
                        print(Danny.get_name(), 'is parking in handicap with no cops around.')
                elif key == 'Go To Jail' or key == 'Luxury Tax':
                    if key == 'Go To Jail':
                        print('Contact police department, you should already be in jail.')
                    if key == 'Luxury Tax':
                        print("$75 to get Dann'y gold watch out from pawn.")
                        Danny.set_money(Danny.get_money() - 75)
                else:
                    obj= GlobalPropDict[key]
                    if obj.get_owner() != 'Free':
                        if obj.get_owner() == play.get_name():
                            play.set_money(play.get_money() + obj.get_rent())
                            Danny.set_money(Danny.get_money() - obj.get_rent())
                            print(obj.get_rent(), 'deducted from Danny account to,', play.get_name())
                        elif obj.get_owner() == 'Jane':
                            Jane.set_money(Jane.get_money() + obj.get_rent())
                            Danny.set_money(Danny.get_money() - obj.get_rent())
                            print(obj.get_rent(), 'deducted from Danny account to Jane.')
                            
                HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)

                compController.BuyProp()
                compController.ViewProp()
                danjailTimeCount= 0
            else:
                print('Still in jail.')
                danjailTimeCount += 1
                turn = 'Jane'
        else:
            Danny.set_jail_Bird(False)
            danjailTimeCount = 0
            print('Out of jail')
            turn= 'Danny'
            DanrollAgain= True

    else:
        danjailTimeCount = 0
        #turn= 'Jane'
        
    while turn == 'Danny' and DanrollAgain == True:
        print("\n-- Danny's turn ------")
        compController= CompAIClass.ComputerAI(GlobalPropDict, Danny, Property_LocationDict)
        # Roll the dice
        DanrollAgain= compController.RollDice()
        Danny.setLocation(compController.getDiceValue())
        # Move --------------------------------------------
        HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)
        sleep(2)
        index = Danny.getLocation()

        if index == 30:
            # move the peice to the just Visiting spot
            Danny.set_jail_Bird(True)
            index= 10
            Danny.specifyLocation(index)
            ##HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, pygame.display.update)
            print('Danny is in jail')
            turn = 'Jane'
            JanrollAgain= True
        else:
            # Determine rent --------
            key= Property_LocationDict[index]
            if key == 'Chance' or key == 'Community Chest':
                if key == 'Chance':
                    cardNum= random.randint(1, 16)
                    print('Drawing Chance Card')
                    play, Danny, Jane= GlobalChanceCardsDict[cardNum].do_action('Danny', play, Danny, Jane)
                elif key == 'Community Chest':
                    cardNum= random.randint(1, 16)
                    print('Drawing Community Chest Card')
                    play, Danny, Jane= GlobalCommunityDict[cardNum].do_action('Danny', play, Danny, Jane)
            elif key == 'GO' or key == 'Income Tax':
                if key == 'Income Tax':
                    ten= Danny.get_money() * .1
                    if ten > 200:
                        print('Taking income tax of $200.')
                        Danny.set_money(Danny.get_money() - 200)
                    else:
                        print('Taking ten percent of', Danny.get_money())
                        Danny.set_money(Danny.get_money() - int(ten))
            elif key == 'Just Visiting' or key == 'Free Parking':
                if key == 'Just Visiting':
                    print(Danny.get_name(), 'visting Aunt May.')
                if key == 'Free Parking':
                    print(Danny.get_name(), 'is parking in handicap with no cops around.')
            elif key == 'Go To Jail' or key == 'Luxury Tax':
                if key == 'Go To Jail':
                    print('Contact police department, you should already be in jail.')
                if key == 'Luxury Tax':
                    print("$75 to get Danny's gold watch out from pawn.")
                    Danny.set_money(Danny.get_money() - 75)
            else:
                obj= GlobalPropDict[key]
                if obj.get_owner() != 'Free':
                    if obj.get_owner() == play.get_name():
                        play.set_money(play.get_money() + obj.get_rent())
                        Danny.set_money(Danny.get_money() - obj.get_rent())
                        print(obj.get_rent(), "deducted from Danny's account to,", play.get_name())
                    elif obj.get_owner() == 'Jane':
                        Jane.set_money(Jane.get_money() + obj.get_rent())
                        Danny.set_money(Danny.get_money() - obj.get_rent())
                        print(obj.get_rent(), "deducted from Danny's account to Jane.")
                        
            HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)
            
            # Move --------------------------------------------

            if Danny.get_jail_Bird() == True:
                DanrollAgain == False
            else:       
                compController.BuyProp()
                compController.ViewProp()

        if DanrollAgain == False:
            turn = 'Jane'
            DanrollAgain= True

    return play, Danny, Jane, GlobalPropDict, turn, danjailTimeCount, DanrollAgain


def startJanTurn(GlobalPropDict, Property_LocationDict, play, Danny, Jane, screen,
              cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background,
              update, janjailTimeCount, turn, JanrollAgain, GlobalCommunityDict, GlobalChanceCardsDict):
    
    if Jane.get_jail_Bird() == True:
        if janjailTimeCount < 2:
            print("\n-- Jane's turn in jail------")
            compController= CompAIClass.ComputerAI(GlobalPropDict, Jane, Property_LocationDict)
            # Roll the dice
            JanrollAgain= compController.RollDice()
            if JanrollAgain == True or Jane.get_Out_of_Jail_Card() == True:
                if Jane.get_Out_of_Jail_Card() == True:
                    Jane.set_Out_of_Jail_Card(False)
                    
                Jane.set_jail_Bird(False)
                Jane.setLocation(compController.getDiceValue())

                index = Jane.getLocation()
                # Determine rent --------
                key= Property_LocationDict[index]
                if key == 'Chance' or key == 'Community Chest':
                    if key == 'Chance':
                        cardNum= random.randint(1, 16)
                        print('Drawing Chance Card')
                        play, Danny, Jane= GlobalChanceCardsDict[cardNum].do_action('Jane', play, Danny, Jane)
                        ## Add special condition for income taxes
                    elif key == 'Community Chest':
                        cardNum= random.randint(1, 16)
                        print('Drawing Community Chest Card')
                        play, Danny, Jane= GlobalCommunityDict[cardNum].do_action('Jane', play, Danny, Jane)
                elif key == 'GO' or key == 'Income Tax':
                    if key == 'Income Tax':
                        ten= Jane.get_money() * .1
                        if ten > 200:
                            print('Taking income tax of $200.')
                            Jane.set_money(Jane.get_money() - 200)
                        else:
                            print('Taking ten percent of', Jane.get_money())
                            Jane.set_money(Jane.get_money() - int(ten))
                elif key == 'Just Visiting' or key == 'Free Parking':
                    if key == 'Just Visiting':
                        print(Jane.get_name(), 'visting the Pretty Bunny.')
                    if key == 'Free Parking':
                        print(Jane.get_name(), 'is parking in a loading zone with no cops around.')
                elif key == 'Go To Jail' or key == 'Luxury Tax':
                    if key == 'Go To Jail':
                        print('Contact police department, you should already be in jail.')
                    if key == 'Luxury Tax':
                        print("$75 to buy a new hat.")
                        Jane.set_money(Jane.get_money() - 75)
                else:
                    obj= GlobalPropDict[key]
                    if obj.get_owner() != 'Free':
                        if obj.get_owner() == play.get_name():
                            play.set_money(play.get_money() + obj.get_rent())
                            Danny.set_money(Danny.get_money() - obj.get_rent())
                            print(obj.get_rent(), "deducted from Jane's account to,", play.get_name())
                        elif obj.get_owner() == 'Danny':
                            Danny.set_money(Danny.get_money() + obj.get_rent())
                            Jane.set_money(Jane.get_money() - obj.get_rent())
                            print(obj.get_rent(), 'deducted from Danny account to Jane.')
                            
                HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)

                compController.BuyProp()
                compController.ViewProp()
                janjailTimeCount= 0
            else:
                print('Still in jail.')
                janjailTimeCount += 1
                turn = 'PlayerTurn'
        else:
            Jane.set_jail_Bird(False)
            janjailTimeCount = 0
            print('Out of jail')
            turn= 'PlayerTurn'
            JanrollAgain= True

    else:
        janjailTimeCount = 0
        #turn= 'Jane'
        
    while turn == 'Jane' and JanrollAgain == True:
        print("\n-- Jane's turn ------")
        compController= CompAIClass.ComputerAI(GlobalPropDict, Jane, Property_LocationDict)
        # Roll the dice
        JanrollAgain= compController.RollDice()
        Jane.setLocation(compController.getDiceValue())
        # Move --------------------------------------------
        HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)
        sleep(2)
        index = Jane.getLocation()

        if index == 30:
            # move the peice to the just Visiting spot
            Jane.set_jail_Bird(True)
            index= 10
            Jane.specifyLocation(index)
            ##HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, pygame.display.update)
            print('Jane is in jail')
            turn = 'PlayerTurn'
            JanrollAgain= True
        else:
            # Determine rent --------
            key= Property_LocationDict[index]
            if key == 'Chance' or key == 'Community Chest':
                if key == 'Chance':
                    cardNum= random.randint(1, 16)
                    print('Drawing Chance Card')
                    play, Danny, Jane= GlobalChanceCardsDict[cardNum].do_action('Jane', play, Danny, Jane)
                elif key == 'Community Chest':
                    cardNum= random.randint(1, 16)
                    print('Drawing Community Chest Card')
                    play, Danny, Jane= GlobalCommunityDict[cardNum].do_action('Jane', play, Danny, Jane)
            elif key == 'GO' or key == 'Income Tax':
                if key == 'Income Tax':
                    ten= Jane.get_money() * .1
                    if ten > 200:
                        print('Taking income tax of $200.')
                        Jane.set_money(Jane.get_money() - 200)
                    else:
                        print('Taking ten percent of', Jane.get_money())
                        Jane.set_money(Jane.get_money() - int(ten))
            elif key == 'Just Visiting' or key == 'Free Parking':
                if key == 'Just Visiting':
                    print(Jane.get_name(), 'visting Aunt May.')
                if key == 'Free Parking':
                    print(Jane.get_name(), 'is parking in handicap with no cops around.')
            elif key == 'Go To Jail' or key == 'Luxury Tax':
                if key == 'Go To Jail':
                    print('Contact police department, you should already be in jail.')
                if key == 'Luxury Tax':
                    print("$75 to buy a new hat.")
                    Jane.set_money(Jane.get_money() - 75)
            else:
                obj= GlobalPropDict[key]
                if obj.get_owner() != 'Free':
                    if obj.get_owner() == play.get_name():
                        play.set_money(play.get_money() + obj.get_rent())
                        Jane.set_money(Jane.get_money() - obj.get_rent())
                        print(obj.get_rent(), "deducted from Jane's account to,", play.get_name())
                    elif obj.get_owner() == 'Danny':
                        Danny.set_money(Danny.get_money() + obj.get_rent())
                        Jane.set_money(Jane.get_money() - obj.get_rent())
                        print(obj.get_rent(), 'deducted from Jane account to Danny.')
                        
            HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)
            
            # Move --------------------------------------------

            if Jane.get_jail_Bird() == True:
                JanrollAgain == False
            else:       
                compController.BuyProp()
                compController.ViewProp()

        if JanrollAgain == False:
            turn = 'PlayerTurn'
            JanrollAgain= True

    return play, Danny, Jane, GlobalPropDict, turn, janjailTimeCount, JanrollAgain

