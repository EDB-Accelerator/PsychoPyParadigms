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
# Import developer-defined functions
import sys
sys.path.insert(1, './src')
from DictWrite import SectionStart,SectionEnd,DictWriteRaw
import os
import platform
import random

def PlayVideo(df,dfRaw,params,dict,dictRaw,win,version):
    # Initialization
    dict["Section"] = "Video Play: Version" + str(version)

    # Starting Screen
    SectionStart(df, dfRaw, params, dict, dictRaw, dict["Section"])

    # Play Video
    DictWriteRaw(dfRaw, dictRaw, params, "Video Play (Started): Version" + str(version))
    if platform.system() == 'Windows':
        if version == 1:
            os.system('runvideo1.bat')
        elif version == 2:
            os.system('runvideo2.bat')

    # elif platform.system() == 'Drawin':
        # os.system('/Applications/VLC.app/Contents/MacOS/VLC --fullscreen "./video/version1.mp4" vlc://quit')
    DictWriteRaw(dfRaw, dictRaw, params, "Video Play (Ended): Version" + str(version))

    SectionEnd(df,dfRaw,params,dict,dictRaw,dict["Section"])
