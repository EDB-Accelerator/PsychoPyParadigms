from psychopy import visual,event,core
import time

def DisplayFixationCross(df,win,bold):

    #Initialization
    fCS = 0.1 # size (for brevity)
    fCP = [0,0] # position (for brevity)

    if bold is 'Horizontal':
        fixation1 = visual.ShapeStim(win, lineColor='#000000', lineWidth=3.0, vertices=(
        (fCP[0], fCP[1]), (fCP[0], fCP[1] + fCS / 2), (fCP[0], fCP[1] - fCS / 2)), units='height', closeShape=False,
                                     name='fixCross');
        fixation1.draw()
        fixation2 = visual.ShapeStim(win, lineColor='#000000', lineWidth=10.0,
                                     vertices=((fCP[0] - fCS / 2, fCP[1]), (fCP[0] + fCS / 2, fCP[1])), units='height',
                                     closeShape=False, name='fixCross');
        fixation2.draw()
    elif bold is 'Vertical':
        fixation1 = visual.ShapeStim(win, lineColor='#000000', lineWidth=10.0, vertices=(
        (fCP[0], fCP[1]), (fCP[0], fCP[1] + fCS / 2), (fCP[0], fCP[1] - fCS / 2)), units='height', closeShape=False,
                                     name='fixCross');
        fixation1.draw()
        fixation2 = visual.ShapeStim(win, lineColor='#000000', lineWidth=3.0,
                                     vertices=((fCP[0] - fCS / 2, fCP[1]), (fCP[0] + fCS / 2, fCP[1])), units='height',
                                     closeShape=False, name='fixCross');
        fixation2.draw()
    else:
        fixation = visual.ShapeStim(win, lineColor='#000000', lineWidth=3.0, vertices=(
        (fCP[0] - fCS / 2, fCP[1]), (fCP[0] + fCS / 2, fCP[1]), (fCP[0], fCP[1]), (fCP[0], fCP[1] + fCS / 2),
        (fCP[0], fCP[1] - fCS / 2)), units='height', closeShape=False, name='fixCross')
        fixation.draw()

    # Flip Window (display FixationCross image)
    win.flip()

    # Show scale and measure the elapsed wall-clock time.
    keys = []
    startTime = endTime = time.time()
    while (endTime - startTime < 10) and keys != ['1'] and keys != ['2']:
        keys = event.getKeys()
        endTime = time.time()
        core.wait(1 / 200)
        print(keys)
