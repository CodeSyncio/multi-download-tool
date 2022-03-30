#start of all function defining , importing , ...

import os          
from time import sleep as ts
from linecache import getline as gl
from webbrowser import open_new_tab as nw
p = print
curdir = os.getcwd()
def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear')     
def cb() :
    procnamescounter = 1
    for number in range (10) :
        os.system("taskkill /im " + gl(browsrprocnames,procnamescounter) +" /f") 
        cls()
        procnamescounter = procnamescounter + 1
folderpath = curdir+'/configs'
cext = curdir+'/configs/crome_extensions.conf'
fext = curdir+'/configs/firefox_extensions.conf'
cob = curdir+'/configs/blank.conf'
co = curdir+'/configs/overclocking.conf'
cg = curdir+'/configs/games.conf'
conu = curdir+'/configs/utilitys.conf'
browsrprocnames = curdir+'/configs/BrowserProcNames.conf'
timesconfig = curdir+'/configs/timeouts.conf'

#preperation for file verifier

foldrcheck = os.path.exists(folderpath)
chromextcheck = os.path.exists(cext)
firefextcheck = os.path.exists(fext)
blankcheck = os.path.exists(cob)
overclcheck = os.path.exists(co)
gamescheck = os.path.exists(cg)
utilscheck = os.path.exists(conu)
procnamescheck = os.path.exists(browsrprocnames)
timescheck = os.path.exists(timesconfig)


#end of all function defining , importing , ...

#start of file verifier

if (chromextcheck 
    and firefextcheck 
    and blankcheck 
    and overclcheck 
    and gamescheck 
    and utilscheck 
    and procnamescheck
    and timescheck) == True:
    p('FILE CHECK PASSED')
    pass
else:
    if foldrcheck == True:
        p('Not all config files are present and/or named correctly, more info:\n\n[True = file is present]\n[False = file is missing/named wrong]\n\n\n')
        p('crome_extensions.conf = '+ str(chromextcheck))
        p('firefox_extensions.conf = '+ str(firefextcheck))
        p('blank.conf = '+ str(blankcheck))
        p('overclocking.conf = '+ str(overclcheck))
        p('games.conf = '+ str(gamescheck))
        p('utilitys.conf = '+ str(utilscheck))
        p('BrowserProcNames.conf = '+ str(procnamescheck))
        p('timeouts.conf = '+ str(timescheck))
        p('\n\n')
        tempfunc = input('Press enter to exit...')
        quit()
    else:
        p('the folder ("configs") does not exist or is misnamed')
        p('\n\n')
        tempfunc = input('Press enter to exit...')
        quit()

#end of file verifier

#Start of defining main program
s = int(gl(timesconfig,2))
def od():
    p('Opening Download(s) in ' + str(s) + ' second(s)')
pe = 'press enter to choose another option...'


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
        cb()      
        cls()
        od()
        ts (s)
        cobcounter = 1
        for number in range(10):
            nw(gl(cob, cobcounter))
            cobcounter = cobcounter + 1
        sm()
    elif Main == '2' :
        cb()      
        cls()
        od()
        ts (s)
        gcounter = 1
        for number in range(10):
                nw(gl(cg, gcounter))
                gcounter = gcounter + 1
        sm()
    elif Main == '3' : 
        cb()   
        cls()
        p ('Choose wich browser... \n\n\n')
        p ('[1] Brave')
        p ('[2] firefox')
        p ('[3] TOR')
        p ('[4] google chrome')
        Brch = input()
        if Brch == '1':
            cls()
            od()
            ts (s)
            nw('https://brave.com/download/')
            sm()
        elif Brch == '2':
            cls()
            od()
            ts (s)
            nw('https://www.mozilla.org/nl/firefox/new/')
            sm()
        elif Brch == '3':
            cls()
            od()
            ts (s)
            nw('https://www.torproject.org/download/')
            sm()
        elif Brch == '4':
            cls()
            od()
            ts (s)
            nw('https://www.google.com/intl/en/chrome/')
            sm()
    elif Main == '4' :
        cb()
        cls()
        p ('Choose wich utility... \n\n\n')
        conunames = 1
        for number in range(10):
            p (gl(conu,conunames))
            conunames = conunames + 1
        uch = input()
        utilcounter = 1
        cls()
        for number in range(11):
            if int(uch) == utilcounter :
                cls()
                od()
                ts (s)
                finallineutil = 11 +int(uch)
                nw(gl(conu,finallineutil ))
                sm()
            else:
                utilcounter = utilcounter + 1
    elif Main == '5' :
        cb()
        cls()
        od()
        ts (s)
        occounter = 1
        for number in range(10):
            nw(gl(co, occounter))
            occounter = occounter + 1
        sm()
    elif Main == '6' :
        cb()
        cls()
        p('Choose your browser: \n\n\n')
        p('[1] Any chromium based browser')
        p('[2] Firefox (tor)')
        ExtOpt = input()
        if ExtOpt == '1':
            cls()
            od()
            ts (s)
            extcounter = 1
            for number in range(10):
                nw(gl(cext, extcounter))
                extcounter = extcounter + 1
            sm()
        elif ExtOpt == '2':
            cls()
            od()
            ts (s)
            extcounter = 1
            for number in range(10):
                nw(gl(fext, extcounter))
                extcounter = extcounter + 1
            sm()
        sm()
    elif Main == '9' :
        cb()
        cls()
        od()
        ts (s)
        nw('https://sites.google.com/view/district14/homepage')
        sm()

#end of defining main program

#start of porgram

p('made by me :)')
ts (1)
cls()
sm()
