import urllib2
import re
import time;
from time import sleep
import xlwt
from datetime import datetime

            ################################################################
            #                                                                                                                            
            #     --- Volt Social media scraper ---                                                                    
            #                                                                                                                              
            #     NOTE: For interval setting                                                                              
            #    While Facebook, Myspace, and Twitter update instantly,                                 
            #    YouTube(channel views) has a ~5 minute upate period,      
            #    whilst Last.FM's update time is possibly >8 hours         
            #                                                              
            ################################################################

def webScrap(a,b,c,d,e,f,x,y,unit):

    localtime = time.asctime( time.localtime(time.time()) )

    space1 = ":\n\t"
    aPlace = ":"
    bPlace = ":"
    cPlace = ":"
    dPlace = ":"
    ePlace = ":"
    fPlace = ":"
    initialA = 0
    initialB = 0
    initialC = 0
    initialD1 = 0
    initialD2 = 0
    initialE = 0

    # For Excel Sheet
    row = 1
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet')

    for i in range(1, x+1):

        #A - Intializing the Name and gathering Twitter Followers
        
        if a != 'false':
            pageA = urllib2.urlopen(a)
            resultA = pageA.read()

            artistName = re.sub("</", "", (resultA.split('name>')[1])) 

            print('\n\tThis artist is ' + artistName + "." )

            followerCount = re.sub("\D", "", (resultA.split('followers')[1])) 

            print( artistName + ' has ' + followerCount + " Twitter followers.")

        else:
            artistName = "False"
            followerCount = "False"

        aPlace = space1 + followerCount + aPlace

            

        #B - Facebook likes, Conditional so that it works with both the old format and the new one (Timeline).

        pageB = urllib2.urlopen(b)
        resultB = pageB.read()

        if (resultB.split(' ')[8]) == 'xmlns="http://www.w3.org/1999/xhtml"':
            fbLikes = re.sub("\D", "", (resultB.split('uiNumberGiant')[1]))
        elif (resultB.split(' ')[3]) == 'id="facebook"':
          sep = 'likes'
          resultB = resultB.split(sep, 1)[0]
          fbLikes = re.sub("\D", "", (resultB.split('div')[93]))
            
        else: 
            fbLikes = "Error"

        print('This artist has ' + fbLikes + " Facebook likes.")

        bPlace = space1 + fbLikes + bPlace


        #C - Myspace Total Plays 

        pageC = urllib2.urlopen(c)
        resultC = pageC.read()
        sep = 'Today:'
        resultC = resultC.split(sep, 1)[0]
        playCount = re.sub("\D", "", (resultC.split('strong')[3]))

        print('This artist has ' + playCount + " Myspace plays.")
        
        cPlace = space1 + playCount + cPlace
            
        #D - Youtube Channel Script - Gives Youtube Channel Views and Subscribers.

        pageD = urllib2.urlopen(d)
        pageD2 = urllib2.urlopen(d)
        resultD = pageD.read()
        resultD2 = pageD2.read()
        
        sep = '<span class=\"stat-value\">'
        sep2 = '<span class=\"stat-name\">'
        resultD = resultD.split(sep, 1)[1]
        resultD = resultD.split(sep2, 1)[0]

        #For the channel split

        resultD2 = resultD2.split(sep, 2)[2]
        resultD2 = resultD2.split(sep2, 1)[0]
        
        subCount = re.sub("\D", "", (resultD))


        #Channel views
        chanView = re.sub("\D", "", (resultD2))

        print('Their channel has ' + subCount + " Youtube subscribers and " + chanView + " channel views")

        dPlace = space1 + subCount + dPlace
                 
        #E - Last.FM

        pageE = urllib2.urlopen(e)
        resultE = pageE.read()

        sep1 = 'data-listener-count'
        sep2 = '\">'
        resultE = resultE.split(sep1, 1)[1]
        resultE = resultE.split(sep2, 1)[0]
        fmCount = re.sub("\D", "", (resultE))

        print('This artist has had ' + fmCount + ' different listeners on Last.FM' + "\n")

        ePlace = space1 + fmCount + ePlace

        #F - Youtube - Specific Video views
        if f != 'false':
         
            pageF = urllib2.urlopen(f)
            resultF = pageE.read()

            viewCount = re.sub("\D", "", (resultF.split('strong')[4])) 
            likeCount = re.sub("\D", "", (resultF.split('span')[48]))
            dislikeCount = re.sub("\D", "", (resultF.split('span')[50]))

            sep2 = ' - YouTube'
            resultF = resultF.split(sep, 1)[0]
            title = re.sub("\n", "", (resultF.split('title>')[1]))
            print('This video has ' + viewCount + ' Youtube views. It also has ' +  likeCount + ' likes and ' + dislikeCount + ' dislikes -' + title)

            fPlace = space1 + viewCount + fPlace
            
        else:
            title = '~Unavailable~ Value entered was \'false\''
            viewCount = ''
            likeCount = ''
            dislikeCount = ''




        ########################################
        #    THIS MAKES THE INITIAL VALUE      #
        ########################################

        if i == 1:
            initialA += int(followerCount)
            initialB += int(fbLikes)
            initialC += int(playCount)
            initialD1 += int(subCount)
            initialD2 += int(chanView)
            initialE += int(fmCount)
        if i > 1:

            growthA = int(followerCount) - initialA
            growthB = int(fbLikes) - initialB
            growthC = int(playCount) - initialC
            growthD1 = int(subCount) - initialD1
            growthD2 = int(chanView) - initialD2
            growthE = int(fmCount) - initialE
            

            print('In ' + str(y*i) + ' seconds, there was a Facebook change by ' + str(growthA) + ' likes')
            print('A Twitter change by ' + str(growthB) + ' followers,')
            print('A Myspace change by ' + str(growthC) + ' plays')
            print('A YouTube change by ' + str(growthD1) + ' subscribers')
            print('As well as an increase by ' + str(growthD2) + ' channel views')
            print('And a Last FM growth by ' + str(growthE) + ' plays')


        ########################################
        #    Makes EXCEL file                  #
        ########################################
            
            ws.write(row, 0, str(y*i) + unit)
            ws.write(row, 1, growthA)
            ws.write(row, 2, growthB)
            ws.write(row, 3, growthC)
            ws.write(row, 4, growthD1)
            ws.write(row, 5, growthD2)
            ws.write(row, 6, growthE)
            row = row + 1
              
        sleep(y)

        ########################################
        #    AFTER LOOP, make text file    #
        ########################################
           
    open("Statistics.txt","a").write("\n" + "="*65 + "\nLocal Time: " + localtime + "\n" + artistName + "\nYouTube Video Title is\n" + title + "\nYouTube views" + ePlace + "\nYouTube likes: " + likeCount + "\nYouTube dislikes" + dislikeCount + "\nYouTube Channel Views" + chanView + "\nYouTube Subscribers" + dPlace + "\nFacebook Likes" + bPlace + "\nMyspace plays" + cPlace + "\nTwitter followers" + aPlace + "\nDifferent Last.FM plays" + fPlace)


        # Save Excel
    ws.write(0, 1, 'Twitter Follower Count')
    ws.write(0, 2, 'Facebook Likes')  
    ws.write(0, 3, 'Myspace Plays')  
    ws.write(0, 4, 'YouTube Subscribers') 
    ws.write(0, 5, 'YouTube Channel Views') 
    ws.write(0, 6, 'Last.FM plays')     
    wb.save('example.xls')
    
        ####################################
        #             ~ MAIN ~             #
        ####################################
        
userInput = raw_input('Enter the name of the artist: ')
duration = int(raw_input('Enter the number of iterations: '))
interval = int(raw_input('Enter the interval between iterations (seconds): '))
unit = raw_input(str(interval) + ' seconds, minutes, or hours?')
if unit.lower() == 'minutes':
    interval = interval * 60
if unit.lower() ==  'hours':
    interval = interval * 3600
for letter in unit.split():
    unit = unit[0]
    
            #########################
            #                       #
            #    ---DICTIONARY---   #
            #    ----SECTION-----   #
            #                       #
            # Intialize variables   #
            #      into main        #
            #                       #
            ######################### 
            
if userInput.lower() == 'lil wayne'.lower():
    a = 'http://twitter.com/users/show/liltunechi.xml'
    b = 'http://www.facebook.com/LilWayne'
    c = 'http://www.myspace.com/lilwayne'
    d = 'https://www.youtube.com/user/LilWayneVEVO'
    e = 'http://www.last.fm/music/Lil%27+Wayne'
    f = 'false'    

    
webScrap (a, b, c, d , e, f, duration, interval, unit)

