import os          
from time import sleep as ts
from linecache import getline as gl
from webbrowser import open_new_tab as nw
cext = 'config_crome_extensions.txt'
fext = 'config_firefox_extensions.txt'
cob = 'config_blank.txt'
co = 'config_overclocking.txt'
cg = 'config_games.txt'
def od():
    p('Opening Download(s) in ' + str(s) + ' second(s)')
pe = 'press enter to choose another option...'
conu = 'config_utils.txt'
s = 1 #waiting time between pressing enters
p = print
def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear')     
def cb() :
    os.system("taskkill /im brave.exe /f") 
    cls()
    os.system("taskkill /im msedge.exe /f") 
    cls()
    os.system("taskkill /im chrome.exe /f") 
    cls()
    os.system("taskkill /im firefox.exe /f") 
    cls()
def sm():
    cb()
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
        cls()
        od()
        ts (s)
        cobcounter = 1
        for number in range(10):
            nw(gl(cob, cobcounter))
            cobcounter = cobcounter + 1
        
        pse = input(pe)
        sm()
    elif Main == '2' :      
        cls()
        od()
        ts (s)
        gcounter = 1
        for number in range(10):
                nw(gl(cg, gcounter))
                gcounter = gcounter + 1
        pse = input(pe)
        sm()
    elif Main == '3' :    
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
            pse = input(pe)
            sm()
        elif Brch == '2':
            cls()
            od()
            ts (s)
            nw('https://www.mozilla.org/nl/firefox/new/')
            pse = input(pe)
            sm()
        elif Brch == '3':
            cls()
            od()
            ts (s)
            nw('https://www.torproject.org/download/')
            pse = input(pe)
            sm()
        elif Brch == '4':
            cls()
            od()
            ts (s)
            nw('https://www.google.com/intl/en/chrome/')
            pse = input(pe)
            sm()
    elif Main == '4' :
        cls()
        p ('Choose wich utility... \n\n\n')
        conunames = 1
        for number in range(10):
            p (gl(conu,conunames))
            conunames = conunames + 1
        uch = input()
        utilcounter = 1
        cls()
        for number in range(10):
            if uch == utilcounter :
                cls()
                od()
                ts (s)
                nw(gl(conu, 11 + uch))
    elif Main == '5' :
        cls()
        od()
        ts (s)
        occounter = 1
        for number in range(10):
            nw(gl(co, occounter))
            occounter = occounter + 1
        pse = input(pe)
        sm()
    elif Main == '6' :
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
            pse = input(pe)
            sm()
        elif ExtOpt == '2':
            cls()
            od()
            ts (s)
            extcounter = 1
            for number in range(10):
                nw(gl(fext, extcounter))
                extcounter = extcounter + 1
            pse = input(pe)
            sm()
        pse = input(pe)
        sm()
    elif Main == '9' :
        cls()
        od()
        ts (s)
        nw('https://sites.google.com/view/district14/homepage')
        pse = input(pe)
        sm()
        pse = input(pe)
        sm()
p('made by me :)')
ts (1)
cls()
sm()
