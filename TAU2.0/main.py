from psychopy import visual, event, core,gui
import sys
sys.path.insert(1,'src')
from psychopy import prefs, gui
import datetime



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
    UserInputBank = userInput.show()

    return UserInputBank

def display_text_and_wait_keys(win,text,keys):
    # Create a text stimulus
    hello_text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)

    # Draw the text stimulus to the window
    hello_text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Wait for a key press (specifically the spacebar)
    keys = event.waitKeys(keyList=keys)

    return keys

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
        if user_input == '4' and user_input == '6':
            continue
        keys = event.getKeys()
        if keys:
            user_input = keys[0]
            # print(user_input)
            continue
    return user_input if user_input == '4' or user_input == '6' else None

def display_check_scanner(win):
    info = {}
    gui.DlgFromDict(dictionary=info,title='Scanner Prepared?')
    # core.quit()  # the user hit cancel so exit

def display_faces_and_wait_given_sec(win, face_top, face_bottom, wait_time,mode="face"):
    # Define the positions for the images
    top_position = [0, 0.4]  # Adjust as needed
    bottom_position = [0, -0.4]  # Adjust as needed

    # Load and prepare the images
    if mode == 'face':
        top_image = visual.ImageStim(win=win, image=face_top, pos=top_position)
        bottom_image = visual.ImageStim(win=win, image=face_bottom, pos=bottom_position)
    else:
        top_position = [0, 0.4]  # Adjust as needed
        bottom_position = [0, -0.4]  # Adjust as needed
        top_image = visual.TextStim(win, text=face_top, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0), wrapWidth=2)
        bottom_image = visual.TextStim(win, text=face_bottom, color=(1, 1, 1), colorSpace='rgb', pos=(0, -0.4),
                                       wrapWidth=2)
    # Draw the images on the window
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
            if response in ['4', '6']:
                print(response)  # Optional: Print the response for debugging
                break  # Exit the loop after recording the first valid response

    # Pause for the remaining time if a response was received before wait_time
    remaining_time = wait_time - timer.getTime()
    if remaining_time > 0:
        core.wait(remaining_time)

    # Return the recorded response and response time only if it is valid
    return (response, response_time) if response in ['4', '6'] else (None, None)


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
except:
    params = {'sdan': user_info['Subject ID'],
              'session': user_info['Session Number'],
              'version': user_info['Stimuli Set']
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
import pandas as pd
import random

# Function to load and concatenate CSV files
def load_and_concat_csv_files(prefixes, categories, directory='timing'):
    dataframes = []
    for prefix in prefixes:
        for category in categories:
            df = pd.read_csv(f'{directory}/{prefix}{category}.csv')
            df['type'] = f'{prefix}{category}'
            dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

# Prefixes and categories that apply
prefixes = ['f', 'm']
categories = ['NTc', 'NN', 'NTi']




# Initialize a list to hold trial data
trial_data = []

for list_idx in range(2):

    # Load and concatenate all files into a single DataFrame
    df_all = load_and_concat_csv_files(prefixes, categories)

    # Load ITI files
    df_iti = pd.read_csv("timing/ITIList.csv")
    ITIs = list(df_iti['ITIDur']) * 6
    random.shuffle(ITIs)

    # Shuffle the combined DataFrame
    df_all = df_all.sample(frac=1).reset_index(drop=True)

    # for i in range(len(df_all)):
    for i in range(5):
        trial_id = i + 1
        df = df_all.iloc[i]

        # 1. Fixation Cross
        start_time = core.Clock()
        display_text_and_wait_given_sec(win, "+", 0.5)
        fixation_duration = start_time.getTime()
        trial_data.append({
            'Trial_ID': trial_id,
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

            'Type': None
        })

        # 2. Display Faces
        start_time = core.Clock()
        FaceTop = f"enlarged_images/{params['version']}/{df['FaceTop']}.bmp"
        FaceBottom = f"enlarged_images/{params['version']}/{df['FaceBottom']}.bmp"

        # top_image = visual.ImageStim(win=win, image=FaceTop, pos=[0, 0.4])
        # bottom_image = visual.ImageStim(win=win, image=FaceBottom, pos=[0,-0.4])
        # top_image.draw()
        # bottom_image.draw()
        # win.flip()
        display_faces_and_wait_given_sec(win, FaceTop, FaceBottom, 0.5)
        face_display_duration = start_time.getTime()
        trial_data.append({
            'Trial_ID': trial_id,
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
            ProbeTop = ""
        elif df['ProbeTop'] == "left":
            ProbeTop = "<"
        elif df['ProbeTop'] == "right":
            ProbeTop = ">"
        else:
            ProbeTop = ""  # Default to an empty string if the value is unexpected

        if df['ProbeBottom'] == "blank":
            ProbeBottom = ""
        elif df['ProbeBottom'] == "left":
            ProbeBottom = "<"
        elif df['ProbeBottom'] == "right":
            ProbeBottom = ">"
        else:
            ProbeBottom = ""  # Default to an empty string if the value is unexpected
        response,response_time = display_faces_and_wait_given_sec(win, ProbeTop, ProbeBottom, 1,mode="probe")
        face_display_duration = start_time.getTime()
        trial_data.append({
            'Trial_ID': trial_id,
            'Step': 'Display Faces',
            'Stimulus': f'{FaceTop} / {FaceBottom}',

            'Duration': face_display_duration,

            'FaceTop': df['FaceTop'] if 'FaceTop' in df else None,
            'FaceBottom': df['FaceBottom'] if 'FaceBottom' in df else None,
            'ProbeTop': df['ProbeTop'] if 'ProbeTop' in df else None,
            'ProbeBottom': df['ProbeBottom'] if 'ProbeBottom' in df else None,
            'Response': str(response) if response is not None else "",
            'ResponseTime': str(response_time) if response_time is not None else "",
            'Correctness': (
                "No Response" if response is None else
                "Correct" if (response == "4" and df["ProbeType"] == "left") or (
                            response == "6" and df["ProbeType"] == "right") else
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
            'Trial_ID': trial_id,
            'Step': 'ITI',
            'Stimulus': 'ITI',
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

            'Type': None
        })

        # Fixation
        start_time = core.Clock()
        display_text_and_wait_given_sec(win, "+", 2.5)
        fixation_duration = start_time.getTime()
        trial_data.append({
            'Trial_ID': trial_id,
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

            'Type': None
        })

    # Rest
    start_time = core.Clock()
    display_text_and_wait_keys(win, 'Please rest', ['4', '6'])
    rest_duration = start_time.getTime()
    trial_data.append({
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

        'Type': None
    })

# Convert the list of trial data to a DataFrame
df_trials = pd.DataFrame(trial_data)


from datetime import datetime

# Get the current date and time
now = datetime.now()
formatted_datetime = now.strftime("%Y%m%d_%H%M%S")

# Save the DataFrame to a CSV file with date and time in the filename
df_trials.to_csv(f'results/subject_{params["sdan"]}_session_{params["session"]}_{formatted_datetime}.csv', index=False)

# Thank you screen.
display_text_and_wait_given_sec(win,"Thank you!",1.0)


# Close the window and quit PsychoPy
win.close()
core.quit()