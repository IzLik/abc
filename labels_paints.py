from tqdm import trange
from time import sleep
from turtle import *

def logo():
    print(' '*50,' ▀█▀ ░█▀▀█ 　 ▀▀█▀▀ ░█▀▀▀ ░█▀▀▀█ ▀▀█▀▀') 
    print(' '*50,' ░█─ ░█─░█ 　 ─░█── ░█▀▀▀ ─▀▀▀▄▄ ─░█──')
    print(' '*50,' ▄█▄ ─▀▀█▄ 　 ─░█── ░█▄▄▄ ░█▄▄▄█ ─░█──')
    print(' '*70,'by  ɴᴇᴜʀᴏᴘʀᴏɢʀᴀᴍᴍᴇʀs')

def loading():
    print('Загрузка...\n')
    for i in trange(100):
        sleep(0.05)
    sleep(1)
    print('\nЗагрузка завершена!')
    sleep(1)
    
def loading_line():
    z = 1
    s = 110
    analis = ''
    for p in range(2):
        for q in range(56):
            print('-' * z, ' * ', '-' * s, ' .', '-' * z)
            z += 1
            s -= 2
            sleep(0.01)
        print(' ' * (z - 4), analis)
        for q in range(56):
            z -= 1
            s += 2
            print('-' * z, ' . ', '-' * s, ' *', '-' * z)
            sleep(0.01)
        analis = 'Завершение работы'
