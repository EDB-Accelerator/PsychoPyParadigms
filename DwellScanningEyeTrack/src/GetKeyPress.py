from psychopy import event,core
from MusicControl import StopMusic
def GetKeyPress(params=None):
    keys = event.getKeys()
    if keys == ['q'] or keys == ['Q'] or keys == ['Esc']:
        print('Q pressed. Forced Exit.')
        StopMusic()
        if params != None:
            if params['EyeLinkSupport']:
                import pylink
                params['tracker'].setRecordingState(False)
                trackerIO = pylink.EyeLink('100.1.1.1')
                trackerIO.receiveDataFile("et_data.EDF", params["edfFile"] + "_aborted.edf")
                # Stop the ioHub Server
                params['io'].quit()
                trackerIO.close()
        core.quit()
    return keys