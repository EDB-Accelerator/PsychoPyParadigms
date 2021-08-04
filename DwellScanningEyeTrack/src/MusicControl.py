import os

def PauseMusic():
    if os.path.isfile('.tmp/a') == False:
        open('.tmp/a', 'a').close()
        # if os.path.isfile('.tmp/b'):
        #     os.remove('.tmp/b')
        # if os.path.isfile('.tmp/c'):
        #     os.remove('.tmp/c')

def UnpauseMusic():
    if os.path.isfile('.tmp/b') == False:
        open('.tmp/b', 'a').close()
        # if  os.path.isfile('.tmp/a'):
        #     os.remove('.tmp/a')
        # if  os.path.isfile('.tmp/c'):
        #     os.remove('.tmp/c')
def StopMusic():
    if os.path.isfile('.tmp/c') == False:
        open('.tmp/c', 'a').close()
        # if  os.path.isfile('.tmp/a'):
        #     os.remove('.tmp/a')
        # if  os.path.isfile('.tmp/b'):
        #     os.remove('.tmp/b')

