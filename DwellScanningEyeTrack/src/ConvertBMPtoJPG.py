from PIL import Image
import glob
import cv2
import os

blocks = glob.glob("img_training/*")

for block in blocks:
    imgList = glob.glob(block + "/*.bmp")
    for imgFile in imgList:
        image = cv2.imread(imgFile)
        cv2.imwrite(imgFile.replace('.bmp', '.jpg'), image)
        os.remove(imgFile)

for block in blocks:
    imgList = glob.glob(block + "/*.jpg")
    for imgFile in imgList:
        imgOld = imgFile
        imgFile = imgFile.replace("block", "Block")
        imgFile = imgFile.replace("matrix", "Matrix")
        imgFile = imgFile.replace(" ", "")
        os.rename(imgOld,imgFile)
