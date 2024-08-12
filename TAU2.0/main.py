from psychopy import visual, event, core,gui
import sys

sys.path.insert(1,'src')

# Function to display the input dialog and return the results
def get_user_input():
    info = {'Subject Number': '', 'Session Number': '', 'Stimuli Set': ['A', 'B']}
    order = ['Subject Number', 'Session Number', 'Stimuli Set']
    dlg = gui.DlgFromDict(dictionary=info, title='Experiment Startup', order=order)
    if dlg.OK:
        return info
    else:
        core.quit()  # the user hit cancel so exit

def display_text_and_wait_keys(win,text,keys):
    # Create a text stimulus
    hello_text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)

    # Draw the text stimulus to the window
    hello_text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Wait for a key press (specifically the spacebar)
    keys = event.waitKeys(keyList=keys)

def display_text_and_wait_given_sec(win,text,wait_time):
    # Create a text stimulus
    hello_text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)

    # Draw the text stimulus to the window
    hello_text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Display the text and check for a key press within 1 second
    user_input = None
    timer = core.Clock()
    while timer.getTime() < wait_time:  # Run for 1 second
        keys = event.getKeys()
        if keys:
            user_input = keys[0]
            break
    return user_input

def display_check_scanner(win):
    info = {}
    gui.DlgFromDict(dictionary=info,title='Scanner Prepared?')
    # core.quit()  # the user hit cancel so exit

user_info = get_user_input()
params = {'sdan' : user_info['Subject Number|0'],
          'session': user_info['Session Number|1'],
          'version': user_info['Stimuli Set|2']
}
win = visual.Window(size=(1024, 768), fullscr=False, color=(0, 0, 0), colorSpace='rgb')

display_text_and_wait_keys(win,'Instructions\n\n'
                'In each trial, a + sign will appear in the center of the screen,\n'
                'followed by a pair of faces, and then by a target: < or >\n\n'
                'if the target is <, press the left button.\n'
                'if the target is >, press the right button.\n\n'
                'Respond as quickly as you can without making mistakes\n\n'
                'Press any button to start.', ['4','6'])

# Create a window
key = display_text_and_wait_given_sec(win,"",1.0)
display_check_scanner(win)
display_text_and_wait_keys(win,'Waiting for the scanner..', ['4'])

# TrialProc

# 1. InitTrial
# 'top box coordinates: anchor + jitter
# Set probe_box_top = CSlideImage(Probe.States(Probe.ActiveState).Objects("top"))
# probe_box_top.x = (PROBE_TOP_X_ANCHOR - JITTER_RANGE_HORIZONTAL/2) + CInt(random(0,JITTER_RANGE_HORIZONTAL))
# probe_box_top.y = (PROBE_TOP_Y_ANCHOR - JITTER_RANGE_VERTICAL/2) + CInt(random(0,JITTER_RANGE_VERTICAL))
#
# 'bottom box coordinates: anchor + jitter
# Set probe_box_bottom = CSlideImage(Probe.States(Probe.ActiveState).Objects("bottom"))
# probe_box_bottom.x = (PROBE_BOTTOM_X_ANCHOR - JITTER_RANGE_HORIZONTAL/2) + CInt(random(0,JITTER_RANGE_HORIZONTAL))
# probe_box_bottom.y = (PROBE_BOTTOM_Y_ANCHOR - JITTER_RANGE_VERTICAL/2) + CInt(random(0,JITTER_RANGE_VERTICAL))
#
# c.SetAttrib "horizontalJitterTop", PROBE_TOP_X_ANCHOR - probe_box_top.x
# c.SetAttrib "VerticalJitterTop", PROBE_TOP_Y_ANCHOR - probe_box_top.y
# c.SetAttrib "horizontalJitterBottom", PROBE_BOTTOM_X_ANCHOR - probe_box_bottom.x
# c.SetAttrib "VerticalJitterBottom", PROBE_BOTTOM_Y_ANCHOR - probe_box_bottom.y
#
# trial_count = trial_count + 1
###################

# 2. Fixation (500ms)
# 3. Faces
# 4. Probe
# 5. ITI




















# Close the window and quit PsychoPy
# win.close()
# core.quit()