from psychopy import visual, event, core,gui
import sys,os
import platform
sys.path.insert(1,'src')
from psychopy import prefs, gui
import datetime

# Global Exit
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

# Function to display the input dialog and return the results
def get_user_input():
    # info = {'Subject Number': '', 'Session Number': '', 'Stimuli Set': ['A', 'B']}
    # order = ['Subject Number', 'Session Number', 'Stimuli Set']
    # dlg = gui.DlgFromDict(dictionary=info, title='Experiment Startup', order=order)
    # if dlg.OK:
    #     return info
    # else:
    #     core.quit()  # the user hit cancel so exit
    userInput = gui.Dlg(title="Experiment Startup")
    userInput.addField('Subject ID', )
    userInput.addField('Session Number', )
    userInput.addField('Stimuli Set', choices = ['A','B'])
    if platform.system() != "Darwin":
        userInput.addField('FullScreen', True)
    UserInputBank = userInput.show()

    return UserInputBank

def display_text_and_wait_keys(win,text,keys):
    # Create a text stimulus
    hello_text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)

    # Draw the text stimulus to the window
    hello_text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    if keys != "any":
        # Wait for a key press (specifically the spacebar)
        keys = event.waitKeys(keyList=keys)
    else:
        # Continue waiting for key presses until a key other than '2' or '4' is pressed
        valid_key = False
        pressed_key = None
        while not valid_key:
            keys = event.getKeys()
            if keys:
                pressed_key = keys[0]
                if pressed_key not in ['2', '4']:
                    valid_key = True
        # keys = event.waitKeys()
    return keys

def display_text_and_wait_given_sec(win,text,wait_time):
    # Create a text stimulus
    if text == "+" or text == "":
        frame_image = visual.ImageStim(win=win, image="enlarged_images/frame.bmp", pos=[0, 0])
        original_size = frame_image.size
        frame_image.size = [dimension * 1.5 for dimension in original_size]
        frame_image.draw()

    text = visual.TextStim(win, text=text, color=(-1, -1, -1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)
    if text == "Thank you for participating!":
        text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)


    # Draw the text stimulus to the window
    text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Display the text and check for a key press within given second
    user_input = None
    timer = core.Clock()
    while timer.getTime() < wait_time:  # Run for 1 second
        if user_input == '2' and user_input == '4':
            continue
        keys = event.getKeys()
        if keys:
            user_input = keys[0]
            # print(user_input)
            continue
    return user_input if user_input == '4' or user_input == '2' else None

def display_check_scanner(win):
    info = {}
    gui.DlgFromDict(dictionary=info,title='Scanner Prepared?')
    # core.quit()  # the user hit cancel so exit

def display_faces_and_wait_given_sec(win, face_top, face_bottom, wait_time,mode="face"):
    # Define the positions for the images
    top_position = [0, 0.4]  # Adjust as needed
    bottom_position = [0, -0.4]  # Adjust as needed

    # Load and prepare the images
    # if mode == 'face':
    top_image = visual.ImageStim(win=win, image=face_top, pos=top_position)
    bottom_image = visual.ImageStim(win=win, image=face_bottom, pos=bottom_position)
    frame_image = visual.ImageStim(win=win, image="enlarged_images/frame.bmp", pos=[0,0])
    original_size = frame_image.size
    frame_image.size = [dimension * 1.5 for dimension in original_size]

    # background_image = visual.ImageStim(win=win, image="enlarged_images/background.bmp", pos=[0, 0])
    # original_size_bg = background_image.size
    # background_image.size = [dimension * 5 for dimension in original_size_bg]



    # else:
        # top_position = [0, 0.4]  # Adjust as needed
        # bottom_position = [0, -0.4]  # Adjust as needed
        # top_image = visual.TextStim(win, text=face_top, color=(1, 1, 1), colorSpace='rgb', pos=top_position, wrapWidth=2)
        # bottom_image = visual.TextStim(win, text=face_bottom, color=(1, 1, 1), colorSpace='rgb', pos=bottom_position,
        #                                wrapWidth=2)
    # Draw the images on the window
    # background_image.draw()
    frame_image.draw()
    top_image.draw()
    bottom_image.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Display the text and check for a key press within the given time
    timer = core.Clock()
    response = None
    response_time = None

    while timer.getTime() < wait_time:
        # Check for key press
        keys = event.getKeys(timeStamped=timer)
        if keys:
            response, response_time = keys[0]
            if response in ['2', '4']:
                print(response)  # Optional: Print the response for debugging
                break  # Exit the loop after recording the first valid response

    # Pause for the remaining time if a response was received before wait_time
    remaining_time = wait_time - timer.getTime()
    if remaining_time > 0:
        core.wait(remaining_time)

    # Return the recorded response and response time only if it is valid
    return (response, response_time) if response in ['2', '4'] else (None, None)


# Initialization
# Constants
PROBE_TOP_X_ANCHOR = 512
PROBE_TOP_Y_ANCHOR = 185
PROBE_BOTTOM_X_ANCHOR = 512
PROBE_BOTTOM_Y_ANCHOR = 485
JITTER_RANGE_HORIZONTAL = 20
JITTER_RANGE_VERTICAL = 40

ACC_CHECK_TRIALS = 10  # Number of trials to check for accuracy threshold
ERROR_THRESHOLD = 0.31  # Subject must do better than this % during ACC_CHECK_TRIALS

# Variables
face_set = ""  # String equivalent
probe_box_top = None  # Placeholder for the SlideImage equivalent in Python
probe_box_bottom = None  # Placeholder for the SlideImage equivalent in Python

trial_count = 0  # Integer equivalent
error_count = 0  # Integer equivalent

aborted = False  # Boolean equivalent

TR = 0  # Integer equivalent
leftresp = 0  # Integer equivalent
rightresp = 0  # Integer equivalent
triggervalue = 0  # Integer equivalent


user_info = get_user_input()
try:
    params = {'sdan': user_info[0],
              'session': user_info[1],
              'version': user_info[2]
              }
    prefs.general['fullscr'] = user_info[3]

except:
    params = {'sdan': user_info['Subject ID'],
              'session': user_info['Session Number'],
              'version': user_info['Stimuli Set']
              }

# win = visual.Window(size=(1024, 768), fullscr=prefs.general['fullscr'], color=(74, 96, 93), colorSpace='rgb255')
win = visual.Window(size=(1024, 768), fullscr=prefs.general['fullscr'], color=(-1, -1, -1), colorSpace='rgb')
win.mouseVisible = False
display_text_and_wait_keys(win,'Instructions\n\n'
                'In each trial, a + sign will appear in the center of the screen,\n'
                'followed by a pair of faces, and then by a target: < or >\n\n'
                'if the target is <, press the left button.\n'
                'if the target is >, press the right button.\n\n'
                'Respond as quickly as you can without making mistakes\n\n'
                'Press any button to start.', "any")

# Create a window
key = display_text_and_wait_given_sec(win," ",1.0)
# win.mouseVisible = True
# display_check_scanner(win)
# display_text_and_wait_keys(win,'Scanner Ready?', ['5'])
# win.mouseVisible = False
display_text_and_wait_keys(win,'Waiting for the scanner..', ['5'])

# TrialProc
import pandas as pd
import random

# Function to load and concatenate CSV files
def load_and_concat_csv_files(prefixes, categories, directory='timing'):
    dataframes = []
    for category in categories:
        if category in ['NTc', 'NN', 'NTi']:
            for prefix in prefixes:
                df = pd.read_csv(f'{directory}/{prefix}{category}.csv')
                df['type'] = f'{prefix}{category}'
                dataframes.append(df)
        elif category in ['null','baseline']:
            df = pd.read_csv(f'{directory}/{category}.csv')
            df['type'] = f'{category}'
            dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)

# Prefixes and categories that apply
prefixes = ['f', 'm']
categories = ['NTc', 'NN', 'NTi','null','baseline']

# Initialize a list to hold trial data
trial_data = []

for list_idx in range(2):

    # Load and concatenate all files into a single DataFrame
    df_all = load_and_concat_csv_files(prefixes, categories)

    # Load ITI files
    df_iti = pd.read_csv("timing/ITIList.csv")
    ITIs = list(df_iti['ITIDur']) * 11
    random.shuffle(ITIs)

    # Shuffle the combined DataFrame
    df_all = df_all.sample(frac=1).reset_index(drop=True)

    # for i in range(len(df_all)):
    for i in range(10):
        trial_id = i + 1
        df = df_all.iloc[i]

        # 1. Fixation Cross
        start_time = core.Clock()
        display_text_and_wait_given_sec(win, "+", 0.5)
        fixation_duration = start_time.getTime()
        trial_data.append({
            'Subject ID': params['sdan'],
            'Session Number': params['session'],
            'Stimuli Set': params['version'],
            'Trial_ID': str(int(trial_id)),
            'Step': 'Fixation',
            'Stimulus': '+',
            'Duration': fixation_duration,

            'FaceTop': df['FaceTop'] if 'FaceTop' in df else None,
            'FaceBottom': df['FaceBottom'] if 'FaceBottom' in df else None,
            'ProbeTop': df['ProbeTop'] if 'ProbeTop' in df else None,
            'ProbeBottom': df['ProbeBottom'] if 'ProbeBottom' in df else None,
            'Response': None,
            'ResponseTime': None,
            'Correctness': "",

            'CorrectResponse': df['CorrectResponse'] if 'CorrectResponse' in df else None,
            'ProbeBehind': df['ProbeBehind'] if 'ProbeBehind' in df else None,
            'ProbeType': df['ProbeType'] if 'ProbeType' in df else None,
            'ProbeLocation': df['ProbeLocation'] if 'ProbeLocation' in df else None,
            'Condition': df['Condition'] if 'Condition' in df else None,

            'Type': df['type']
        })

        # 2. Display Faces
        start_time = core.Clock()
        FaceTop = f"enlarged_images/{params['version']}/{df['FaceTop']}.bmp" if df['FaceTop']!='blank' else f"enlarged_images/blank.bmp"
        FaceBottom = f"enlarged_images/{params['version']}/{df['FaceBottom']}.bmp" if df['FaceBottom']!='blank' else f"enlarged_images/blank.bmp"

        # top_image = visual.ImageStim(win=win, image=FaceTop, pos=[0, 0.4])
        # bottom_image = visual.ImageStim(win=win, image=FaceBottom, pos=[0,-0.4])
        # top_image.draw()
        # bottom_image.draw()
        # win.flip()
        display_faces_and_wait_given_sec(win, FaceTop, FaceBottom, 0.5)
        face_display_duration = start_time.getTime()
        trial_data.append({
            'Subject ID': params['sdan'],
            'Session Number': params['session'],
            'Stimuli Set': params['version'],
            'Trial_ID': str(int(trial_id)),
            'Step': 'Display Faces',
            'Stimulus': f'{FaceTop} / {FaceBottom}',
            'Duration': face_display_duration,

            'FaceTop': df['FaceTop'] if 'FaceTop' in df else None,
            'FaceBottom': df['FaceBottom'] if 'FaceBottom' in df else None,
            'ProbeTop': df['ProbeTop'] if 'ProbeTop' in df else None,
            'ProbeBottom': df['ProbeBottom'] if 'ProbeBottom' in df else None,
            'Response': "",
            'ResponseTime': "",
            'Correctness': "",
            'CorrectResponse': df['CorrectResponse'] if 'CorrectResponse' in df else None,
            'ProbeBehind': df['ProbeBehind'] if 'ProbeBehind' in df else None,
            'ProbeType': df['ProbeType'] if 'ProbeType' in df else None,
            'ProbeLocation': df['ProbeLocation'] if 'ProbeLocation' in df else None,
            'Condition': df['Condition'] if 'Condition' in df else None,

            'Type': df['type']
        })

        # Probe
        start_time = core.Clock()
        # Determine the correct probe display based on 'ProbeTop' and 'ProbeBottom' values
        if df['ProbeTop'] == "blank":
            ProbeTop = "enlarged_images/blank.bmp"
        elif df['ProbeTop'] == "left":
            ProbeTop = "enlarged_images/left.bmp"
        elif df['ProbeTop'] == "right":
            ProbeTop = "enlarged_images/right.bmp"
        else:
            ProbeTop = ""  # Default to an empty string if the value is unexpected

        if df['ProbeBottom'] == "blank":
            ProbeBottom = "enlarged_images/blank.bmp"
        elif df['ProbeBottom'] == "left":
            ProbeBottom = "enlarged_images/left.bmp"
        elif df['ProbeBottom'] == "right":
            ProbeBottom = "enlarged_images/right.bmp"
        else:
            ProbeBottom = ""  # Default to an empty string if the value is unexpected
        # response,response_time = display_faces_and_wait_given_sec(win, ProbeTop, ProbeBottom, 1,mode="probe")
        response, response_time = display_faces_and_wait_given_sec(win, ProbeTop, ProbeBottom, 1)
        face_display_duration = start_time.getTime()
        trial_data.append({
            'Subject ID': params['sdan'],
            'Session Number': params['session'],
            'Stimuli Set': params['version'],
            'Trial_ID': str(int(trial_id)),
            'Step': 'Display Probes',
            'Stimulus': f'{ProbeTop} / {ProbeBottom}',

            'Duration': face_display_duration,

            'FaceTop': df['FaceTop'] if 'FaceTop' in df else None,
            'FaceBottom': df['FaceBottom'] if 'FaceBottom' in df else None,
            'ProbeTop': df['ProbeTop'] if 'ProbeTop' in df else None,
            'ProbeBottom': df['ProbeBottom'] if 'ProbeBottom' in df else None,
            'Response': "" if df["type"] == "null" else str(response) if response is not None else "",
            'ResponseTime': "" if df["type"] == "null" else str(response_time) if response_time is not None else "",
            'Correctness': "" if df["type"] == "null" else (
                "No Response" if response is None else
                "Correct" if (response == "4" and df["ProbeType"] == "left") or (
                            response == "2" and df["ProbeType"] == "right") else
                "Incorrect"
            ),
            'CorrectResponse': df['CorrectResponse'] if 'CorrectResponse' in df else None,
            'ProbeBehind': df['ProbeBehind'] if 'ProbeBehind' in df else None,
            'ProbeType': df['ProbeType'] if 'ProbeType' in df else None,
            'ProbeLocation': df['ProbeLocation'] if 'ProbeLocation' in df else None,
            'Condition': df['Condition'] if 'Condition' in df else None,

            'Type': df['type']
        })

        # ITI
        start_time = core.Clock()
        display_text_and_wait_given_sec(win,"",ITIs[i]/1000)
        iti_duration = start_time.getTime()
        trial_data.append({
            'Subject ID': params['sdan'],
            'Session Number': params['session'],
            'Stimuli Set': params['version'],
            'Trial_ID': str(int(trial_id)),
            'Step': 'ITI',
            'Stimulus': 'Blank',
            'Duration': iti_duration,

            'FaceTop': df['FaceTop'] if 'FaceTop' in df else None,
            'FaceBottom': df['FaceBottom'] if 'FaceBottom' in df else None,
            'ProbeTop': df['ProbeTop'] if 'ProbeTop' in df else None,
            'ProbeBottom': df['ProbeBottom'] if 'ProbeBottom' in df else None,
            'Response': None,
            'ResponseTime': None,
            'Correctness': "",
            'CorrectResponse': df['CorrectResponse'] if 'CorrectResponse' in df else None,
            'ProbeBehind': df['ProbeBehind'] if 'ProbeBehind' in df else None,
            'ProbeType': df['ProbeType'] if 'ProbeType' in df else None,
            'ProbeLocation': df['ProbeLocation'] if 'ProbeLocation' in df else None,
            'Condition': df['Condition'] if 'Condition' in df else None,

            'Type': df['type']
        })

    # Fixation
    start_time = core.Clock()
    display_text_and_wait_given_sec(win, "+", 2.5)
    fixation_duration = start_time.getTime()
    trial_data.append({
        'Trial_ID': str(int(trial_id)),
        'Step': 'Fixation',
        'Stimulus': '+',
        'Duration': fixation_duration,

        'FaceTop': df['FaceTop'] if 'FaceTop' in df else None,
        'FaceBottom': df['FaceBottom'] if 'FaceBottom' in df else None,
        'ProbeTop': df['ProbeTop'] if 'ProbeTop' in df else None,
        'ProbeBottom': df['ProbeBottom'] if 'ProbeBottom' in df else None,
        'Response': None,
        'ResponseTime': None,
        'Correctness': "",
        'CorrectResponse': df['CorrectResponse'] if 'CorrectResponse' in df else None,
        'ProbeBehind': df['ProbeBehind'] if 'ProbeBehind' in df else None,
        'ProbeType': df['ProbeType'] if 'ProbeType' in df else None,
        'ProbeLocation': df['ProbeLocation'] if 'ProbeLocation' in df else None,
        'Condition': df['Condition'] if 'Condition' in df else None,

        'Type': df['type']
    })

    # Rest
    if list_idx == 0:
        start_time = core.Clock()
        display_text_and_wait_keys(win, 'Please rest', "any")
        rest_duration = start_time.getTime()
        trial_data.append({
            'Subject ID': params['sdan'],
            'Session Number': params['session'],
            'Stimuli Set': params['version'],
            'Trial_ID': None,
            'Step': 'REST',
            'Stimulus': 'Please Rest',

            'Duration': rest_duration,

            'FaceTop': df['FaceTop'] if 'FaceTop' in df else None,
            'FaceBottom': df['FaceBottom'] if 'FaceBottom' in df else None,
            'ProbeTop': df['ProbeTop'] if 'ProbeTop' in df else None,
            'ProbeBottom': df['ProbeBottom'] if 'ProbeBottom' in df else None,
            'Response': None,
            'ResponseTime': None,
            'Correctness': "",
            'CorrectResponse': df['CorrectResponse'] if 'CorrectResponse' in df else None,
            'ProbeBehind': df['ProbeBehind'] if 'ProbeBehind' in df else None,
            'ProbeType': df['ProbeType'] if 'ProbeType' in df else None,
            'ProbeLocation': df['ProbeLocation'] if 'ProbeLocation' in df else None,
            'Condition': df['Condition'] if 'Condition' in df else None,

            'Type': df['type']
        })

# Convert the list of trial data to a DataFrame
df_trials = pd.DataFrame(trial_data)

from datetime import datetime

# Get the current date and time
now = datetime.now()
formatted_datetime = now.strftime("%Y%m%d_%H%M%S")

import os

# Define the folder name
folder_name = "results"

# Check if the folder exists, if not, create it
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f'Folder "{folder_name}" created.')
else:
    print(f'Folder "{folder_name}" already exists.')

# Define the desired column order based on the keys
column_order = [
    'Subject ID', 'Session Number', 'Stimuli Set', 'Trial_ID', 'Step', 'Stimulus',
    'Duration', 'FaceTop', 'FaceBottom', 'ProbeTop', 'ProbeBottom',
    'Response', 'ResponseTime', 'Correctness', 'CorrectResponse',
    'ProbeBehind', 'ProbeType', 'ProbeLocation', 'Condition', 'Type'
]

# Identify any additional columns that are not in the specified column order
additional_columns = [col for col in df_trials.columns if col not in column_order]

# Reorder the DataFrame with the specified columns first, followed by any additional columns
df_trials = df_trials[column_order + additional_columns]

# Save the DataFrame to a CSV file with the ordered columns
df_trials.to_csv(f'results/subject_{params["sdan"]}_session_{params["session"]}_{formatted_datetime}.csv', index=False)

# Thank you screen.
display_text_and_wait_given_sec(win,"Thank you for participating!",2.0)

# Close the window and quit PsychoPy
win.close()
core.quit()