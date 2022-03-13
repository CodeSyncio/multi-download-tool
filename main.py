#import fuctions

import os
from pkgutil import extend_path             
import time
import webbrowser
import linecache

#clear console command

def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear')     








#used to kill all running browser processes (avoid a big mess)

def clrbrowsers() :

   
    
    os.system("taskkill /im brave.exe /f") 
    cls()
    os.system("taskkill /im msedge.exe /f") 
    cls()
    os.system("taskkill /im chrome.exe /f") 
    cls()
    os.system("taskkill /im firefox.exe /f") 
    cls()
   
  
clrbrowsers()


#main fuction of program

def startmenu():
    
    cls()
    print ('[Choose a number corresponding to an option]')
    print ('OPTIONS: \n \n \n')
    print ('[1] Tools for after blank windows installation')
    print ('[2] Game Launchers')
    print ('[3] Internet (browsers etc.)')
    print ('[4] Utilities')
    print ('[5] Overclocking')
    print ('[6] Usefull Extensions (browsers)')
    print ('[9] my discord :)')
    

    MainOptChoise = input()

    if MainOptChoise == '1' :
        cls()
        print('Opening Downloads in 3 sec...')
        
        
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 1))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 2))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 3))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 4))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 5))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 6))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 7))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 8))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 9))
        webbrowser.open_new_tab(linecache.getline('blank_tools_config.txt', 10))
        




        prsenter = input('press enter to choose another option...')
        startmenu()
    elif MainOptChoise == '2' :
        
        cls()
        print('Opening Downloads in 3 sec...')
        time.sleep (3)
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 1))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 2))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 3))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 4))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 5))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 6))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 7))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 8))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 9))
        webbrowser.open_new_tab(linecache.getline('game_launchers_config.txt', 10))
        prsenter = input('press enter to choose another option...')
        startmenu()


    elif MainOptChoise == '3' :
        cls()
        print ('Choose wich browser... \n\n\n')
        print ('[1] Brave')
        print ('[2] firefox')
        print ('[3] TOR')
        print ('[4] google chrome')
       
        
        BrowserChoise = input()

        if BrowserChoise == '1':
            cls()
            print('Opening Download in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab('https://brave.com/download/')
            prsenter = input('press enter to choose another option...')
            startmenu()
        elif BrowserChoise == '2':
            cls()
            print('Opening Download in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab('https://www.mozilla.org/nl/firefox/new/')
            prsenter = input('press enter to choose another option...')
            startmenu()

        elif BrowserChoise == '3':
            cls()
            print('Opening Download in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab('https://www.torproject.org/download/')
            prsenter = input('press enter to choose another option...')
            startmenu()

        elif BrowserChoise == '4':
            cls()
            print('Opening Download in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab('https://www.google.com/intl/en/chrome/')
            prsenter = input('press enter to choose another option...')
            startmenu()

             

    elif MainOptChoise == '4' :
        cls()
        print ('Choose wich utility... \n\n\n')
        print ('[1] qBittorrent')
        print ('[2] WinDirStat')
        print ('[3] Malwarebytes')
        print ('[4] Visual Studio')

        utilchoise = input()

        if utilchoise == '1':
            cls()
            print('Opening Download in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab('https://www.qbittorrent.org/download.php')
            prsenter = input('press enter to choose another option...')
            startmenu()

        elif utilchoise == '2':
            cls()
            print('Opening Download in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab('https://www.fosshub.com/WinDirStat.html')
            prsenter = input('press enter to choose another option...')
            startmenu()

        elif utilchoise == '3':
            cls()
            print('Opening Download in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab('https://nl.malwarebytes.com/mwb-download/')
            prsenter = input('press enter to choose another option...')
            startmenu()

        elif utilchoise == '4':
            cls()
            print('Opening Download in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab('https://code.visualstudio.com/download')
            prsenter = input('press enter to choose another option...')
            startmenu()


    elif MainOptChoise == '5' :
        cls()
        print('Opening downloads in 3 sec...')
        time.sleep (3)
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 1))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 2))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 3))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 4))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 5))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 6))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 7))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 8))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 9))
        webbrowser.open_new_tab(linecache.getline('overclocking_config.txt', 10))
        prsenter = input('press enter to choose another option...')
        startmenu()

    
    elif MainOptChoise == '6' :
        cls()
        print('Choose your browser: \n\n\n')
        print('[1] Any chromium based browser')
        print('[2] Firefox (tor)')
        ExtOpt = input()

        if ExtOpt == '1':
            cls()
            print('Opening downloads in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 1))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 2))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 3))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 4))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 5))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 6))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 7))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 8))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 9))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_chromium_config.txt', 10))
            
            prsenter = input('press enter to choose another option...')
            startmenu()

        elif ExtOpt == '2':
            cls()
            print('Opening downloads in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 1))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 2))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 3))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 4))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 5))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 6))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 7))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 8))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 9))
            webbrowser.open_new_tab(linecache.getline('usefull_extensions_firefox_config.txt', 10))
            
            prsenter = input('press enter to choose another option...')
            startmenu()


        



        prsenter = input('press enter to choose another option...')
        startmenu()
    
    
    
    
    
    
    
    
    
    elif MainOptChoise == '9' :
        cls()
        print('Opening my site in 3 sec...')
        time.sleep (3)
        webbrowser.open_new_tab('https://sites.google.com/view/district14/homepage')
        prsenter = input('press enter to choose another option...')
        startmenu()



        prsenter = input('press enter to choose another option...')
        startmenu()


        
#calls main function      
        

print('made by me :)')

time.sleep (1)
cls()
startmenu()
        

