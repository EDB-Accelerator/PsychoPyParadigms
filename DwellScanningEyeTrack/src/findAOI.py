from psychopy.iohub import launchHubServer
from psychopy.core import getTime, wait
import pylink


def pointFromCenter(n,center,standard):
    return int(center+n*(center*2)/standard)

tk = pylink.EyeLink('100.1.1.1')
dataFileName = 'test1.edf'
tk.openDataFile(dataFileName)

err = tk.startRecording(1, 1, 1, 1)
pylink.pumpDelay(100)  # wait for 100 ms to cache some samples

ratio = 0.2
resolution = [1024,768]
tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, pointFromCenter(-70,resolution[0]/2,1024), pointFromCenter(-70,resolution[1]/2,768), pointFromCenter(70,resolution[0]/2,1024), pointFromCenter(70,resolution[1]/2,768), 'example_IA'))

# tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, pointFromCenter(236,1024/2,ratio), pointFromCenter(-42,768/2,ratio), pointFromCenter(788,1024/2,ratio), pointFromCenter(940,768/2,ratio), 'example_IA'))
# tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (2, pointFromCenter(12,1024/2,ratio), pointFromCenter(-42,768/2,ratio), pointFromCenter(157,1024/2,ratio), pointFromCenter(942,768/2,ratio), 'example_IA'))
# tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (3, pointFromCenter(863,1024/2,ratio), pointFromCenter(-42,768/2,ratio), pointFromCenter(1008,1024/2,ratio), pointFromCenter(942,768/2,ratio), 'example_IA'))


# tk.sendMessage('!V IMGLOAD CENTER %s %d %d' % ('./img/doors1/p1r1.jpg', 1024/2,768/2))
tk.sendMessage('!V IMGLOAD CENTER %s %d %d' % ('./img/FixationCross/Horizontal.jpg', 1024/2,768/2))

# Quit

# STEP 8: close the EDF data file and put the tracker in idle mode
tk.setOfflineMode()
# pylink.pumpDelay(100)
# tk.closeDataFile()

tk.receiveDataFile(dataFileName, 'test1.edf')
