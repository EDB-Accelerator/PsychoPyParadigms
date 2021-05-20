import psychopy.event
import psychopy.misc
from psychopy import visual

win = visual.Window(
    size=[1024, 768],
    units="pix",
    fullscr=False,
    color='white'
)

circle = visual.Circle(win=win, units="pix", fillColor='black', lineColor='white', edges=1000, pos=(0, 0),
                       radius=10)
# 'test' circles
circle.radius = 30

rectangle = visual.Rect(win=win,units="pix",width=1000,height=1000,pos=(0,0),fillColor='black')

test_offset = 100

circle.draw()
rectangle.draw()
win.flip()


win.flip()

win.getMovieFrame()
psychopy.event.waitKeys()

win.close()