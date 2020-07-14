from psychopy import core, visual, event
import time
import pandas as pd

def tableWrite(Df,Dict):
    # Move data in Dict into Df.
    Df = Df.append(pd.Series(dtype=float), ignore_index=True) #Insert Empty Rows
    for key in Dict:
        Df[key].loc[len(Df)-1] = Dict[key] # FYI, len(Df)-1: means the last row of pandas dataframe.
    return Df

def displayVAS(win,text,labels):
    scale = visual.RatingScale(win,
                               labels=labels,  # End points
                               scale=None,  # Suppress default
                               low=1, high=30, tickHeight=0, markerStart=15, precision=1)  # markerstart=50
    myItem = visual.TextStim(win, text=text, height=.12, units='norm',wrapWidth=2)
    # Show scale and measure the elapsed wall-clock time.
    startTime = time.time()
    while scale.noResponse:
        scale.draw()
        myItem.draw()
        win.flip()
    endTime = time.time()
    win.flip()
    return scale.getRating(),endTime-startTime

def displayInstruction(win):
    message = visual.TextStim(win, text="Do you want to see the instruction? (y: Yes, n: No)")
    message.draw();
    win.flip();
    c = ['']
    # Wait for user types "y" or "n".
    while(c[0].upper() != "Y" and c[0].upper() != "N"):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

    # If user types "y", run instruction.
    if c[0].upper() == "Y":
        c = ['R']
        while(c[0].upper() == "R"):
            core.wait(1 / 120)
            for i in range(1,17):
                imgFile = "./instruction/Slide" + str(i) + ".JPG"
                img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(1200, 800))
                img1.draw();win.flip();
                c = event.waitKeys()

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
