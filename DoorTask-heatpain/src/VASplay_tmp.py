import platform
import datetime
from psychopy import visual, event, core

def displayVAS(Df, params, win, question, labels, SectionName, VAS_type):
    Dict = {
        'ExperimentName': params['expName'],
        "Subject": params['subjectID'],
        "Session": params['Session'],
        "Version": params['Version'],
        "Section": SectionName,
        "VAS_type": VAS_type,
        "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    }

    os_type = platform.system()
    start_time = core.Clock()

    if os_type == 'Darwin':  # macOS with Slider
        question_stim = visual.TextStim(win, text=question, pos=(0, 0.4), height=0.07, wrapWidth=1.5)
        slider = visual.Slider(
            win=win,
            ticks=(0, 1),
            labels=labels,
            granularity=0.01,
            style='rating',
            size=(1.0, 0.1),
            pos=(0, 0),
            labelHeight=0.06,
            color='White',
            fillColor='White',
            borderColor='White'
        )

        rating = None
        while rating is None:
            question_stim.draw()
            slider.draw()
            win.flip()

            if 'escape' in event.getKeys():
                core.quit()

            rating = slider.getRating()

        Dict["VAS_score"] = rating
        Dict["VAS_RT"] = start_time.getTime() * 1000  # in milliseconds

    else:  # Windows with RatingScale
        scale = visual.RatingScale(
            win,
            low=0,
            high=1,
            markerStart=0.5,
            labels=labels,
            stretch=1.5,
            scale=question,
            pos=(0, -0.4),
            size=1.5,
            tickHeight=0.0,
            showAccept=True
        )

        while scale.noResponse:
            scale.draw()
            win.flip()
            if 'escape' in event.getKeys():
                core.quit()

        Dict["VAS_score"] = scale.getRating()
        Dict["VAS_RT"] = scale.getRT() * 1000 if scale.getRT() else None

    return Dict
