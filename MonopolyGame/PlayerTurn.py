import HelperFunctions
import OptionsClass
import random

def startTurn(playerdidRoll, GlobalPropDict, Property_LocationDict, play, Danny, Jane, screen,
              cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background,
              update, backMusic, playjailTimeCount, GlobalCommunityDict, GlobalChanceCardsDict):
# move the part where the rent and cards are pluck to options class so it can be called by the rolling thing to stop double draw    
    # Create instance of Player options, including roll, sell proptery
    op= OptionsClass.Options(playerdidRoll, GlobalPropDict, play, Property_LocationDict, Danny, Jane)
    if play.get_jail_Bird() == True:
        # If player is in jail, call jail gui
        op.JailGUI(playjailTimeCount)
        # Increment the counter
        playjailTimeCount += 1
        # Allow comp Danny to take turn
        op.Isturn = False
        # Player did roll dice
        playerdidRoll = False

        # If rolled double, used 'Get out of jail' card, pay fine or served time, release player from jail
        if play.get_jail_Bird() == False:
            op.Isturn= False
            play.setLocation(op.getDiceValue())
            index = play.getLocation()
            HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)
            playerdidRoll = True
            playjailTimeCount= 0
            
    if play.get_jail_Bird() == False:
        op.OptionsGUI()
        # Return player and comp objs
        play= op.getPlayer()
        Danny= op.getDanny()
        Jane= op.getJane()
        
        if op.endGame == True:
            HelperFunctions.EndGame(play, Danny, Jane, backMusic)
        play.setLocation(op.getDiceValue())
        
        index = play.getLocation()

        # Check to see if the player landed on Go to Jail
        if index == 30:
            # move the peice to the just Visiting spot
            play.set_jail_Bird(True)
            index= 10
            play.specifyLocation(index)
            HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)
        else:
            # Determine rent --------
            key= Property_LocationDict[index]
            if key == 'Chance' or key == 'Community Chest':
                if key == 'Chance':
                    cardNum= random.randint(1, 16)
                    print('Drawing Chance Card')
                    play, Danny, Jane= GlobalChanceCardsDict[cardNum].do_action(play.get_name(), play, Danny, Jane)
                elif key == 'Community Chest':
                    cardNum= random.randint(1, 16)
                    print('Drawing Community Chest Card')
                    play, Danny, Jane= GlobalCommunityDict[cardNum].do_action(play.get_name(), play, Danny, Jane)
            elif key == 'GO' or key == 'Income Tax':
                if key == 'Income Tax':
                    ten= play.get_money() * .1
                    if ten > 200:
                        print('Taking income tax of $200.')
                        play.set_money(play.get_money() - 200)
                    else:
                        print('Taking ten percent of', play.get_money())
                        play.set_money(play.get_money() - int(ten))
            elif key == 'Just Visiting' or key == 'Free Parking':
                if key == 'Just Visiting':
                    print(play.get_name(), 'visting Uncle Krazy.')
                if key == 'Free Parking':
                    print(play.get_name(), 'stole the parking spot from the old lady.')
            elif key == 'Go To Jail' or key == 'Luxury Tax':
                if key == 'Go To Jail':
                    print('Contact police department, you should already be in jail.')
                if key == 'Luxury Tax':
                    print("$75 for your mistress' down payment for a ring.")
                    play.set_money(play.get_money() - 75)
                    
            else:
                obj= GlobalPropDict[key]
                if obj.get_owner() != 'Free':
                    if obj.get_owner() == 'Danny':
                        Danny.set_money(Danny.get_money() + obj.get_rent())
                        play.set_money(play.get_money() - obj.get_rent())
                        print(obj.get_rent(), 'deducted from your account to Danny.')
                    elif obj.get_owner() == 'Jane':
                        Jane.set_money(Jane.get_money() + obj.get_rent())
                        play.set_money(play.get_money() - obj.get_rent())
                        print(obj.get_rent(), 'deducted from your account to Jane.')

        # Depending on the card number, the main blit or the chance card blit will do it
            HelperFunctions.ScreenBlit(play, Danny, Jane, screen, cattoken, cartoken, hattoken, BoardxPoints, BoardyPoints, background, update)
            
        if op.getdidRoll() == True:
            playerdidRoll = True

        if op.Isturn == False:
            #######turn = op.turn
            ####DanrollAgain= True
            playerdidRoll = False

    return play, Danny, Jane, GlobalPropDict, op.Isturn, playerdidRoll, playjailTimeCount###, DanrollAgain
