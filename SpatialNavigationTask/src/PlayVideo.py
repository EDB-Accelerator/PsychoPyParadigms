# Python3-based package
"""
MIT License

Copyright (c) 2021 NIMH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
PlayInstruction.py

This function is for displaying Instructions.

Created on Thu Feb 18 08:11:29 EST 2021

@author: Kyunghun Lee
- Created on Thu Feb 18 08:11:29 EST 2021 by KL
"""

from psychopy import visual,core
from DictWrite import DictWriteRaw,SectionStart,SectionEnd
from DrawButton import DrawButton
import os
import platform

def PlayVideo(df,dfRaw,params,dict,dictRaw,win):
    # Initialization
    dict["Section"] = "Video Play"

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    if platform.system() == 'Windows':
        os.system('runvideo.bat')

    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])


# import cv2
# def play_videoFile(filePath,mirror=False):
#     cap = cv2.VideoCapture(filePath)
#     cv2.namedWindow('Video Life2Coding',cv2.WINDOW_AUTOSIZE)
#     while True:
#         ret_val, frame = cap.read()
#         if mirror:
#             frame = cv2.flip(frame, 1)
#         cv2.imshow('Video Life2Coding', frame)
#         if cv2.waitKey(1) == 27:
#             break  # esc to quit
#     cv2.destroyAllWindows()
# def main():
#     play_videoFile('./video/version1.mp4',mirror=False)
# if __name__ == '__main__':
#     main()