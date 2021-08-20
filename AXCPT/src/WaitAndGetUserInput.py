def WaitAndGetUserInput(c,waitTime):
    import time
    from psychopy import event, core
    import datetime

    startTime = time.time()
    responseTime = ""
    c = []
    while time.time()-startTime < waitTime:
        if c == []:
            c = event.getKeys()
            responseTime = datetime.datetime.now()

            if c == ['q'] or c == ['Q']:
                print('Q pressed. Forced Exit.')
                core.quit()
            # print(c)
        core.wait(1/120)

    if c == []:
        responseTime = ""
        c = ""
    else:
        try:
            c = c[0].upper()
        except:
            pass

    return c,responseTime

def WaitUserSpace():
    from psychopy import core, event
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character
        # print(c)

        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()
