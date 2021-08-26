import pymem, pymem.process, requests, keyboard, time
from threading import Thread
from math import sqrt, pi, atan
from time import sleep
import os
import pymem, pymem.process, requests, sys
from threading import Thread
from math import sqrt, pi, atan
from win32gui import GetWindowText, GetForegroundWindow
import pyautogui as pg
from time import sleep
import keyboard
import os
from time import time
import pymem, time, requests
import pymem.process
from threading import Thread

def bunner1():
	print('''
		  __________
	                      .~#########%%;~.
	                     /############%%;`\
	                    /######/~\/~\%%;,;,\
	                   |#######\    /;;;;.,.|
	                   |#########\/%;;;;;.,.|
	          XX       |##/~~\####%;;;/~~\;,|       XX
	        XX..X      |#|  o  \##%;/  o  |.|      X..XX
	      XX.....X     |##\____/##%;\____/.,|     X.....XX
	 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
	X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
	X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
	X  \...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx
	 X# \.X        @#%,.@                 @#%,.@
	                @#%,.@              @#%,.@
	                  @#%,.@          @#%,.@
	                     @#%,.@      @#%,.@
	                       @#%.,@  @#%,.@
	''')

def bunner2():
	print('''
_____________________________________________________________________      
            ___           _,.---,---.,_                                    
            |         ,;~'             '~;,                                
            |       ,;                     ;,                              
   Frontal  |      ;                        ; ,--- Supraorbital Foramen    
    Bone    |     ,'                        /'                             
            |    ,;                       /' ;,                            
            |    ; ;      .          . <-'  ; |                            
            |__  | ;   ______       ______   ;<----- Coronal Suture        
           ___   |  '/~ ~ . ~ ~\'  |                                       
           |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |                           
 Maxilla,  |      |   |        }:{        | <------ Orbit                  
Nasal and  |      |   l       / | \       !   |                            
Zygomatic  |      .~  (__,.-- .^. --.,__)  ~.                              
  Bones    |      |    ----;' / | \  ;-<--------- Infraorbital Foramen     
           |__     \__.       \/^\/       .__                              
              ___   V| \                 / |V <--- Mastoid Process         
              |      | |T~\___!___!___/~T| |                               
              |      | | IIII_I_I_I_IIII | |                               
     Mandible |      |  \ III I I I III,/  |                               
              |       \    ~~~~~~~~~~                                      
              |         \   .       . <-x---- Mental Foramen               
              |__         \.    ^    .                                     
                            ^~~~^~~~^                                      
  _________________________________________________________________
''')

def bunner3():
	print('''	           ...
                 ;::::;   
               ;::::; :;    
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO
           ::::::;       ;          OOOOO
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#
       ''')

print("1. Bhop")
print("2. No Flash")
print("3. WH")
print("4. FLUD")

con = input("--> ")

if con == "1":
	url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
	response = requests.get(url).json()

	dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
	dwForceJump = int(response["signatures"]["dwForceJump"])

	m_fFlags = int(response["netvars"]["m_fFlags"])

	pm = pymem.Pymem("csgo.exe")
	client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
	os.system("cls")
	print('''STARTING: WH
	   ''')
	bunner1()
	    
	def buny():
	    while True:
	        if pm.read_int(client + dwLocalPlayer):
	            player = pm.read_int(client + dwLocalPlayer)
	            force_jump = client + dwForceJump
	            on_ground = pm.read_int(player + m_fFlags)

	            if keyboard.is_pressed("space"):
	                if on_ground == 257:
	                    pm.write_int(force_jump, 5)
	                    time.sleep(0.17)
	                    pm.write_int(force_jump, 4)
	            
	buny()

elif con == "2":
	offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
	response = requests.get(offsets).json()

	dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
	m_flFlashMaxAlpha = int(response["netvars"]["m_flFlashMaxAlpha"])

	try:
		pm = pymem.Pymem("csgo.exe")
		client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
		os.system("cls")
		print('''STARTING: No Flash
	    ''')
		bunner2()
	except:
		ctypes.windll.user32.MessageBoxW (None, 'Не удалось получить доступ к процессу - csgo.exe.', 'Сбой', 0)
		sys.exit()

	def NoFlash():
	    while True:
	        player = pm.read_int(client + dwLocalPlayer)
	        if player:
	            flash_value = player + m_flFlashMaxAlpha
	            if flash_value:
	                pm.write_float(flash_value, float(0))
	        time.sleep(1)


	Thread(target=NoFlash).start()

elif con == "3":
	url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
	response = requests.get(url).json()

	dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
	dwEntityList = int(response["signatures"]["dwEntityList"])
	dwGlowObjectManager = int(response["signatures"]["dwGlowObjectManager"])


	m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
	m_bSpottedByMask = int(response["netvars"]["m_bSpottedByMask"])
	m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])

	try:
		pm = pymem.Pymem("csgo.exe")
		client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
		os.system("cls")
		print('''STARTING: WH
	    ''')
		bunner3()
	except:
		ctypes.windll.user32.MessageBoxW (None, 'Не удалось получить доступ к процессу - csgo.exe.', 'Сбой', 0)
		sys.exit()

	GS = 0

	def GlowESP():
	    while True:
	        if pm.read_int(client + dwLocalPlayer):
	            localplayer = pm.read_int(client + dwLocalPlayer)
	            localplayer_team = pm.read_int(localplayer + m_iTeamNum)
	            localplayer_index = pm.read_int(localplayer + 0x64) - 1
	            for x in range(64):
	                if pm.read_int(client + dwEntityList + x * 0x10):
	                    entity = pm.read_int(client + dwEntityList + x * 0x10)
	                    spotted = pm.read_int(entity + m_bSpottedByMask)
	                    entity_team = pm.read_int(entity + m_iTeamNum)
	                    glow_manager = pm.read_int(client + dwGlowObjectManager)
	                    entity_glow = pm.read_int(m_iGlowIndex + entity)

	                    if entity and entity_team != localplayer_team:
	                        if spotted == 1 << localplayer_index:
	                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(3))  # R
	                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))  # G
	                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(2.5))  # B
	                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
	                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)
	                        else:
	                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))  # G
	                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))  # B
	                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
	                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)
	                            
	Thread(target=GlowESP).start()

elif con == "4":
	os.system("cls")
	print('''STARTING: Flud
	    ''')
	bnner()
	print("1. ???WHAT???")
	print("2. ???WHY???")
	print("3. HAHAHAHAHA")
	print("4. FLUD")
	print("5. 1")
	print("6. FULL")

	a = "1"
	b = "2"
	d = "3"
	e = "4"
	f = "5"
	g = "6"

	spam = input('--> ')

	if spam == a:
		os.system("cls")
		print('''        _       _             _      ____  _             _   _             
	       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
	      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
	     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
	    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |.....
	                                                                     |___/ ''')
		while True:
			os.system("color 1")
			pg.typewrite( '???WHAT???' )
			pg.typewrite(["enter"])

	elif spam == b:
		os.system("cls")
		print('''        _       _             _      ____  _             _   _             
	       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
	      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
	     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
	    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |.....
	                                                                     |___/ ''')
		while True:
			os.system("color 4")
			pg.typewrite( '???WHY???' )
			pg.typewrite(["enter"])

	elif spam == d:
		os.system("cls")
		print('''        _       _             _      ____  _             _   _             
	       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
	      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
	     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
	    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |.....
	                                                                     |___/ ''')
		while True:
			os.system("color 2")
			pg.typewrite( 'HAHAHAHAHA' )
			pg.typewrite(["enter"])

	elif spam == e:
		os.system("cls")
		print('''        _       _             _      ____  _             _   _             
	       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
	      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
	     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
	    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |.....
	                                                                     |___/ ''')
		while True:
			os.system("color 6")
			pg.typewrite( 'FLUD' )
			pg.typewrite(["enter"])

	elif spam == f:
		os.system("cls")
		print('''        _       _             _      ____  _             _   _             
	       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
	      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
	     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
	    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |.....
	                                                                     |___/ ''')
		while True:
			os.system("color 9")
			pg.typewrite( '1' )
			pg.typewrite(["enter"])

	elif spam == g:
		os.system("cls")
		print('''        _       _             _      ____  _             _   _             
	       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
	      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
	     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
	    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |.....
	                                                                     |___/ ''')
		while True:
			os.system("cls")
			os.system("color 8")
			pg.typewrite( 'WHAT???' )
			pg.typewrite(["enter"])
			pg.typewrite( 'WHY???' )
			pg.typewrite(["enter"])
			pg.typewrite( 'HAHAHAHHA' )
			pg.typewrite(["enter"])
			pg.typewrite( 'FLUD' )
			pg.typewrite(["enter"])
			pg.typewrite( '1' )
			pg.typewrite(["enter"])

	elif spam == "7":
		os.system("cls")
		print('''        _       _             _      ____  _             _   _             
	       / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
	      / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
	     / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
	    /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |.....
	                                                                     |___/ ''')
		while True:
			pg.typewrite( '🌭🍔🍕' )
			pg.typewrite(["enter"])