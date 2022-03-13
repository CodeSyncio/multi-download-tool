#imports all required functions

import os          
import time
import webbrowser
import linecache

#function to clear the console (windows based operating system = "cls", linux based operating systems = "clear")

def cls():                                         
    os.system('cls' if os.name=='nt' else 'clear')     








#function to kill your browser windows after opening a different category (to avoid big RAM usage)

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


#defining of main program function starts here

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
        
        
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 1))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 2))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 3))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 4))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 5))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 6))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 7))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 8))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 9))
        webbrowser.open_new_tab(linecache.getline('config_blank.txt', 10))
        




        prsenter = input('press enter to choose another option...')
        startmenu()
    elif MainOptChoise == '2' :      
        
        cls()
        print('Opening Downloads in 3 sec...')
        time.sleep (3)
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 1))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 2))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 3))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 4))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 5))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 6))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 7))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 8))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 9))
        webbrowser.open_new_tab(linecache.getline('config_games.txt', 10))
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
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 1))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 2))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 3))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 4))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 5))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 6))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 7))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 8))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 9))
        webbrowser.open_new_tab(linecache.getline('config_overclocking.txt', 10))
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
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 1))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 2))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 3))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 4))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 5))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 6))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 7))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 8))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 9))
            webbrowser.open_new_tab(linecache.getline('config_crome_extensions.txt', 10))
            
            prsenter = input('press enter to choose another option...')
            startmenu()

        elif ExtOpt == '2':
            cls()
            print('Opening downloads in 3 sec...')
            time.sleep (3)
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 1))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 2))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 3))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 4))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 5))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 6))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 7))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 8))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 9))
            webbrowser.open_new_tab(linecache.getline('config_firefox_extensions.txt', 10))
            
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
        

