import psychopy.event
import psychopy.misc
from psychopy import visual

win = visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

circle = visual.Circle(win=win,units="pix",fillColor=[-1] * 3,lineColor=[-1] * 3,edges=128,pos = [0,0])

# 'test' circles
circle.radius = 12

test_offset = 100



circle.draw()


win.flip()

win.getMovieFrame()
psychopy.event.waitKeys()

win.close()