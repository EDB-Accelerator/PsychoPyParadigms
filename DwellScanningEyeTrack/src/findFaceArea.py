import psychopy.event
import psychopy.misc
from psychopy import visual

resolution = [1024,768]

win = visual.Window(
    size=resolution,
    units="pix",
    fullscr=False,
    color='white'
)

img = 'img/Anger-Neutral/6N-10A/block1matrix1.jpeg'

imgStim = visual.ImageStim(win=win, image=img, units="pix", opacity=1,
                           size=(resolution[1], resolution[1]))
# imgStim.draw()
# circle = visual.Circle(win=win, units="pix", fillColor='black', lineColor='white', edges=1000, pos=(0, 0),
#                        radius=10)
#
circle = visual.Circle(win=win, units="pix", fillColor='black', lineColor='white', edges=1000, pos=(-287.5, 287.5),
                       radius=10)
# 'test' circles
# circle.radius = 30

rectangles = []
for i in range(4):
    for j in range(4):
        gap = 287.5 * 2 / 3 * resolution[1] /768
        length = 177 * resolution[1] / 768
        oPoint = 287.5 * resolution[1] /768
        rectangles.append(visual.Rect(win=win,units="pix",width=length,height=length,pos=(-oPoint+j*gap,oPoint-i*gap),fillColor='null',lineColor='red'))
        # rectangles[-1].draw()


rectangles[1].lineColor = 'black'

imgStim.draw()
for i in range(len(rectangles)):
    rectangles[i].draw()

win.flip()


win.flip()

win.getMovieFrame()
psychopy.event.waitKeys()

win.close()