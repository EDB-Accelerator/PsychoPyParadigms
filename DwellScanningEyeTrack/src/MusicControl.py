import os

def PauseMusic():
    if os.path.isfile('a') == False:
        open('a', 'a').close()
        if os.path.isfile('b'):
            os.remove('b')
        if os.path.isfile('c'):
            os.remove('c')

def UnpauseMusic():
    if os.path.isfile('b') == False:
        open('b', 'a').close()
        if  os.path.isfile('a'):
            os.remove('a')
        if  os.path.isfile('c'):
            os.remove('c')
def StopMusic():
    if os.path.isfile('c') == False:
        open('c', 'a').close()
        if  os.path.isfile('a'):
            os.remove('a')
        if  os.path.isfile('b'):
            os.remove('b')

