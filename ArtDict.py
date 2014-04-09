class ArtDict:
    '''
    All the input values for a bunch of artists
    Edit, add artists.

    This is old and inefficient! turn into dictionary
    '''
    def __init__(self, name):
	    self.name = name

    def artInputs (self, userInput):
    	
        if self.name == 'lil wayne'.lower():
            a = 'http://twitter.com/users/show/liltunechi.xml'
            b = 'http://www.facebook.com/LilWayne'
            c = 'http://www.myspace.com/lilwayne'
            d = 'https://www.youtube.com/user/LilWayneVEVO'
            e = 'http://www.last.fm/music/Lil%27+Wayne'
            f = 'false'    

        elif self.name == 'rihanna'.lower():
            a = 'http://twitter.com/users/show/rihanna.xml'
            b = 'http://www.facebook.com/rihanna' 
            c = 'www.myspace.com/rihanna'
            d = 'http://www.youtube.com/user/rihanna'
            e = 'http://www.last.fm/music/Rihanna'
            f = 'false'    

        elif self.name == 'lmfao'.lower():
            a = 'http://twitter.com/users/show/LMFAO.xml'
            b = 'http://www.facebook.com/LMFAO'
            c = 'http://www.myspace.com/LMFAO'
            d = 'http://www.youtube.com/user/LMFAO'
            e = 'http://last.fm/music/LMFAO'
            f = 'false'    

        elif self.name == 'adele'.lower():
            a = 'http://twitter.com/users/show/officaladele.xml'
            b = 'http://www.facebook.com/Adele'
            c = 'http://www.myspace.com/Adelelondon'
            d = 'http://www.youtube.com/artist/Adele'
            e = 'http://last.fm/music/Adele'
            f = 'false'    
        elif self.name == 'akon'.lower():
            a = 'http://twitter.com/users/show/akon.xml'
            b = 'http://www.facebook.com/akon'
            c = 'http://www.myspace.com/akon'
            d = 'http://www.youtube.com/artist/akon'
            e = 'http://last.fm/music/akon'
            f = 'false'    
        elif self.name == 'chris brown'.lower():
            a = 'http://twitter.com/users/show/chrisbrown.xml'
            b = 'http://www.facebook.com/chrisbrown'
            c = 'http://www.myspace.com/chrisbrown'
            d = 'http://www.youtube.com/user/Chris+Brown'
            e = 'http://last.fm/music/chrisbrown'
            f = 'false'    
        elif self.name == 'whitney houston'.lower():
            a = 'false'
            b = 'http://www.facebook.com/whitneyhouston'
            c = 'http://www.myspace.com/whitneyhouston'
            d = 'http://www.youtube.com/user/whitneyhouston'
            e = 'http://last.fm/music/whitney+houston'
            f = 'false'    
        elif self.name == 'pitbull'.lower():
            a = 'http://twitter.com/users/show/pitbull.xml'
            b = 'http://www.facebook.com/pitbull'
            c = 'http://www.myspace.com/pitbull'
            d = 'http://www.youtube.com/user/pitbull'
            e = 'http://last.fm/music/pitbull'
            f = 'false'    
        elif self.name == 'eminem'.lower():
            a = 'http://twitter.com/users/show/eminem.xml'
            b = 'http://www.facebook.com/eminem'
            c = 'http://www.myspace.com/eminem'
            d = 'http://www.youtube.com/user/eminem'
            e = 'http://last.fm/music/eminem'
            f = 'false'    
        elif self.name == 'drake'.lower(): 
	        a = 'http://twitter.com/users/show/drake.xml'
	        b = 'http://www.facebook.com/drake'
	        c = 'http://www.myspace.com/thisisdrake'
	        d = 'http://www.youtube.com/user/drakeofficial'
	        e = 'http://last.fm/music/drake' 
	        f = 'false'
        elif self.name == 'beyonce'.lower():
            a = 'http://twitter.com/users/show/Beyonce.xml'
            b = 'http://www.facebook.com/Beyonce'
            c = 'http://www.myspace.com/Beyonce'
            d = 'http://www.youtube.com/user/Beyonce'
            e = 'http://last.fm/music/beyonce'
            f = 'false'    
        elif self.name == 'taylor swift'.lower():
            a = 'http://twitter.com/users/show/taylorswift.xml'
            b = 'http://www.facebook.com/taylorswift'
            c = 'http://www.myspace.com/taylorswift'
            d = 'http://www.youtube.com/user/taylorswift'
            e = 'http://last.fm/music/taylor+swift'
            f = 'false'    
        elif self.name == 'justin bieber'.lower():
            a = 'http://twitter.com/users/show/justinbieber.xml'
            b = 'http://www.facebook.com/justinbieber'
            c = 'http://www.myspace.com/justinbieber'
            d = 'http://www.youtube.com/user/justinbieber'
            e = 'http://last.fm/music/justin+bieber'
            f = 'false'      
        elif self.name == "adestria".lower():
	        a = 'http://twitter.com/#!/adestriaband'
	        b = 'http://www.facebook.com/adestriamusic'
	        c = 'http://www.myspace.com/adestriamusic'
	        d = 'http://www.youtube.com/Adestriamusic'
	        e = 'http://www.last.fm/music/Adestria'
	        f = 'false'    

        elif self.name == 'All That Remains'.lower():
	        a = 'http://twitter.com/users/show/atrhq.xml'
	        b = 'http://www.facebook.com/allthatremains'
	        c = 'http://www.myspace.com/allthatremains'
	        d = 'http://www.youtube.com/user/allthatremainsVEVO'
	        e = 'http://www.last.fm/music/All+That+Remains'
	        f = 'false'   
        elif self.name == 'Mathias Anderle'.lower():
	        a = 'http://twitter.com/users/show/mathiasanderle.xml'
	        b = 'http://www.facebook.com/mathiasanderlemusic'
	        c = 'http://www.myspace.com/mathiasanderlemusic'
	        d = 'http://www.youtube.com/user/mathiasanderlemusic'
	        e = 'http://last.fm/music/Mathias+Anderle'
	        f = 'false'    
        elif self.name == 'Nicole Atkins'.lower():
	        a = 'http://twitter.com/users/show/nicoleatkins'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/nicoleatkins'
	        d = 'http://www.youtube.com/user/nicoleatkinsVEVO'
	        e = 'http://last.fm/music/Nicole+Atkins'
	        f = 'false'    
        elif self.name == 'Attila'.lower():
	        a = 'http://twitter.com/users/show/AttilaGA.xml'
	        b = 'http://www.facebook.com/AttilaGA'
	        c = 'http://www.myspace.com/attilaga'
	        d = 'http://www.youtube.com/user/AttilaVEVO'
	        e = 'http://last.fm/music/Attila'
	        f = 'false'    
        elif self.name == 'Joan Baez'.lower():
	        a = 'http://twitter.com/users/show/joancbaez.xml'
	        b = 'http://www.facebook.com/OfficialJoanBaez'
	        c = 'http://www.myspace.com/joanbaez'
	        d = 'http://youtube.com/joanbaez'
	        e = 'http://last.fm/music/joan+baez'
	        f = 'false'    
        elif self.name == 'Dave Barnes'.lower():
	        a = 'http://twitter.com/users/show/davebarnesmusic'
	        b = 'http://www.facebook.com/davebarnesmusic'
	        c = 'http://www.myspace.com/davebarnes'
	        d = 'http://www.youtube.com/user/DaveBarnesVEVO'
	        e = 'http://last.fm/music/Dave+Barnes'
	        f = 'false'    
        elif self.name == 'Brad'.lower():
	        a = 'http://twitter.com/users/show/thebandbrad.xml'
	        b = 'http://www.facebook.com/bradcorporation'
	        c = 'http://www.myspace.com/bradcorporation'
	        d = 'http://www.youtube.com/user/bradcorporation'
	        e = 'http://www.last.fm/music/Brad'
	        f = 'false'    
        elif self.name == 'A Bullet for Pretty Boy'.lower():
	        a = 'http://twitter.com/#!/abfpb'
	        b = 'https://www.facebook.com/abulletforprettyboy'
	        c = 'http://www.myspace.com/abulletforprettyboy'
	        d = 'http://www.youtube.com/abulletforprettyboy'
	        e = 'http://www.last.fm/music/A+Bullet+For+Pretty+Boy'
	        f = 'false'   
        elif self.name == 'Vanessa Carlton'.lower():
	        a = 'http://twitter.com/users/show/vanessacarlton.xml'
	        b = 'http://www.facebook.com/vanessacarlton'
	        c = 'http://www.myspace.com/vanessacarlton'
	        d = 'http://www.youtube.com/user/VanessaCarltonVEVO'
	        e = 'http://last.fm/music/Vanessa+Carlton'
	        f = 'false'    
        elif self.name == 'Simon Collins'.lower():
	        a = 'http://twitter.com/users/show/simoncollins_.xml'
	        b = 'http://www.facebook.com/lightyearsmusic.simoncollins'
	        c = 'http://www.myspace.com/simoncollins'
	        d = 'http://www.youtube.com/user/simoncollinsmusic'
	        e = 'http://last.fm/music/Simon+Collins'
	        f = 'false'    
        elif self.name == 'Casino Madrid'.lower():
	        a = 'http://twitter.com/users/show/casinomadrid.xml'
	        b = 'http://www.facebook.com/casinomadrid'
	        c = 'http://www.myspace.com/casinomadrid'
	        d = 'http://www.youtube.com/user/csnmadrid'
	        e = 'http://last.fm/music/casino+madrid'
	        f = 'false'    
        elif self.name == 'Chelsea Grin'.lower():
	        a = 'http://twitter.com/users/show/chelseagrinUT.xml'
	        b = 'http://www.facebook.com/ChelseaGrinMetal'
	        c = 'http://www.myspace.com/chelseagrinmetal'
	        d = 'http://www.youtube.com/user/chelseagrinTV'
	        e = 'http://last.fm/music/Chelsea+Grin'
	        f = 'false'    
        elif self.name == 'Close to Home'.lower():
	        a = 'http://twitter.com/users/show/wearecth.xml'
	        b = 'http://www.facebook.com/OfficialCloseToHome'
	        c = 'http://www.myspace.com/cth'
	        d = 'http://www.youtube.com/user/closetohome'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'The Crimson Armada'.lower(): 
	        a = 'http://twitter.com/users/show/tcaband.xml'
	        b = 'http://www.facebook.com/TCAband'
	        c = 'http://www.myspace.com/thecrimsonarmada'
	        d = 'http://www.youtube.com/user/thecrimsonarmadallc'
	        e = 'http://last.fm/music/the+crimson+armada'
	        f = 'false'    
        elif self.name == 'The Dangerous Summer'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Dead Confederate'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Devin the Dude'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Kevin Devine'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Emerson, Lake and Palmer'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'EndeverafteR'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'For the Fallen Dreams'.lower(): 
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name== 'For Today'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Hit the Lights'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Just Surrender'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Ocean Is Theory'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'I Declare War'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Vanna'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Angelique Kidjo'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Madina Lake'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Man Made Machine'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Andy McKee'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Jon McLaughlin'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Nonpoint'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Norma Jean'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'P.O.D.'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Saves the Day'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Semi Precious Weapons'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Such Gold'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Shadows Fall'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Ryan Shaw'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Tina Sugandh'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'The Summer Set'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Kelly Sweet'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'The Sword'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Cesar Velazquez'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'The Wiggles'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Dar Williams'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Chris Brown'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'    
        elif self.name == 'Zappa Plays Zappa'.lower():
	        a = 'http://twitter.com/users/show/chrisbrown.xml'
	        b = 'http://www.facebook.com/chrisbrown'
	        c = 'http://www.myspace.com/chrisbrown'
	        d = 'http://www.youtube.com/user/Chris+Brown'
	        e = 'http://last.fm/music/chrisbrown'
	        f = 'false'   
	        
	        
'''
THE WORD ALIVE
Youtube:  http://www.youtube.com/user/TheWordAliveBand
Myspace: http://www.myspace.com/thewordalive
Twitter: https://twitter.com/thewordalive
Facebook: http://www.facebook.com/thewordalive
RUFUS WAINWRIGHT
Youtube: http://www.youtube.com/user/valentinalover
MySpace : http://www.myspace.com/rufuswainwright
Twitter: https://twitter.com/rufuswainwright
Facebook: http://www.facebook.com/rufuswainwrightofficial
ANDREW JACKSON JIHAD
Youtube: http://www.youtube.com/user/BrantosIscariot
MySpace : http://www.myspace.com/andrewjacksonjihad
Twitter: https://twitter.com/ajjtheband
Facebook: http://www.facebook.com/pages/Andrew-Jackson-Jihad/123094587723
THE SUMMER SET
Youtube: http://www.youtube.com/user/thesummerset
MySpace : http://www.myspace.com/thesummerset
Twitter: https://twitter.com/the_summer_set
Facebook: http://www.facebook.com/thesummerset
MAROON 5:
Youtube: http://www.youtube.com/user/Maroon5
MySpace : http://www.myspace.com/Maroon5
Twitter: https://twitter.com/maroon5
Facebook: http://www.facebook.com/maroon5
DRAKE:
Youtube:  http://www.youtube.com/user/DrakeVEVO
MySpace : http://www.myspace.com/thisisdrake
Twitter: https://twitter.com/drake
Facebook: http://www.facebook.com/Drake
RIHANNA:
Youtube : http://www.youtube.com/user/Rihanna
MySpace : http://www.myspace.com/rihanna
Twitter: https://twitter.com/rihanna
Facebook: http://www.facebook.com/rihanna
CHILDISH GAMBINO:
Youtube : http://www.youtube.com/user/IAMDONALDFAN
MySpace : http://www.myspace.com/childishgambino
Twitter: https://twitter.com/donaldglover
Facebook: http://www.facebook.com/IamDonald
mewithoutYou
Youtube: http://www.youtube.com/user/jaja351
MySpace : http://www.myspace.com/mewithoutyou
Twitter: https://twitter.com/mewithoutYou
Facebook: http://www.facebook.com/mewithoutyou
La Dispute
Youtube: http://www.youtube.com/user/xxBloodyMemories
MySpace : http://www.myspace.com/ladispute
Twitter: https://twitter.com/ladisputeband
Facebook: http://www.facebook.com/LaDisputeMusic
I Call Fives
Youtube: None http://www.youtube.com/PureNoiseRecs
MySpace : http://www.myspace.com/icallfives
Twitter: https://twitter.com/icallfives
Facebook: http://www.facebook.com/icallfives
The Wonder Years
Youtube: Hopeless Records Youtube
MySpace : http://www.myspace.com/thewonderyears
Twitter: https://twitter.com/twypoppunk
Facebook: http://www.facebook.com/thewonderyearsband
The Story So Far
Youtube: http://www.youtube.com/user/TheStorySoFarVEVO
MySpace : http://www.myspace.com/thestorysofarca
Twitter: https://twitter.com/thestorysofarca
Facebook: http://www.facebook.com/thestorysofarca
State Champs
Youtube:  http://www.youtube.com/user/statechampsny
MySpace : http://www.myspace.com/statechampsny
Twitter: https://twitter.com/state_champs
Facebook: http://www.facebook.com/statechampsny
Justin Bieber
Youtube: http://www.youtube.com/user/kidrauhl
MySpace : http://www.myspace.com/justinbieber
Twitter: https://twitter.com/justinbieber
Facebook: http://www.facebook.com/JustinBieber
Cody Simpson
Youtube: http://www.youtube.com/user/CodySimpsonMusic
MySpace : http://www.myspace.com/codysimpsonmusic
Twitter: https://twitter.com/codysimpson
Facebook: http://www.facebook.com/codysimpsonmusic
Bruce Springsteen
Youtube: http://www.youtube.com/user/BruceSpringsteen
MySpace : http://www.myspace.com/brucespringsteen
Twitter: https://twitter.com/springsteen
Facebook:  http://www.facebook.com/brucespringsteen
Elton John
Youtube: http://www.youtube.com/user/EltonJohnVEVO
MySpace : http://www.myspace.com/eltonjohn
Twitter: https://twitter.com/eltonjohndotcom
Facebook: http://www.facebook.com/EltonJohn
MxPx
Youtube: http://www.youtube.com/user/mxpxvideoblog
MySpace : http://www.myspace.com/mxpx
Twitter: https://twitter.com/mxpx
Facebook: http://www.facebook.com/MxPxPx
Kanye West
Youtube: http://www.youtube.com/user/kanyewest
MySpace : http://www.myspace.com/kanyewest
Twitter: https://twitter.com/kanyewest
Facebook: http://www.facebook.com/pages/Kayne-West/111738558845479
Rick Ross
Youtube: http://www.youtube.com/user/OfficialRickRossTV
MySpace : http://www.myspace.com/rickross
Twitter: https://twitter.com/rickyrozay
Facebook: http://www.facebook.com/rickross
J Cole
Youtube: http://www.youtube.com/user/JColeVEVO
MySpace : http://www.myspace.com/jcole
Twitter: https://twitter.com/jcolenc
Facebook: http://www.facebook.com/JColeMusic
Nickelback
Youtube:  http://www.youtube.com/user/nickelbacktv
MySpace : http://www.myspace.com/nickelback
Twitter: https://twitter.com/nickelback
Facebook: http://www.facebook.com/Nickelback
Three Days Grace
Youtube: http://www.youtube.com/user/ThreeDaysGraceVideos
MySpace : http://www.myspace.com/threedaysgrace
Twitter:  https://twitter.com/threedaysgrace
Facebook: http://www.facebook.com/threedaysgrace
Breaking Benjamin
Youtube: http://www.youtube.com/user/BreakingBenjaminOFCL
MySpace : http://www.myspace.com/breakingbenjamin
Twitter: https://twitter.com/breakingbenj
Facebook: http://www.facebook.com/BreakingBenjamin
'''
        return(a,b,c,d,e,f)	        
