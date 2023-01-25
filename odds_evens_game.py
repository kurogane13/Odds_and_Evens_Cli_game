import random
import datetime
import time
from datetime import datetime


def randoms_game():
    global loop, odds, evens, randomnumber, count_set, seconds
    odds = []
    evens = []

    loop = 1
    while True:

        now = datetime.now()
        actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
        print("TODAY IS: ")
        print(" ")
        print(actualdatetime)
        print("##########################################################")
        print("WELCOME TO ODDS AND EVEN NUMBERS GAME!.")
        print("A PLAYER WILL GET THE ODD NUMBERS, AND THE OTHER THE EVENS")
        print("-------------------------------------------------------")
        print("THE COMPUTER WILL AUTOMATICALLY ASSIGN A NUMBER RANDOMLY(ODD OR EVEN)")
        print("IF IT SELECTS AN ODD NUMBER A POINT WILL BE SCORED FOR THE ODD PLAYER")
        print("ON THE CONTRARY, THE EVEN PLAYER WILL GET A POINT.")
        print("****************************************************************")
        print(" ")
        print("NOTE: THE PROGRAM RECORDS A LOG OF EACH PLAY, WITH DATE AND TIME")
        print("YOU CAN FIND THE LOG IN THE CURRENT PATH.")
        print("THE LOGFILE NAME IS odds_and_evens.log")
        print(" ")
        print("****************************************************************")
        print("################################################################")
        print("----------------------------------------------------------------")
        print("- YOU WILL HAVE TO SET UP THE AMOUNT OF POINTS REACHED TO WIN")
        print("- THE MAXIMUM VALUE, BETWEEN 0 AND THE LATTER.")
        print("----------------------------------------------------------------")
        input("Press enter to access the program settings now...")
        print("----------------------------------------------------------------")
        print("GAME MODES MENU")
        print(" ")
        print("0 - Computer automatic mode. The computer plays both players.")
        print("1 - Manual Mode. You can play by yourself, or with a partner ")
        print("2 - Fast mode. The computer plays against itself, at full speed")
        print("")
        print("----------------------------------------------------------------")
        loop = 5
        while (loop==5):

            gamemode = input("Please select a number from the menu and press enter...")
            
            if gamemode == '0':
                print(" ")
                print("----------------------------------------")
                print("MODE 0 accessed. ")
                print(" ")
                print("Computer automatic mode selected.")
                print("----------------------------------------")

                loop = 6
                while (loop==6):

                    seconds = input("Enter the amount of seconds interval, the computer will wait, until it selects a random number...")
                    if not seconds.isdigit():
                        print("------------------------------------------")
                        print("Only numbers are allowed here!")
                        print("------------------------------------------")
                        loop = 6

                    else:
                        print("------------------------------------------")
                        print("Seconds interval was set to: "+str(seconds))
                        print("------------------------------------------")

                        loop = 2
                        while (loop==2):
                            count_set = input("Set Top count points. The player who reaches this amount of points wins...")
                            if not count_set.isdigit():
                                print("------------------------------------------")
                                print("Only numbers are allowed here!")
                                print("------------------------------------------")
                                loop = 2
                            else:
                                print("-------------------------------------------------------")
                                print("Top count points was set to: "+count_set)
                                count_set = int(count_set)
                                loop = 3
                                while (loop==3):
                                    print("-------------------------------------------------------")
                                    maxnumber = input("Set a Maximum number. The computer will randomly select numbers between 0, and this number...")
                                    if not maxnumber.isdigit():
                                        print("------------------------------------------")
                                        print("Only numbers are allowed here!")
                                        loop = 3
                                    else:
                                        print("------------------------------------------")
                                        print("Maximum Number was set to: "+maxnumber)
                                        print("------------------------------------------")
                                        input("Ok!, press enter to start the game now...")
                                        now = datetime.now()
                                        actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                        print("Game started date and time: ")
                                        print(actualdatetime)
                                        with open('odds_and_evens.log', 'a') as logfile:
                                                now = datetime.now()
                                                startdatetime = datetime.now()
                                                
                                                logfile.write("########################################"+'\n')
                                                logfile.write("NEW GAME STARTED"+'\n')
                                                logfile.write("------------------------------------"+'\n')
                                                logfile.write("DATE AND TIME OF STARTED GAME "+'\n')
                                                logfile.write(str(startdatetime)+'\n')
                                                logfile.write("########################################"+'\n')
                                                logfile.close()

                                        
                                        loop = 4
                                        while (loop==4):
                                            
                                            randomnumber = random.randint(0, int(maxnumber))
                                            print("-------------------------------------------------------")

                                            if (randomnumber % 2) == 0:
                                                print("Number "+str(randomnumber)+" is even")
                                                print("-------------------------------------------------------")
                                                evens.append(randomnumber)
                                                evenspoints = (len(evens))
                                                print("Appended number "+str(randomnumber)+" to the evens numbers list")
                                                print("-------------------------------------------------------")
                                                print("Showing Even numbers list: ")
                                                print(evens)
                                                print("-------------------------------------------------------")
                                                print("Amount of points for EVEN numbers player is: ")
                                                print(evenspoints)

                                                with open('odds_and_evens.log', 'a') as logfile:
                                                    lines = "-------------------------------------------------------"
                                                    logfile.write(lines+'\n')
                                                    logfile.write("HIT FOR EVENS PLAYER AT: ")
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    logfile.write(actualdatetime+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Number "+str(randomnumber)+" is even"+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Appended number "+str(randomnumber)+" to the evens numbers list"+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Showing Even numbers list: "+'\n')
                                                    logfile.write(str(evens)+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Amount of points for EVEN numbers player is: "+'\n')
                                                    logfile.write(str(evenspoints)+'\n')
                                                    logfile.close()
                                                
                                                if evenspoints == count_set:
                                                    with open('odds_and_evens.log', 'a') as logfile:
                                                        
                                                        logfile.write(lines+'\n')
                                                        logfile.write("EVEN PLAYER YOU WIN!!, YOU REACHED THE AMOUNT OF POINTS OF: "+'\n')
                                                        logfile.write(str(evenspoints)+'\n')
                                                        logfile.write(lines+'\n')
                                                        logfile.write("Both Lists were reset, and no numbers are contained in them."+'\n')
                                                        hashtag = ("##########################################################")
                                                        logfile.write(hashtag+'\n')
                                                        logfile.write("DATE AND TIME OF FINISHED GAME IS: "+'\n')
                                                        now = datetime.now()
                                                        actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                        logfile.write(" "+'\n')
                                                        logfile.write(actualdatetime+'\n')
                                                        logfile.write(hashtag+'\n')
                                                        now = datetime.now()
                                                        finishtime = datetime.now()
                                                        deltatime = finishtime-startdatetime
                                                        logfile.write(" "+'\n')
                                                        logfile.write("DURATION OF THE PROGRAM WAS: "+'\n')
                                                        logfile.write(" "+'\n')
                                                        logfile.write("hh:mm:ss:microseconds"+'\n')
                                                        logfile.write(str(deltatime)+'\n')
                                                        logfile.write(" "+'\n')
                                                        logfile.write(hashtag+'\n')
                                                        logfile.close()
                                                    print("-------------------------------------------------------")
                                                    print("COMPUTER EVENS PLAYER WINS!!, THE PLAYER REACHED THE AMOUNT OF POINTS OF:")
                                                    print(evenspoints)
                                                    odds = []
                                                    evens = []
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    print(hashtag)
                                                    print(" ")
                                                    print("GAME FINISHED DATE AND TIME: ")
                                                    print(" ")
                                                    print(actualdatetime)
                                                    print(" ")
                                                    print(hashtag)
                                                    print(" ")
                                                    print("DURATION OF THE PROGRAM WAS: ")
                                                    print(" ")
                                                    print("hh:mm:ss:microseconds")
                                                    print(deltatime)
                                                    print(" ")
                                                    print(hashtag)
                                                    print("Both Lists were reset, and no numbers are contained in them.")
                                                    print("-------------------------------------------------------")
                                                    input("PRESS ENTER TO PLAY AGAIN...")

                                                    randoms_game()
                                                else:
                                                    with open('odds_and_evens.log', 'a') as logfile:
                                                        evenspoints = (len(evens))
                                                        oddpoints = (len(odds))
                                                        logfile.write(lines+'\n')
                                                        logfile.write("SCORES AT:"+'\n')
                                                        now = datetime.now()
                                                        actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                        logfile.write(actualdatetime+'\n')
                                                        logfile.write(lines+'\n')
                                                        logfile.write("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints)+'\n')
                                                        logfile.write(lines+'\n')
                                                        logfile.close()
                                                    print(" ")
                                                    print("SCORES AT:")
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    print(actualdatetime)
                                                    
                                                    print(" ")
                                                    print("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints))
                                                    if oddpoints > evenspoints:
                                                        print(" ")
                                                        print("ODDS IS WINNING - EVENS IS LOSING")
                                                        seconds = int(seconds)
                                                        for remaining_seconds in range(seconds,0,-1):
                                                            print("-------------------------------------------------")
                                                            print("Computer selecting random number in: " +str(remaining_seconds)+" seconds...")
                                                            time.sleep(1)

                                                    if oddpoints < evenspoints:
                                                        print(" ")
                                                        print("ODDS IS LOSING - EVENS IS WINNING")
                                                    
                                                        seconds = int(seconds)
                                                        for remaining_seconds in range(seconds,0,-1):
                                                            print("-------------------------------------------------")
                                                            print("Computer selecting random number in: " +str(remaining_seconds)+" seconds...")
                                                            time.sleep(1)

                                            else:
                                                print("Number "+str(randomnumber)+" is odd")
                                                print("-------------------------------------------------------")
                                                odds.append(randomnumber)
                                                print("Appended number "+str(randomnumber)+" to the Odds numbers list")
                                                print("-------------------------------------------------------")
                                                print("Showing Odd numbers list: ")
                                                print(odds)
                                                print("-------------------------------------------------------")
                                                print("Amount of points for ODD numbers player is: ")
                                                oddpoints = len(odds)
                                                print(oddpoints)

                                                with open('odds_and_evens.log', 'a') as logfile:
                                                    oddpoints = (len(odds))
                                                    lines = "-------------------------------------------------------"
                                                    logfile.write(lines+'\n')
                                                    logfile.write("HIT FOR ODDS PLAYER AT: ")
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    logfile.write(actualdatetime+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Number "+str(randomnumber)+" is odd"+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Appended number "+str(randomnumber)+" to the odd numbers list"+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Showing Odd numbers list: "+'\n')
                                                    logfile.write(str(odds)+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Amount of points for ODDS numbers player is: "+'\n')
                                                    logfile.write(str(oddpoints)+'\n')
                                                    logfile.close()
                                                
                                                if oddpoints == count_set:
                                                    with open('odds_and_evens.log', 'a') as logfile:
                                                        logfile.write(lines+'\n')
                                                        logfile.write("ODDS PLAYER YOU WIN!!, YOU REACHED THE AMOUNT OF POINTS OF: "+'\n')
                                                        logfile.write(str(oddpoints)+'\n')
                                                        logfile.write(lines+'\n')
                                                        logfile.write("Both Lists were reset, and no numbers are contained in them."+'\n')
                                                        hashtag = ("##########################################################")
                                                        logfile.write(hashtag+'\n')
                                                        logfile.write("DATE AND TIME OF FINISHED GAME IS: "+'\n')
                                                        now = datetime.now()
                                                        actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                        logfile.write(" "+'\n')
                                                        logfile.write(actualdatetime+'\n')
                                                        logfile.write(hashtag+'\n')
                                                        now = datetime.now()
                                                        finishtime = datetime.now()
                                                        deltatime = finishtime-startdatetime
                                                        logfile.write(" "+'\n')
                                                        logfile.write("DURATION OF THE PROGRAM WAS: "+'\n')
                                                        logfile.write(" "+'\n')
                                                        logfile.write("hh:mm:ss:microseconds"+'\n')
                                                        logfile.write(str(deltatime)+'\n')
                                                        logfile.write(" "+'\n')
                                                        logfile.write(hashtag+'\n')
                                                        logfile.close()
                                                    print("-------------------------------------------------------")
                                                    print("COMPUTER ODDS PLAYER WINS!!, THE PLAYER REACHED THE AMOUNT OF POINTS OF: ")
                                                    print(oddpoints)
                                                    odds = []
                                                    evens = []
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    print(hashtag)
                                                    print(" ")
                                                    print("GAME FINISHED DATE AND TIME: ")
                                                    print(" ")
                                                    print(actualdatetime)
                                                    print(" ")
                                                    print(hashtag)
                                                    print(" ")
                                                    print("DURATION OF THE PROGRAM WAS: ")
                                                    print(" ")
                                                    print("hh:mm:ss:microseconds")
                                                    print(deltatime)
                                                    print(" ")
                                                    print(hashtag)
                                                    print("Both Lists were reset, and no numbers are contained in them.")
                                                    print("-------------------------------------------------------")
                                                    input("PRESS ENTER TO PLAY AGAIN...")
                                                    
                                                    randoms_game()

                                                else:
                                                    
                                                    with open('odds_and_evens.log', 'a') as logfile:
                                                        evenspoints = len(evens)
                                                        oddpoints = len(odds)
                                                        logfile.write(lines+'\n')
                                                        logfile.write("SCORES AT:"+'\n')
                                                        now = datetime.now()
                                                        actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                        logfile.write(actualdatetime+'\n')
                                                        logfile.write(lines+'\n')
                                                        logfile.write("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints)+'\n')
                                                        logfile.write(lines+'\n')
                                                        logfile.close()
                                                    print(" ")
                                                    print("SCORES AT:")
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    print(actualdatetime)
                                                    print(" ")
                                                    evenspoints = (len(evens))
                                                    oddpoints = (len(odds))
                                                    print("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints))
                                                    if oddpoints > evenspoints:
                                                        print(" ")
                                                        print("ODDS IS WINNING - EVENS IS LOSING")
                                                        seconds = int(seconds)
                                                        for remaining_seconds in range(seconds,0,-1):
                                                            print("-------------------------------------------------")
                                                            print("Computer selecting random number in: " +str(remaining_seconds)+" seconds...")
                                                            time.sleep(1)

                                                    if oddpoints < evenspoints:
                                                        print(" ")
                                                        print("ODDS IS LOSING - EVENS IS WINNING")
                                                        for remaining_seconds in range(seconds,0,-1):
                                                            print("-------------------------------------------------")
                                                            print("Computer selecting random number in: " +str(remaining_seconds)+" seconds...")
                                                            time.sleep(1)
                                                    
                                                    
                                                
                                                    
                
            if gamemode == '1':
                oddpoints = (len(odds))
                evenspoints = (len(evens))
                print(" ")
                print("MODE 1 accessed. ")
                print(" ")
                print("------------------------------------------")
                print("Manual Mode Selected. You will manually have to press enter, for the computer to select the numbers.")
                loop = 2
                while (loop==2):
                    print("------------------------------------------")
                    count_set = input("Set Top count points. The player who reaches this amount of points wins...")
                    if not count_set.isdigit():
                        print("------------------------------------------")
                        print("Only numbers are allowed here!")
                        print("------------------------------------------")
                        loop = 2
                    else:
                        print("-------------------------------------------------------")
                        print("Top count points was set to: "+count_set)
                        count_set = int(count_set)
                        loop = 3
                        while (loop==3):
                            print("-------------------------------------------------------")
                            maxnumber = input("Set a Maximum number. The computer will randomly select numbers between 0, and this number...")
                            if not maxnumber.isdigit():
                                print("------------------------------------------")
                                print("Only numbers are allowed here!")
                                loop = 3
                            else:
                                print("------------------------------------------")
                                print("Maximum Number was set to: "+maxnumber)
                                print("------------------------------------------")
                                input("Ok!, press enter to start the game now...")
                                
                                with open('odds_and_evens.log', 'a') as logfile:
                                        logfile.write("########################################"+'\n')
                                        logfile.write("NEW GAME STARTED"+'\n')
                                        logfile.write("------------------------------------"+'\n')
                                        logfile.write("DATE AND TIME OF STARTED GAME "+'\n')
                                        now = datetime.now()
                                        startdatetime = datetime.now()
                                        logfile.write(str(startdatetime)+'\n')
                                        logfile.write("########################################"+'\n')
                                        logfile.close()

                                print("Game started date and time: ")
                                now = datetime.now()
                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                print(actualdatetime)

                                loop = 4
                                while (loop==4):

                                    randomnumber = random.randint(0, int(maxnumber))
                                    print("-------------------------------------------------------")

                                    if (randomnumber % 2) == 0:
                                        print("Number "+str(randomnumber)+" is even")
                                        print("-------------------------------------------------------")
                                        evens.append(randomnumber)
                                        evenspoints = (len(evens))
                                        print("Appended number "+str(randomnumber)+" to the evens numbers list")
                                        print("-------------------------------------------------------")
                                        print("Showing Even numbers list: ")
                                        print(evens)
                                        print("-------------------------------------------------------")
                                        print("Amount of points for EVEN numbers player is: ")
                                        print(evenspoints)

                                        with open('odds_and_evens.log', 'a') as logfile:
                                            lines = "-------------------------------------------------------"
                                            logfile.write(lines+'\n')
                                            logfile.write("HIT FOR EVENS PLAYER AT: ")
                                            now = datetime.now()
                                            actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                            logfile.write(actualdatetime+'\n')
                                            logfile.write(lines+'\n')
                                            logfile.write("Number "+str(randomnumber)+" is even"+'\n')
                                            logfile.write(lines+'\n')
                                            logfile.write("Appended number "+str(randomnumber)+" to the evens numbers list"+'\n')
                                            logfile.write(lines+'\n')
                                            logfile.write("Showing Even numbers list: "+'\n')
                                            logfile.write(str(evens)+'\n')
                                            logfile.write(lines+'\n')
                                            logfile.write("Amount of points for EVEN numbers player is: "+'\n')
                                            logfile.write(str(evenspoints)+'\n')
                                            logfile.close()
                                        
                                        if evenspoints == count_set:
                                            with open('odds_and_evens.log', 'a') as logfile:
                                                logfile.write(lines+'\n')
                                                logfile.write("EVEN PLAYER YOU WIN!!, YOU REACHED THE AMOUNT OF POINTS OF: "+'\n')
                                                logfile.write(str(evenspoints)+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Both Lists were reset, and no numbers are contained in them."+'\n')
                                                hashtag = ("##########################################################")
                                                logfile.write(hashtag+'\n')
                                                logfile.write("DATE AND TIME OF FINISHED GAME IS: "+'\n')
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                logfile.write(" "+'\n')
                                                logfile.write(actualdatetime+'\n')
                                                logfile.write(hashtag+'\n')
                                                now = datetime.now()
                                                finishtime = datetime.now()
                                                deltatime = finishtime-startdatetime
                                                logfile.write(" "+'\n')
                                                logfile.write("DURATION OF THE PROGRAM WAS: "+'\n')
                                                logfile.write(" "+'\n')
                                                logfile.write("hh:mm:ss:microseconds"+'\n')
                                                logfile.write(str(deltatime)+'\n')
                                                logfile.write(" "+'\n')
                                                logfile.write(hashtag+'\n')
                                                logfile.close()
                                            print("-------------------------------------------------------")
                                            print("COMPUTER EVENS PLAYER WINS!!, THE PLAYER REACHED THE AMOUNT OF POINTS OF:")
                                            print(evenspoints)
                                            odds = []
                                            evens = []
                                            now = datetime.now()
                                            actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                            print(hashtag)
                                            print(" ")
                                            print("GAME FINISHED DATE AND TIME: ")
                                            print(" ")
                                            print(actualdatetime)
                                            print(" ")
                                            print(hashtag)
                                            print(" ")
                                            print("DURATION OF THE PROGRAM WAS: ")
                                            print(" ")
                                            print("hh:mm:ss:microseconds")
                                            print(deltatime)
                                            print(" ")
                                            print(hashtag)
                                            print("Both Lists were reset, and no numbers are contained in them.")
                                            print("-------------------------------------------------------")
                                            input("PRESS ENTER TO PLAY AGAIN...")

                                            randoms_game()
                                        else:
                                            with open('odds_and_evens.log', 'a') as logfile:
                                                evenspoints = (len(evens))
                                                oddpoints = (len(odds))
                                                logfile.write(lines+'\n')
                                                logfile.write("SCORES AT:"+'\n')
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                logfile.write(actualdatetime+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints)+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.close()
                                            print(" ")
                                            print("SCORES AT:")
                                            now = datetime.now()
                                            actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                            print(actualdatetime)
                                            
                                            print(" ")
                                            print("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints))
                                            print("-------------------------------------------------------")
                                            if oddpoints < evenspoints:
                                                        print(" ")
                                                        print("ODDS IS LOSING - EVENS IS WINNING")
                                                        print(" ")
                                                        print("-------------------------------------------------------")
                                                        input("Press enter to continue playing...")
                                            if oddpoints > evenspoints:
                                                        print(" ")
                                                        print("ODDS IS WINNING - EVENS IS LOSING")
                                                        print(" ")
                                                        print("-------------------------------------------------------")
                                                        input("Press enter to continue playing...")
                                            

                                    else:
                                        print("Number "+str(randomnumber)+" is odd")
                                        print("-------------------------------------------------------")
                                        odds.append(randomnumber)
                                        print("Appended number "+str(randomnumber)+" to the Odds numbers list")
                                        print("-------------------------------------------------------")
                                        print("Showing Odd numbers list: ")
                                        print(odds)
                                        print("-------------------------------------------------------")
                                        print("Amount of points for ODD numbers player is: ")
                                        oddpoints = len(odds)
                                        print(oddpoints)

                                        with open('odds_and_evens.log', 'a') as logfile:
                                            oddpoints = (len(odds))
                                            lines = "-------------------------------------------------------"
                                            logfile.write(lines+'\n')
                                            logfile.write("HIT FOR ODDS PLAYER AT: ")
                                            now = datetime.now()
                                            actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                            logfile.write(actualdatetime+'\n')
                                            logfile.write(lines+'\n')
                                            logfile.write("Number "+str(randomnumber)+" is odd"+'\n')
                                            logfile.write(lines+'\n')
                                            logfile.write("Appended number "+str(randomnumber)+" to the odd numbers list"+'\n')
                                            logfile.write(lines+'\n')
                                            logfile.write("Showing Odd numbers list: "+'\n')
                                            logfile.write(str(odds)+'\n')
                                            logfile.write(lines+'\n')
                                            logfile.write("Amount of points for ODDS numbers player is: "+'\n')
                                            logfile.write(str(oddpoints)+'\n')
                                            logfile.close()
                                        
                                        if oddpoints == count_set:
                                            with open('odds_and_evens.log', 'a') as logfile:
                                                logfile.write(lines+'\n')
                                                logfile.write("ODDS PLAYER YOU WIN!!, YOU REACHED THE AMOUNT OF POINTS OF: "+'\n')
                                                logfile.write(str(oddpoints)+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Both Lists were reset, and no numbers are contained in them."+'\n')
                                                hashtag = ("##########################################################")
                                                logfile.write(hashtag+'\n')
                                                logfile.write("DATE AND TIME OF FINISHED GAME IS: "+'\n')
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                logfile.write(" "+'\n')
                                                logfile.write(actualdatetime+'\n')
                                                logfile.write(hashtag+'\n')
                                                now = datetime.now()
                                                finishtime = datetime.now()
                                                deltatime = finishtime-startdatetime
                                                logfile.write(" "+'\n')
                                                logfile.write("DURATION OF THE PROGRAM WAS: "+'\n')
                                                logfile.write(" "+'\n')
                                                logfile.write("hh:mm:ss:microseconds"+'\n')
                                                logfile.write(str(deltatime)+'\n')
                                                logfile.write(" "+'\n')
                                                logfile.write(hashtag+'\n')
                                                logfile.close()
                                            print("-------------------------------------------------------")
                                            print("COMPUTER ODDS PLAYER WINS!!, THE PLAYER REACHED THE AMOUNT OF POINTS OF: ")
                                            print(oddpoints)
                                            odds = []
                                            evens = []
                                            now = datetime.now()
                                            actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                            print(hashtag)
                                            print(" ")
                                            print("GAME FINISHED DATE AND TIME: ")
                                            print(" ")
                                            print(actualdatetime)
                                            print(" ")
                                            print(hashtag)
                                            print(" ")
                                            print("DURATION OF THE PROGRAM WAS: ")
                                            print(" ")
                                            print("hh:mm:ss:microseconds")
                                            print(deltatime)
                                            print(" ")
                                            print(hashtag)
                                            print("Both Lists were reset, and no numbers are contained in them.")
                                            print("-------------------------------------------------------")
                                            input("PRESS ENTER TO PLAY AGAIN...")
                                            
                                            randoms_game()

                                        else:
                                            
                                            with open('odds_and_evens.log', 'a') as logfile:
                                                evenspoints = len(evens)
                                                oddpoints = len(odds)
                                                logfile.write(lines+'\n')
                                                logfile.write("SCORES AT:"+'\n')
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                logfile.write(actualdatetime+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints)+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.close()
                                            print(" ")
                                            print("SCORES AT:")
                                            now = datetime.now()
                                            actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                            print(actualdatetime)
                                            print(" ")
                                            evenspoints = (len(evens))
                                            oddpoints = (len(odds))
                                            print("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints))
                                            print("-------------------------------------------------------")
                                            
                                            print(" ")
                                            print("ODDS IS WINNING - EVENS IS LOSING")
                                            print(" ")
                                            input("Press enter to continue playing...")
                                                    
                                                
                                            

            if gamemode == '2':

                print(" ")
                print("----------------------------------------")
                print("MODE 2 accessed. ")
                print(" ")
                print("Computer automatic Fast mode selected.")
                print("----------------------------------------")
                print("The computer will play both players at full speed")
                print("----------------------------------------")
                print("It is suggested that you enter higher value points, and maxvalues,")
                print("so that you can watch the computer perform its calculations faster.")
                print("----------------------------------------")

                loop = 6
                while (loop==6):

                    
                    loop = 2
                    while (loop==2):

                        count_set = input("Set Top count points. The player who reaches this amount of points wins...")
                        if not count_set.isdigit():
                            print("------------------------------------------")
                            print("Only numbers are allowed here!")
                            print("------------------------------------------")
                            loop = 2
                        else:
                            print("-------------------------------------------------------")
                            print("Top count points was set to: "+count_set)
                            count_set = int(count_set)
                            loop = 3
                            while (loop==3):
                                print("-------------------------------------------------------")
                                maxnumber = input("Set a Maximum number. The computer will randomly select numbers between 0, and this number...")
                                if not maxnumber.isdigit():
                                    print("------------------------------------------")
                                    print("Only numbers are allowed here!")
                                    loop = 3
                                else:
                                    print("------------------------------------------")
                                    print("Maximum Number was set to: "+maxnumber)
                                    print("------------------------------------------")
                                    input("Ok!, press enter to start the game now...")
                                    with open('odds_and_evens.log', 'a') as logfile:
                                            logfile.write("########################################"+'\n')
                                            logfile.write("NEW GAME STARTED"+'\n')
                                            logfile.write("------------------------------------"+'\n')
                                            logfile.write("DATE AND TIME OF STARTED GAME "+'\n')
                                            now = datetime.now()
                                            startdatetime = datetime.now()
                                            logfile.write(str(startdatetime)+'\n')
                                            logfile.write("########################################"+'\n')
                                            logfile.close()

                                    print("Game started date and time: ")
                                    now = datetime.now()
                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                    print(actualdatetime)

                                    loop = 4
                                    while (loop==4):
                                        
                                        randomnumber = random.randint(0, int(maxnumber))
                                        
                                        if (randomnumber % 2) == 0:
                                            
                                            print("Number "+str(randomnumber)+" is even")
                                            print("-------------------------------------------------------")
                                            evens.append(randomnumber)
                                            evenspoints = (len(evens))
                                            print("Appended number "+str(randomnumber)+" to the evens numbers list")
                                            print("-------------------------------------------------------")
                                            print("Showing Even numbers list: ")
                                            print(evens)
                                            print("-------------------------------------------------------")
                                            print("Amount of points for EVEN numbers player is: ")
                                            print(evenspoints)

                                            with open('odds_and_evens.log', 'a') as logfile:
                                                lines = "-------------------------------------------------------"
                                                logfile.write(lines+'\n')
                                                logfile.write("HIT FOR EVENS PLAYER AT: ")
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                logfile.write(actualdatetime+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Number "+str(randomnumber)+" is even"+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Appended number "+str(randomnumber)+" to the evens numbers list"+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Showing Even numbers list: "+'\n')
                                                logfile.write(str(evens)+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Amount of points for EVEN numbers player is: "+'\n')
                                                logfile.write(str(evenspoints)+'\n')
                                                logfile.close()
                                            
                                            if evenspoints == count_set:
                                                with open('odds_and_evens.log', 'a') as logfile:
                                                    logfile.write(lines+'\n')
                                                    logfile.write("EVEN PLAYER YOU WIN!!, YOU REACHED THE AMOUNT OF POINTS OF: "+'\n')
                                                    logfile.write(str(evenspoints)+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Both Lists were reset, and no numbers are contained in them."+'\n')
                                                    hashtag = ("##########################################################")
                                                    logfile.write(hashtag+'\n')
                                                    logfile.write("DATE AND TIME OF FINISHED GAME IS: "+'\n')
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    logfile.write(" "+'\n')
                                                    logfile.write(actualdatetime+'\n')
                                                    logfile.write(hashtag+'\n')
                                                    now = datetime.now()
                                                    finishtime = datetime.now()
                                                    deltatime = finishtime-startdatetime
                                                    logfile.write(" "+'\n')
                                                    logfile.write("DURATION OF THE PROGRAM WAS: "+'\n')
                                                    logfile.write(" "+'\n')
                                                    logfile.write("hh:mm:ss:microseconds"+'\n')
                                                    logfile.write(str(deltatime)+'\n')
                                                    logfile.write(" "+'\n')
                                                    logfile.write(hashtag+'\n')
                                                    logfile.close()
                                                print("-------------------------------------------------------")
                                                print("COMPUTER EVENS PLAYER WINS!!, THE PLAYER REACHED THE AMOUNT OF POINTS OF:")
                                                print(evenspoints)
                                                odds = []
                                                evens = []
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                print(hashtag)
                                                print(" ")
                                                print("GAME FINISHED DATE AND TIME: ")
                                                print(" ")
                                                print(actualdatetime)
                                                print(" ")
                                                print(hashtag)
                                                print(" ")
                                                print("DURATION OF THE PROGRAM WAS: ")
                                                print(" ")
                                                print("hh:mm:ss:microseconds")
                                                print(deltatime)
                                                print(" ")
                                                print(hashtag)
                                                print("Both Lists were reset, and no numbers are contained in them.")
                                                print("-------------------------------------------------------")
                                                input("PRESS ENTER TO PLAY AGAIN...")

                                                randoms_game()
                                            else:
                                                with open('odds_and_evens.log', 'a') as logfile:
                                                    evenspoints = (len(evens))
                                                    oddpoints = (len(odds))
                                                    logfile.write(lines+'\n')
                                                    logfile.write("SCORES AT:"+'\n')
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    logfile.write(actualdatetime+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints)+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.close()
                                                print(" ")
                                                print("SCORES AT:")
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                print(actualdatetime)
                                                
                                                print(" ")
                                                print("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints))
                                                print(" ")
                                                if oddpoints > evenspoints:
                                                    print("ODDS IS WINNING - EVENS IS LOSING")
                                                    print(" ")

                                                if oddpoints < evenspoints:
                                                    print("EVENS IS WINNING - ODDS IS LOSING")
                                                    print(" ")
                                                

                                        else:
                                            print("Number "+str(randomnumber)+" is odd")
                                            print("-------------------------------------------------------")
                                            odds.append(randomnumber)
                                            evenspoints = (len(evens))
                                            oddpoints = (len(odds))
                                            print("Appended number "+str(randomnumber)+" to the Odds numbers list")
                                            print("-------------------------------------------------------")
                                            print("Showing Odd numbers list: ")
                                            print(odds)
                                            print("-------------------------------------------------------")
                                            print("Amount of points for ODD numbers player is: ")
                                            print(oddpoints)

                                            with open('odds_and_evens.log', 'a') as logfile:
                                                oddpoints = (len(odds))
                                                lines = "-------------------------------------------------------"
                                                logfile.write(lines+'\n')
                                                logfile.write("HIT FOR ODDS PLAYER AT: ")
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                logfile.write(actualdatetime+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Number "+str(randomnumber)+" is odd"+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Appended number "+str(randomnumber)+" to the odd numbers list"+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Showing Odd numbers list: "+'\n')
                                                logfile.write(str(odds)+'\n')
                                                logfile.write(lines+'\n')
                                                logfile.write("Amount of points for ODDS numbers player is: "+'\n')
                                                logfile.write(str(oddpoints)+'\n')
                                                logfile.close()
                                            
                                            if oddpoints == count_set:
                                                with open('odds_and_evens.log', 'a') as logfile:
                                                    logfile.write(lines+'\n')
                                                    logfile.write("ODDS PLAYER YOU WIN!!, YOU REACHED THE AMOUNT OF POINTS OF: "+'\n')
                                                    logfile.write(str(oddpoints)+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("Both Lists were reset, and no numbers are contained in them."+'\n')
                                                    hashtag = ("##########################################################")
                                                    logfile.write(hashtag+'\n')
                                                    logfile.write("DATE AND TIME OF FINISHED GAME IS: "+'\n')
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    logfile.write(" "+'\n')
                                                    logfile.write(actualdatetime+'\n')
                                                    logfile.write(hashtag+'\n')
                                                    now = datetime.now()
                                                    finishtime = datetime.now()
                                                    deltatime = finishtime-startdatetime
                                                    logfile.write(" "+'\n')
                                                    logfile.write("DURATION OF THE PROGRAM WAS: "+'\n')
                                                    logfile.write(" "+'\n')
                                                    logfile.write("hh:mm:ss:microseconds"+'\n')
                                                    logfile.write(str(deltatime)+'\n')
                                                    logfile.write(" "+'\n')
                                                    logfile.write(hashtag+'\n')
                                                    logfile.close()
                                                print("-------------------------------------------------------")
                                                print("COMPUTER ODDS PLAYER WINS!!, THE PLAYER REACHED THE AMOUNT OF POINTS OF: ")
                                                print(oddpoints)
                                                odds = []
                                                evens = []
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                print(hashtag)
                                                print(" ")
                                                print("GAME FINISHED DATE AND TIME: ")
                                                print(" ")
                                                print(actualdatetime)
                                                print(" ")
                                                print(hashtag)
                                                print(" ")
                                                print("DURATION OF THE PROGRAM WAS: ")
                                                print(" ")
                                                print("hh:mm:ss:microseconds")
                                                print(deltatime)
                                                print(" ")
                                                print(hashtag)
                                                print("Both Lists were reset, and no numbers are contained in them.")
                                                print("-------------------------------------------------------")
                                                input("PRESS ENTER TO PLAY AGAIN...")
                                                
                                                randoms_game()

                                            else:
                                                
                                                with open('odds_and_evens.log', 'a') as logfile:
                                                    evenspoints = len(evens)
                                                    oddpoints = len(odds)
                                                    logfile.write(lines+'\n')
                                                    logfile.write("SCORES AT:"+'\n')
                                                    now = datetime.now()
                                                    actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                    logfile.write(actualdatetime+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.write("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints)+'\n')
                                                    logfile.write(lines+'\n')
                                                    logfile.close()
                                                print(" ")
                                                print("SCORES AT:")
                                                now = datetime.now()
                                                actualdatetime = now.strftime("%m/%d/%Y - %H:%M:%S:%f")
                                                print(actualdatetime)
                                                print(" ")
                                                evenspoints = (len(evens))
                                                oddpoints = (len(odds))
                                                print("ODDS SCORE IS: "+str(oddpoints)+" | EVENS SCORE IS: "+str(evenspoints))
                                                print(" ")
                                                if oddpoints > evenspoints:
                                                    print("ODDS IS WINNING - EVENS IS LOSING")
                                                    print(" ")

                                                if oddpoints < evenspoints:
                                                    print("EVENS IS WINNING - ODDS IS LOSING")
                                                    print(" ")
                                                                                             
                                                                        
            if not gamemode.isdigit():
                print("------------------------------------------")
                print("Only numbers are allowed here!")
                print("------------------------------------------")
                loop = 5
randoms_game()

    
            

    
    