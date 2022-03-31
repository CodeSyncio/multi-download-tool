#====INFO====#
#I am far from being a perfect programmer, so some things might be very clumzy, but they work :o
#i also know some of my code is very "unclean", i don't have the time to make all 
#little details perfect.
#====INFO FOR MYSELF LATER====
#MADE IN 2022
#30/03/2022 --- i am still very clumzy






#start of all function defining , importing , ...

import os          
from time import sleep as sleep
from linecache import getline as getl
from webbrowser import open_new_tab as newbrowserproc

if os.path.exists("latest_error_log.txt"):
      os.remove("latest_error_log.txt")
else:
  pass

p = print
curdir = os.getcwd()
def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear')     
def killbrowser() :
    procnamescounter = 1
    for number in range (10) :
        os.system("taskkill /im " + getl(path_browsrprocnames,procnamescounter) +" /f") 
        cls()
        procnamescounter = procnamescounter + 1
pathconfigfolder = curdir+'/configs'
path_chrome_ext = curdir+'/configs/crome_extensions.conf'
path_firefox_ext = curdir+'/configs/firefox_extensions.conf'
path_blank = curdir+'/configs/blank.conf'
path_overclocking = curdir+'/configs/overclocking.conf'
path_games = curdir+'/configs/games.conf'
path_utilitys = curdir+'/configs/utilitys.conf'
path_browsrprocnames = curdir+'/configs/BrowserProcNames.conf'
path_timeouts = curdir+'/configs/timeouts.conf'

#preperation for file verifier

foldrcheck = os.path.exists(pathconfigfolder)
chromextcheck = os.path.exists(path_chrome_ext)
firefoxextcheck = os.path.exists(path_firefox_ext)
blankcheck = os.path.exists(path_blank)
overclockcheck = os.path.exists(path_overclocking)
gamescheck = os.path.exists(path_games)
utilscheck = os.path.exists(path_utilitys)
processnamescheck = os.path.exists(path_browsrprocnames)
timescheck = os.path.exists(path_timeouts)


#end of all function defining , importing , ...

#start of file verifier

if (chromextcheck 
    and firefoxextcheck 
    and blankcheck 
    and overclockcheck
    and gamescheck 
    and utilscheck 
    and processnamescheck
    and timescheck) == True:
    p('FILE CHECK PASSED.')
    pass

else:
    
    if foldrcheck == True:
        
        logfile = open("latest_error_log.txt", "w")
        logfile.writelines(["LATEST OUTPUT OF FILE VERIFIER:", "\n\n[True = file was present]\n[False = file was missing/named wrong]",
                    "\n\ncrome_extensions.conf = " +str(chromextcheck),
                    "\nfirefox_extensions.conf = " + str(firefoxextcheck),
                    "\nblank.conf = "+str(blankcheck),
                    "\noverclocking.conf = "+ str(overclockcheck),
                    "\ngames.conf = "+ str(gamescheck),
                    "\nutilitys.conf = " + str(utilscheck),
                    "\nBrowserProcNames.conf = "+str(processnamescheck),
                    "\ntimeouts.conf = "+ str(timescheck)])
        logfile.close()
        
        p('Not all config files are present and/or named correctly, more info:\n\n[True = file is present]\n[False = file is missing/named wrong]\n\n\n')
        p('crome_extensions.conf = '+ str(chromextcheck))
        p('firefox_extensions.conf = '+ str(firefoxextcheck))
        p('blank.conf = '+ str(blankcheck))
        p('overclocking.conf = '+ str(overclockcheck))
        p('games.conf = '+ str(gamescheck))
        p('utilitys.conf = '+ str(utilscheck))
        p('BrowserProcNames.conf = '+ str(processnamescheck))
        p('timeouts.conf = '+ str(timescheck))
        p('\n\n')
        
        tempfunc = input('Press enter to exit...')
        quit()
   
    else:
        
        logfile = open("latest_error_log.txt", "w")
        logfile.writelines(["LATEST OUTPUT OF FILE VERIFIER:",
                            "\n\n The folder 'configs' located in the root folder is misnamed/could noy be found.",
                            "\n\n[True = file is present]\n[False = file is missing/named wrong]",
                            "\n\nRaw error log:","\n\nconfigs = "+ str(foldrcheck)])
        p('the folder ("configs") does not exist or is misnamed')
        p('\n\n')
        
        tempfunc = input('Press enter to exit...')
        quit()

#end of file verifier

#Start of defining main program
timeout_seconds = int(getl(path_timeouts,2))
def opendwnlds():
    p('Opening Download(s) in ' + str(timeout_seconds) + ' second(s)')



def sm():
    cls()
    p ('[Choose a number corresponding to an option]')  
    p ('OPTIONS: \n \n \n')
    p ('[1] Tools for after blank windows installation')
    p ('[2] Game Launchers')
    p ('[3] Internet (browsers etc.)')
    p ('[4] Utilities')
    p ('[5] Overclocking')
    p ('[6] Usefull Extensions (browsers)')
    p ('[9] my discord :)')
    Main = input()
    if Main == '1' :  
        killbrowser()      
        cls()
        opendwnlds()
        sleep (timeout_seconds)
        cobcounter = 1
        for number in range(10):
            newbrowserproc(getl(path_blank, cobcounter))
            cobcounter = cobcounter + 1
        sm()
    elif Main == '2' :
        killbrowser()      
        cls()
        opendwnlds()
        sleep (timeout_seconds)
        gcounter = 1
        for number in range(10):
                newbrowserproc(getl(path_games, gcounter))
                gcounter = gcounter + 1
        sm()
    elif Main == '3' : 
        killbrowser()   
        cls()
        p ('Choose wich browser... \n\n\n')
        p ('[1] Brave')
        p ('[2] firefox')
        p ('[3] TOR')
        p ('[4] google chrome')
        Brch = input()
        if Brch == '1':
            cls()
            opendwnlds()
            sleep (timeout_seconds)
            newbrowserproc('https://brave.com/download/')
            sm()
        elif Brch == '2':
            cls()
            opendwnlds()
            sleep (timeout_seconds)
            newbrowserproc('https://www.mozilla.org/nl/firefox/new/')
            sm()
        elif Brch == '3':
            cls()
            opendwnlds()
            sleep (timeout_seconds)
            newbrowserproc('https://www.torproject.org/download/')
            sm()
        elif Brch == '4':
            cls()
            opendwnlds()
            sleep (timeout_seconds)
            newbrowserproc('https://www.google.com/intl/en/chrome/')
            sm()
    elif Main == '4' :
        killbrowser()
        cls()
        p ('Choose wich utility... \n\n\n')
        conunames = 1
        for number in range(10):
            p (getl(path_utilitys,conunames))
            conunames = conunames + 1
        uch = input()
        utilcounter = 1
        cls()
        for number in range(11):
            if int(uch) == utilcounter :
                cls()
                opendwnlds()
                sleep (timeout_seconds)
                finallineutil = 11 +int(uch)
                newbrowserproc(getl(path_utilitys,finallineutil ))
                sm()
            else:
                utilcounter = utilcounter + 1
    elif Main == '5' :
        killbrowser()
        cls()
        opendwnlds()
        sleep (timeout_seconds)
        occounter = 1
        for number in range(10):
            newbrowserproc(getl(path_overclocking, occounter))
            occounter = occounter + 1
        sm()
    elif Main == '6' :
        killbrowser()
        cls()
        p('Choose your browser: \n\n\n')
        p('[1] Any chromium based browser')
        p('[2] Firefox (tor)')
        ExtOpt = input()
        if ExtOpt == '1':
            cls()
            opendwnlds()
            sleep (timeout_seconds)
            extcounter = 1
            for number in range(10):
                newbrowserproc(getl(path_chrome_ext, extcounter))
                extcounter = extcounter + 1
            sm()
        elif ExtOpt == '2':
            cls()
            opendwnlds()
            sleep (timeout_seconds)
            extcounter = 1
            for number in range(10):
                newbrowserproc(getl(path_firefox_ext, extcounter))
                extcounter = extcounter + 1
            sm()
        sm()
    elif Main == '9' :
        killbrowser()
        cls()
        opendwnlds()
        sleep (timeout_seconds)
        newbrowserproc('https://sites.google.com/view/district14/homepage')
        sm()

#end of defining main program

#start of porgram

p('made by me :)')
sleep (1)
cls()
sm()
