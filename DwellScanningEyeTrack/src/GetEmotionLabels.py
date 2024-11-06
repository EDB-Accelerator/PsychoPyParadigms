# example: './img\\Disgust-Neutral\\10N-6D\\Block1Matrix23.jpeg'
#example: 'img/Anger-Neutral\\6N10A\\Block1Matrix29.jpeg'
import re
import os
def GetEmotionLabels(dfLabel,img):
    # for fileName in ['6N10A','8N8A','10N6A','6N10D','8N8D','10N6D']:
    # for fileName in ['A_8H8S', 'W_8H8A', 'A_8N8D', 'B_8H8A', 'B_8N8D', 'A_8H8A', 'W_8H8S', 'B_8H8S', 'W_8N8D']:
    #     if fileName in img:
    #         break
    fileName = os.path.dirname(img)
    dfLabelFile = dfLabel[fileName]

    imgStr = img.split('Block')[-1]
    [block,matrix] = re.findall('\d+', imgStr)

    SlideImage = "block " + block + " matrix "+ matrix + ".bmp"

    dfLabelRow = dfLabelFile[dfLabelFile['SlideImage']==SlideImage]

    Emotion = ""
    if "Angry-Happy" in img:
        Emotion = "Angry-Happy"
    elif "Disgust-Neutral" in img:
        Emotion = "Disgust-Neutral"
    if "Sad-Happy" in img:
        Emotion = "Sad-Happy"

    Emotion = "Anger" if "Anger" in img else "Disgust"
    EmotionLables = []
    for i in range(1,17):
        if 'NE' in dfLabelRow.iloc[0]['Cell'+str(i)]:
            EmotionLables.append(False)
        else:
            EmotionLables.append(True)

    return Emotion,EmotionLables

# def GetEmotionLabelsThreeFour(dfLabel,img):
#     imgStr = img.split('Block')[-1]
#     [block, matrix] = re.findall('\d+', imgStr)
#
#     SlideImage = "block " + block + " matrix " + matrix + ".bmp"
#
#     dfLabelRow = dfLabel[dfLabel['SlideImage'] == SlideImage]
#
#     # find which emotion it has
#     Emotion = "Anger" if int(matrix) <= 15 else "Disgust"
#     print("matrix:"+str(matrix))
#
#     # Emotion = "Anger" if "Anger" in img else "Disgust"
#     EmotionLables = []
#     for i in range(1, 17):
#         if 'NE' in dfLabelRow.iloc[0]['Cell' + str(i)]:
#             EmotionLables.append(False)
#         else:
#             EmotionLables.append(True)
#     return Emotion, EmotionLables