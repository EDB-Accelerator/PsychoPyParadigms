from psychopy import core,gui
def get_user_input():
    info = {'Subject Number': '', 'Session Number': '', 'Stimuli Set': ['A', 'B']}
    order = ['Subject Number', 'Session Number', 'Stimuli Set']
    dlg = gui.DlgFromDict(dictionary=info, title='Experiment Startup', order=order)
    if dlg.OK:
        return info
    else:
        core.quit()  # the user hit cancel so exit