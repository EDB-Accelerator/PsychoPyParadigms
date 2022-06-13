import time
from psychopy import event, core
import datetime

def WaitAndGetUserInput(c,waitTime,params):

    startTime = time.time()
    responseTime = ""
    c = []
    while time.time()-startTime < waitTime:
        if c == [] or c[0] == '5':
            c = event.getKeys()
            # if c == ['q'] or c == ['Q']:
            #     print('Q pressed. Forced Exit.')
            #     core.quit()
            # print(c)
            c = []
        # print(c)
        core.wait(1/3000)

    if c == []:
        responseTime = ""
        c = ""
    else:
        responseTime = datetime.datetime.now()
        try:
            c = c[0].upper()
        except:
            pass

    if c == params['noKey']:
        c = 'N'
    elif c == params['yesKey']:
        c = 'Y'

    return c,responseTime

# def WaitUserSpace(win):
#     # Wait for user types a space key.
#     c = ['']
#     while (c[0] != 'space'):
#         core.wait(1 / 120)
#         c = event.waitKeys()  # read a character
#
#         if c == ['q'] or c == ['Q']:
#             print('Q pressed. Forced Exit.')
#             core.quit()

def WaitUserSpace(win):
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 3000)
        c = event.waitKeys()  # read a character

        # if c == ['q'] or c == ['Q']:
        #
        #     print('Q pressed. Forced Exit.')
        #     core.quit()
