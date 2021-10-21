#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo of psychopy.visual.ShapeStim: lines and arbitrary fillable shapes
See shapeContains.py for dynamic interaction of ShapeStim and Mouse.
"""

from __future__ import division

from psychopy import visual, event, core
from psychopy.visual import ShapeStim

# win = visual.Window(size=(1920, 1080), units='height')
win = visual.Window(size=(1024, 768), units='height')

r = 1000
arrowLeft = [(-0.2 * r, 0.05 * r), (-0.2 * r, -0.05 * r), (0, -0.05 * r), (0, -0.1 * r), (0.2 * r, 0), (0, 0.1 * r),
             (0, 0.05 * r)]
arrowRight = [(0.2 * r, 0.05 * r), (0.2 * r, -0.05 * r), (0, -0.05 * r), (0, -0.1 * r), (-0.2 * r, 0), (0, 0.1 * r),
              (0, 0.05 * r)]
arrowLine = [(-0.2 * r, 0.05 * r), (-0.2 * r, -0.05 * r), (.2 * r, -.05 * r), (.2 * r, 0.05 * r)]

arrowR = ShapeStim(win, vertices=arrowRight, units='pix', fillColor='black', size=.5, lineColor='black',
                   pos=[0, .1 * r])
arrowL = ShapeStim(win, vertices=arrowLeft, units='pix', fillColor='black', size=.5, lineColor='black',
                   pos=[-0.3 * r, .1 * r])
arrowLine = ShapeStim(win, vertices=arrowLine, units='pix', fillColor='black', size=.5, lineColor='black',
                      pos=[0.3 * r, .1 * r])

messageR = visual.TextStim(win, text="Press the right\nbutton",
                           units='pix', wrapWidth=400, color="black", pos=[-0.3 * r, -.06 * r], height=30)
messageL = visual.TextStim(win, text="Press the left\nbutton",
                           units='pix', wrapWidth=200, color="black", pos=[0 * r, -.06 * r], height=30)
messageC = visual.TextStim(win, text="Do not press a \nbutton",
                           units='pix', wrapWidth=200, color="black", pos=[0.3 * r, -.06 * r], height=30)
message = visual.TextStim(win,text="Press space bar to proceed.",units='pix', wrapWidth=1000, color='black',pos=[0,-200],height=40)
while not event.getKeys():
    arrowL.draw()
    arrowR.draw()
    arrowLine.draw()
    messageR.draw()
    messageL.draw()
    messageC.draw()
    message.draw()
    win.flip()

win.close()
core.quit()