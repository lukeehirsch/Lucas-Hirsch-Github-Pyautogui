from pyautogui import *
import pyautogui as pg
from time import sleep

pg.FAILSAFE = True
pg.PAUSE = 0.7

if pg.confirm(text='Do we need to open set up?(Axie Marketplace and Google sheets)', title='Claim Bot', buttons=['YES', 'NO']) =='YES':   
    pg.press('winleft')
    pg.write('chrome')
    sleep(0.5)
    pg.press('enter')
    sleep(0.5)
    pg.hotkey('winleft', 'up')
    pg.write('https://marketplace.axieinfinity.com/profile/dashboard/')
    pg.press('enter')
    pg.hotkey('ctrl','t')
    pg.write('EXAMPLE GOOGLE SHEETS PAGE')
    pg.press('enter')
    pg.hotkey('ctrl', '1')
    sleep(3)
    
#DESLOG
pg.click(66,1021)
pg.moveTo(pg.locateCenterOnScreen('logout.png', confidence=0.8))
pg.click()

loggeado = ''
loggeado = pg.confirm(text='Remember to be logged to Ronin', title='Claim Bot', buttons=['Done', 'Cancel'])
sleep(1)
if loggeado == 'Cancel':
    exit()
if loggeado == 'Done':
    time.sleep(1)
    account = ''
    account = pg.prompt(text='Which account should we claim?', title='Claim Bot' , default='options')
    if account == 'options':
        sleep(0.5)
        pg.alert(text='1, 2, 3, 4')
    account = pg.prompt(text='Which account should we claim?', title='Claim Bot' , default='')
        
    if account == '1':
        sleep(1)
        pg.moveTo(pg.locateCenterOnScreen('roninext.png', confidence=0.8))
        pg.click()
        sleep(2)
        pg.moveRel(-25,50)
        pg.click()
        sleep(1)
        pg.moveTo(1476, 238)            #POSITION 1
        pg.click()
        pg.moveTo(pg.locateCenterOnScreen('logout.png', confidence=0.8))
        pg.click()
        pg.moveTo(pg.locateCenterOnScreen('loginronin.png', confidence=0.8))
        pg.click()
        pg.moveTo(1700, 400)
        sleep(1)
        pg.scroll(-100)
        pg.moveTo(pg.locateCenterOnScreen('roninconfirm.png', confidence=0.8))
        pg.click()
        sleep(4)

    if account == '2':
        sleep(1)
        pg.moveTo(pg.locateCenterOnScreen('roninext.png', confidence=0.8))
        pg.click()
        sleep(2)
        pg.moveRel(-25,50)
        pg.click()
        sleep(1)
        pg.moveTo(1476, 312)            #POSITION 2
        pg.click()
        pg.moveTo(pg.locateCenterOnScreen('logout.png', confidence=0.8))
        pg.click()
        pg.moveTo(pg.locateCenterOnScreen('loginronin.png', confidence=0.8))
        pg.click()
        pg.moveTo(1700, 400)
        sleep(1)
        pg.scroll(-100)
        pg.moveTo(pg.locateCenterOnScreen('roninconfirm.png', confidence=0.8))
        pg.click()
        sleep(4)        

    if account == '3':
        sleep(1)
        pg.moveTo(pg.locateCenterOnScreen('roninext.png', confidence=0.8))
        pg.click()
        sleep(2)
        pg.moveRel(-25,50)
        pg.click()
        sleep(1)
        pg.moveTo(1476, 384)            #POSITION 3
        pg.click()
##        pg.moveTo(pg.locateCenterOnScreen('logout.png', confidence=0.8))
##        pg.click()
        pg.moveTo(pg.locateCenterOnScreen('loginronin.png', confidence=0.8))
        pg.click()
        pg.moveTo(1700, 400)
        sleep(1)
        pg.scroll(-100)
        pg.moveTo(pg.locateCenterOnScreen('roninconfirm.png', confidence=0.8))
        pg.click()
        sleep(4)
        
    
##START CLAIM
pg.moveTo(pg.locateCenterOnScreen('claimtokens.png', confidence=0.8))
pg.click()
pg.hotkey('ctrl','t')
pg.write('https://scatter.roninchain.com/')
pg.press('enter')
sleep(2)
pg.hotkey('ctrl','1')
sleep(1.5)
pg.press('f5')
time.sleep(3)
pg.moveTo(pg.locateCenterOnScreen('claimable.png', confidence=0.8))
pg.move(31,0)           ##relative
pg.doubleClick()
pg.hotkey('ctrl','c')
sleep(1)
pg.moveTo(pg.locateCenterOnScreen('claimslp.png', confidence=0.8))
sleep(5)

pg.hotkey('ctrl','2')
time.sleep(1)
pg.moveTo(38, 220)
pg.click()
if account == '1':
    pg.write('B2')
if account == '2':
    pg.write('B3')
if account == '3':
    pg.write('B4')
if account == '4':
    pg.write('B5')
sleep(0.5)
pg.press('enter')
pg.hotkey('ctrl','v')
time.sleep(1)
#####################################################################################
pg.press('right')
pg.press('right')
pg.hotkey('ctrl','c')   #copyroninsch
pg.hotkey('ctrl','3')
time.sleep(0.5)
pg.moveTo(934, 341)
pg.click()
pg.moveTo(934, 520)
pg.click()
pg.moveTo(950, 480)
pg.click()
pg.hotkey('ctrl','v')   #pasteronin
pg.write(' ')
pg.hotkey('ctrl','2')
pg.press('left')
pg.hotkey('ctrl','c')   #copyslp
pg.hotkey('ctrl','3')
pg.hotkey('ctrl','v')   #pasteslp
pg.press('enter')
pg.hotkey('ctrl','2')
pg.press('right')
pg.press('right')
pg.press('right')
pg.hotkey('ctrl','c')   #copyroninmanager
pg.hotkey('ctrl','3')
pg.hotkey('ctrl','v')   #pasteronin
pg.write(' ')
pg.hotkey('ctrl','2')
pg.press('left')
pg.hotkey('ctrl','c')   #copyslp
pg.hotkey('ctrl','3')
pg.hotkey('ctrl','v')   #pasteslp
pg.moveTo(pg.locateCenterOnScreen('approveslp.png', confidence=0.8))
pg.click()
pg.moveTo(1700, 400)
sleep(1)
pg.scroll(-100)
pg.moveTo(pg.locateCenterOnScreen('roninconfirm.png', confidence=0.8))
pg.click()
sleep(4)





exit()
