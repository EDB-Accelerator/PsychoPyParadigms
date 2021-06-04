# example: './img\\Disgust-Neutral\\10N-6D\\Block1Matrix23.jpeg'
import re
def GetEmotionLabels(dfLabel,img):
    for fileName in ['6N-10A','8N-8A','10N-6A','6N-10D','8N-8D','10N-6D']:
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