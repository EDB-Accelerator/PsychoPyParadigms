import glob,os
import shutil
from shutil import copyfile,move

# remove all result files
fileList = glob.glob('result/CSV/*.csv')
for F in fileList:
    os.remove(F)
fileList = glob.glob('result/EDF/*.edf')
for F in fileList:
    os.remove(F)

try:
    os.remove(".tmp/version2Lock.txt")
except:
    pass
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

zipf = zipfile.ZipFile('../DwellScanningEyeTrackVer3and4_' + timeLabel +'.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('.', zipf)
zipf.close()