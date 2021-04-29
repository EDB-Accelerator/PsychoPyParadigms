from psychopy.iohub import launchHubServer
from psychopy.core import getTime, wait
import pylink


tk = pylink.EyeLink('100.1.1.1')
dataFileName = 'test1.edf'
tk.openDataFile(dataFileName)

err = tk.startRecording(1, 1, 1, 1)
pylink.pumpDelay(100)  # wait for 100 ms to cache some samples

tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 500, 100, 600, 200, 'example_IA'))
tk.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % ('./img/ITI_fixation.jpg', 1024/2,768/2,1024, 768))

# Quit

# STEP 8: close the EDF data file and put the tracker in idle mode
# tk.setOfflineMode()
# pylink.pumpDelay(100)
# tk.closeDataFile()

tk.receiveDataFile(dataFileName, 'test1.edf')
