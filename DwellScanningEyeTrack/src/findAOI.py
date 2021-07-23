from psychopy.iohub import launchHubServer
from psychopy.core import getTime, wait
import pylink
from psychopy import visual, event, sound

# def newPointResolution(n,center,ratio):
#     return int((n-center) * ratio + center)

def newPointResolution(X,resolution):
    ratio = resolution[1]/768
    center = [resolution[0]/2,resolution[1]/2]

    newX = int((X[0]-512)*ratio + center[0])
    newY = int((X[1]-384)*ratio + center[1])

    return newX,newY

def pointFromCenter(n,center,standard):
    return int(center+n*(center*2)/standard)

tk = pylink.EyeLink('100.1.1.1')
dataFileName = 'test1.edf'
tk.openDataFile(dataFileName)

err = tk.startRecording(1, 1, 1, 1)
pylink.pumpDelay(100)  # wait for 100 ms to cache some samples

resolution = [1024,768]

faceLocations = []
for i in range(4):
    for j in range(4):
        x1 = 136 + 192*j
        y1 = 8 + 192*i
        x2 = 311 + 192*j
        y2 = 184 + 192*i

        x1New,y1New = newPointResolution([x1,y1],resolution)
        x2New, y2New = newPointResolution([x2,y2], resolution)

        faceLocations.append([x1New,y1New,x2New,y2New])

# MAke empty blank file
# win = visual.Window(resolution, monitor="testMonitor", color="white", winType='pyglet')
# win.getMovieFrame()  # Defaults to front buffer, I.e. what's on screen now.
# win.saveMovieFrames("img/FixationCross/blank.jpg")
# win.close()


# Fixation Cross
# tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, pointFromCenter(-70,resolution[0]/2,resolution[0]), pointFromCenter(-70,resolution[1]/2,resolution[1]), pointFromCenter(70,resolution[0]/2,resolution[0]), pointFromCenter(70,resolution[1]/2,resolution[1]), 'example_IA'))
# tk.sendMessage('!V IMGLOAD CENTER %s %d %d' % ('./img/FixationCross/Horizontal.jpg', resolution[0]/2,resolution[1]/2))

# Face
for i in range(len(faceLocations)):
    x1,y1,x2,y2= faceLocations[i][0],faceLocations[i][1],faceLocations[i][2],faceLocations[i][3]
    tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (i,x1,y1,x2,y2,'Face' + str(i)))


tk.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (
"./img/FixationCross/blank.jpg", resolution[0] / 2, resolution[1] / 2,resolution[0], resolution[1]))
# tk.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % ('img/Anger-Neutral/6N-10A/block1matrix1.jpeg', resolution[0]/2,resolution[1]/2,resolution[1],resolution[1]))

# tk.sendMessage('!V IMGLOAD TOP_LEFT %s %d %d %d %d' % (
# "./img/FixationCross/blank.jpg", 0,0,resolution[0], resolution[1]))
# tk.sendMessage('!V IMGLOAD TOP_LEFT %s %d %d %d %d' % ('img/Anger-Neutral/6N-10A/block1matrix1.jpeg', 0,0,resolution[1],resolution[1]))
tk.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % ('img/Anger-Neutral/6N-10A/block1matrix1.jpeg', resolution[0]/2,resolution[1]/2,resolution[1],resolution[1]))


# STEP 8: close the EDF data file and put the tracker in idle mode
tk.setOfflineMode()
# pylink.pumpDelay(100)
# tk.closeDataFile()

tk.receiveDataFile(dataFileName, 'test1.edf')
