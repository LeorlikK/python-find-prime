import pyautogui
import pywinauto
from time import  sleep
import re
import os
import shutil
import psutil
import datetime
from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials


'''Открытие папки куда будут заносится акаунты'''
sleep(2)
try:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'C:/Users/Aboost/Desktop/Prime/BOT_PRIME(AKK)/')
    shutil.rmtree(path)
    os.mkdir('C:/Users/Aboost/Desktop/Prime/BOT_PRIME(AKK)/')
    sleep(3)
    with open('C:/Users/Aboost/Desktop/Prime/BOT_PRIME(AKK)/1.txt', 'w') as tw:
        tw.write(str(''))
except:
    os.mkdir('C:/Users/Aboost/Desktop/Prime/BOT_PRIME(AKK)/')
    with open('C:/Users/Aboost/Desktop/Prime/BOT_PRIME(AKK)/1.txt', 'w') as tw:
        tw.write(str(''))
sleep(1)
'''Удаление и создание текстовика с логами'''
with open('C:/Users/Aboost/Desktop/Prime/BOT_PRIME/Logs.txt', 'w') as tw:
    tw.write(str(''))
'''Открытие текстовика с номерами пачки которые нужно прогнать'''
infile3 = 'C:/Users/Aboost/Desktop/Prime/BOT_PRIME/AKKI.txt'
file3 = open(infile3, mode='r', encoding='utf_8')
akki = []
znachenie = 0
for x in file3:
    akki.append(x)
for hiks in akki:
    '''Открытие панели'''
    infile1 = 'C:/Users/Aboost/Desktop/Prime/BOT_PRIME(AKK)/1.txt'
    file1 = open(infile1, mode='a', encoding='utf_8')
    k = int(hiks)
    os.startfile(r'C:\Users\Aboost\Desktop\CSGO Booster')
    sleep(15)
    x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname2.png')
    pyautogui.click(x, y)
    sleep(2)
    x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname3.png')
    pyautogui.click(x, y)
    sleep(2)
    x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname4.png')
    pyautogui.click(x, y)
    sleep(2)
    m = str(k)
    pyautogui.typewrite(m, interval=0.25)
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname5.png')
    pyautogui.click(x, y)
    sleep(1)
    x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname6.png')
    pyautogui.click(x, y)
    sleep(1)
    pyautogui.click(940, 743)
    sleep(30)
    '''Проверка на загрузку'''
    for hhh in range(10):
        print(hhh)
        try:
            xam, yam = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname11.png')
            break
        except:
            sleep(20)
    if hhh >= 9:
        now = datetime.datetime.now()
        '''Открытие текстовика с логами'''
        infile8 = 'C:/Users/Aboost/Desktop/Prime/BOT_PRIME/Logs.txt'
        file8 = open(infile8, mode='a', encoding='utf_8')
        sleep(1)
        file8.write(m + ' - ' + str(now) + '\n')
        sleep(1)
        file1.close()
        sleep(1)
        file8.close()
        x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname9.png')
        pyautogui.click(x, y)
        sleep(10)
        x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname10.png')
        pyautogui.click(x, y)
        sleep(1)
        continue
    '''Выборка акаунта,поиск окна с ним'''
    sleep(15)
    f = []
    notepads = [item for item in psutil.process_iter() if item.name() == 'csgo.exe']
    print(psutil.process_iter())
    print(notepads)
    f.append(notepads)
    text = r'pid\=\d+'
    text2 = r'\d+'
    v = str(f)
    i = re.findall(text,v)
    i = re.findall(text2,str(i))
    b = i
    l = 0
    for xxx in range(10):
        g = b[l]
        g = int(g)
        app = pywinauto.Application().connect(process=g)
        app.snxhk_border_mywnd.set_focus().click_input()
        t = pyautogui.getActiveWindow()
        l = l + 1
        sleep(1)
        def add_akk():
            sleep(1)
            text3 = r'@ LOGIN:\s\S+'
            fff = re.search(text3, str(t))
            q = re.split("\s", str(fff))
            print(q[6])
            q = q[6]
            q = q[:-2]
            q = (str(q) + '\n')
            file1.write(q)
        def rgb21():
            try:
                crgb21 = pyautogui.pixelMatchesColor(344, 55, (0, 0, 164))
                if str(crgb21) == 'True':
                    add_akk()
                    sleep(1)
                if str(crgb21) == 'False':
                    rgb22()
            except:
                rgb21()
        def rgb22():
            try:
                crgb22 = pyautogui.pixelMatchesColor(344, 55, (6, 6, 162))
                if str(crgb22) == 'True':
                    add_akk()
                    sleep(1)
                if str(crgb22) == 'False':
                    rgb23()
            except:
                rgb22()
        def rgb23():
            try:
                crgb23 = pyautogui.pixelMatchesColor(343, 53, (32, 36, 175))
                if str(crgb23) == 'True':
                    add_akk()
                    sleep(1)
                if str(crgb23) == 'False':
                    rgb24()
            except:
                rgb23()
        def rgb24():
            try:
                crgb24 = pyautogui.pixelMatchesColor(345, 53, (23, 25, 170))
                if str(crgb24) == 'True':
                    add_akk()
                    sleep(1)
                if str(crgb24) == 'False':
                    rgb25()
            except:
                rgb24()
        def rgb25():
            try:
                crgb25 = pyautogui.pixelMatchesColor(344, 53, (35, 37, 171))
                if str(crgb25) == 'True':
                    add_akk()
                    sleep(1)
                if str(crgb25) == 'False':
                    pass
            except:
                rgb25()
        for _ in range(1):
            rgb21()
        sleep(1)
    sleep(1)
    x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname9.png')
    pyautogui.click(x, y)
    sleep(5)
    pyautogui.click(x, y)
    sleep(5)
    x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Aboost\Desktop\Prime\BOT_PRIME\Unname10.png')
    pyautogui.click(x, y)
    file1.close()
    sleep(1)
    '''Подключение к таблице'''
    #pyautogui.confirm(text='Добавить аккаунты в таблицу?', title='Подключение к таблице', buttons=['Да', 'Нет'])
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("MOY.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open('Aboost1').get_worksheet(0)
    infile5 = 'C:/Users/Aboost/Desktop/Prime/BOT_PRIME(AKK)/1.txt'
    file5 = open(infile1, mode='r', encoding='utf_8')
    ghik = []
    for collapse in file5:
        ghik.append(collapse)
    for _ in ghik:
        try:
            collapse = ghik[znachenie]
            collapse = collapse[:-1]
            znachenie = znachenie + 1
            print(collapse)
        except:
            break
        try:
            cell = sheet.find(collapse)
            cell = cell.row
            b = ('B' + str(cell))
            sheet.format(b, {
                "backgroundColor": {
                    "red": 0.0,
                    "green": 1,
                    "blue": 0.0
                }})
            sleep(10)
        except:
            pass
    file5.close()
    sleep(1)
file1.close()
sleep(1)
file3.close()
sleep(1)
file8.close()

# '''Подключение к таблице'''
# pyautogui.confirm(text='Добавить аккаунты в таблицу?', title='Подключение к таблице', buttons=['Да', 'Нет'])
# scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name("MOY.json", scope)
# client = gspread.authorize(creds)
# sheet = client.open('Aboost1').get_worksheet(0)
# infile1 = 'C:/Users/Aboost/Desktop/Prime/BOT_PRIME(AKK)/1.txt'
# file1 = open(infile1, mode='r', encoding='utf_8')
# for collapse[] in file1:
#     collapse = collapse[:-1]
#     print(collapse)
#     cell = sheet.find(collapse)
#     cell = cell.row
#     b = ('B' + str(cell))
#     sheet.format(b, {
#         "backgroundColor": {
#             "red": 0.0,
#             "green": 1,
#             "blue": 0.0
#         }})