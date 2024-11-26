import glob,random
import os

# Make image list.
RunList = glob.glob('./img/*')
random.shuffle(RunList)
idx = 0
ImgList = []
for run in RunList:
    BlockList = glob.glob(run + '/*')
    random.shuffle(BlockList)

    for block in BlockList:

        # Get Image list of each block and Shuffle.
        ImgList = ImgList + glob.glob(block + '/*.jpeg')
        idx += 1

newImgList = []
for imgName in ImgList:
    newImage = imgName.replace(" ","")
    newImage = newImage.replace("b", "B")
    newImage = newImage.replace("m", "M")
    os.rename(imgName,newImage)




a = ImgList[0]
a = a.replace(" ","")
