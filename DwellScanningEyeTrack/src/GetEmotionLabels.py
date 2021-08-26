# example: './img\\Disgust-Neutral\\10N-6D\\Block1Matrix23.jpeg'
#example: 'img/Anger-Neutral\\6N10A\\Block1Matrix29.jpeg'
import re
def GetEmotionLabels(dfLabel,img):
    for fileName in ['6N10A','8N8A','10N6A','6N10D','8N8D','10N6D']:
        if fileName in img:
            break
    dfLabelFile = dfLabel[fileName]

    imgStr = img.split('Block')[-1]
    [block,matrix] = re.findall('\d+', imgStr)

    SlideImage = "block " + block + " matrix "+ matrix + ".bmp"

    dfLabelRow = dfLabelFile[dfLabelFile['SlideImage']==SlideImage]

    Emotion = "Anger" if "Anger" in img else "Disgust"
    EmotionLables = []
    for i in range(1,17):
        if 'NE' in dfLabelRow.iloc[0]['Cell'+str(i)]:
            EmotionLables.append(False)
        else:
            EmotionLables.append(True)

    return Emotion,EmotionLables

def GetEmotionLabelsThreeFour(dfLabel,img):
    imgStr = img.split('Block')[-1]
    [block, matrix] = re.findall('\d+', imgStr)

    SlideImage = "block " + block + " matrix " + matrix + ".bmp"

    dfLabelRow = dfLabel[dfLabel['SlideImage'] == SlideImage]

    # find which emotion it has
    Emotion = "Anger" if block <= 15 else "Disgust"

    # Emotion = "Anger" if "Anger" in img else "Disgust"
    EmotionLables = []
    for i in range(1, 17):
        if 'NE' in dfLabelRow.iloc[0]['Cell' + str(i)]:
            EmotionLables.append(False)
        else:
            EmotionLables.append(True)
    return Emotion, EmotionLables