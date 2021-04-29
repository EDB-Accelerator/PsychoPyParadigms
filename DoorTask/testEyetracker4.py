from psychopy.iohub import launchHubServer
from psychopy.core import getTime, wait
import pylink

def newPoint(n,center,ratio):
    return int((n-center) * ratio + center)




tk = pylink.EyeLink('100.1.1.1')
dataFileName = 'test1.edf'
tk.openDataFile(dataFileName)

err = tk.startRecording(1, 1, 1, 1)
pylink.pumpDelay(100)  # wait for 100 ms to cache some samples

ratio = 1
tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, newPoint(236,1024/2,ratio), newPoint(-42,780/2,ratio), newPoint(788,1024/2,ratio), newPoint(940,780/2,ratio), 'example_IA'))
# tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (2, newPoint(12,1024/2,ratio), newPoint(-42,780/2,ratio), newPoint(157,1024/2,ratio), newPoint(942,780/2,ratio), 'example_IA'))
# tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (3, newPoint(863,1024/2,ratio), newPoint(-42,780/2,ratio), newPoint(1008,1024/2,ratio), newPoint(942,780/2,ratio), 'example_IA'))


# tk.sendMessage('!V IMGLOAD CENTER %s %d %d' % ('./img/doors1/p1r1.jpg', 1024/2,780/2))
tk.sendMessage('!V IMGLOAD CENTER %s %d %d' % ('./img/practice/practice_door.jpg', 1024/2,780/2))

# Quit

# STEP 8: close the EDF data file and put the tracker in idle mode
tk.setOfflineMode()
# pylink.pumpDelay(100)
# tk.closeDataFile()

tk.receiveDataFile(dataFileName, 'test1.edf')
