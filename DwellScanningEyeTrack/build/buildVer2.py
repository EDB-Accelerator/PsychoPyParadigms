import glob,os
import shutil
from shutil import copyfile,move

# remove all timing files in 'notUsed'
fileList = glob.glob('timing/used/*.txt')
for F in fileList:
    os.remove(F)

# Copy good timing files
fileList = glob.glob('good_timing_files/*.txt')
for F in fileList:
    copyfile(F,F.replace('good_timing_files','timing\\notUsed'))

# remove all result files
fileList = glob.glob('result/CSV/*.csv')
for F in fileList:
    os.remove(F)
fileList = glob.glob('result/EDF/*.edf')
for F in fileList:
    os.remove(F)

# Move dwellscansub
move("dwellscansub","..")
move("music","..")
open('.tmp/version2Lock.txt', 'a').close()

# Make zip file
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

import datetime
timeLabel = datetime.datetime.now().strftime("%m%d%Y")

zipf = zipfile.ZipFile('../DwellScanningEyeTrackVer2_' + timeLabel +'.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('.', zipf)
zipf.close()
os.remove(".tmp/version2Lock.txt")
move("../dwellscansub",".")
move("../music",".")
