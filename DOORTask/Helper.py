from psychopy import core, visual, event

def displayVAS(win,text,labels):
    scale = visual.RatingScale(win,
                               labels=labels,  # End points
                               scale=None,  # Suppress default
                               low=1, high=30, tickHeight=0, markerStart=15, precision=1)  # markerstart=50
    myItem = visual.TextStim(win, text=text, height=.12, units='norm',wrapWidth=2)
    # Show scale
    while scale.noResponse:
        scale.draw()
        myItem.draw()
        win.flip()
    win.flip()
    return scale.getRating()

def showImage(win,image,opacity,size):

    if size==None:
        img1 = visual.ImageStim(win=win,image=image,units="pix",opacity=opacity,)
    else:
        img2 = visual.ImageStim(win=win,image=image,units="pix",opacity=opacity,size=size,
        )

    img1.draw()
    img2.draw()
    win.flip()

def showImage(win,image,opacity,size):

    if size==None:
        img = visual.ImageStim(win=win,image=image,units="pix",opacity=opacity,)
    else:
        img = visual.ImageStim(win=win,image=image,units="pix",opacity=opacity,size=size,
        )

    img.draw()
    win.flip()

def overlapImage(win,image,opacity,size):

    if size==None:
        img = visual.ImageStim(win=win,image=image,units="pix",opacity=opacity,overlaps=True)
    else:
        img = visual.ImageStim(win=win,image=image,units="pix",opacity=opacity,size=size,overlaps=True
        )

    img.draw()
    win.flip()

def fadeInOutImage(win,image,duration,size):
    for i in range(60):
        opacity = 1 / 60 * (i+1)
        showImage(win,image, opacity,size)
        core.wait(duration/60)

    for i in range(60):
        opacity = 1 - 1 / 60 * (i+1)
        showImage(win,image, opacity,size)
        core.wait(duration/60)

def displayText(win,textString):
    message = visual.TextStim(win, text=textString, wrapWidth=2)
    message.draw()
    win.flip()
