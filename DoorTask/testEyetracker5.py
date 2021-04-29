from psychopy import visual, core, event,prefs

params = {
    'screenSize': (1024, 780),
}

width = params[ 'screenSize'][0]
height = params[ 'screenSize'][1]
prefs.general['fullscr'] = False
win = visual.Window(params['screenSize'], monitor="testMonitor",color="black",winType='pyglet')
img1 = visual.ImageStim(win=win, image="./img/practice/practice_door.jpg", units="pix", opacity=1, size=(params[ 'screenSize'][0], params['screenSize'][1]))

awardImg = "./img/practice/practice_outcome.jpg"
img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -height * 0.028],
                        size=(width * 0.235, height * 0.464))
img1.draw();
img2.draw();
win.flip()
win.getMovieFrame()  # Defaults to front buffer, I.e. what's on screen now.
win.saveMovieFrames('./img/practice/combined.jpg')
win.close()