def WaitUserSpace(params=None):
    from psychopy import core, event
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')

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