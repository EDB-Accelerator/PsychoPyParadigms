import sys
sys.path.insert(1, './src')

import datetime, os
import subprocess
from psychopy import visual
from Helper import waitUserSpace, tableWrite
import time

def FortuneGamePlay(Df, win, params, SectionName, gameResult):
    if params['JoyStickSupport']:
        from JoystickInput import JoystickInput
    else:
        from VirtualJoystickInput import JoystickInput

    Dict = {
        "Subject": params['subjectID'],
        "Session": params["Session"],
        "Version": params["Version"],
        "Section": SectionName,
        "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"),
    }

    # Initial image
    img1 = visual.ImageStim(win=win, image="./img/changeme.jpg", units="pix", opacity=1, size=(1024, 768))
    img1.draw()
    win.flip()
    win.mouseVisible = False

    # Wait for joystick press
    while (JoystickInput())['buttons_text'] == ' ':
        time.sleep(0.001)
        img1.draw()
        win.flip()
    while (JoystickInput())['buttons_text'] != ' ':
        time.sleep(0.001)

    win.mouseVisible = True
    win.close()

    # Show HTML animation in Edge
    if gameResult in (16, 18):
        html_file = f"FortuneWheel/index{gameResult}.html"
        file_url = f"file://{os.path.abspath(html_file)}"

        # Try both possible Edge install paths
        edge_paths = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
        ]
        edge_exe = None
        for path in edge_paths:
            if os.path.exists(path):
                edge_exe = path
                break

        if not edge_exe:
            raise FileNotFoundError("Microsoft Edge was not found in the standard locations.")

        # Launch Edge in kiosk mode
        edge_process = subprocess.Popen(
            [edge_exe, "--kiosk", file_url, "--edge-kiosk-type=fullscreen"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        # ✅ Immediately reopen the PsychoPy window and show winning message
        win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
        message = visual.TextStim(
            win,
            text=f"You have won ${gameResult}.\n\nClick when you are ready to keep playing.",
            units='norm', wrapWidth=2
        )
        message.draw()
        win.flip()
        win.mouseVisible = False

        # Wait for joystick press to continue
        while (JoystickInput())['buttons_text'] == ' ':
            time.sleep(0.001)
            message.draw()
            win.flip()
        while (JoystickInput())['buttons_text'] != ' ':
            time.sleep(0.001)

        # Kill Edge
        edge_process.terminate()

    return tableWrite(Df, params, Dict), win
