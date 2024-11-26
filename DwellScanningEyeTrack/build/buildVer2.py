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
# move("dwellscansub","..")
try:
    move("music","..")
except:
    pass
open('.tmp/version2Lock.txt', 'a').close()

# Make zip file
import zipfile

# def zipdir(path, ziph):
#     # ziph is zipfile handle
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file),
#                        os.path.relpath(os.path.join(root, file),
#                                        os.path.join(path, '..')))

def zipdir_with_file_operations(path, ziph, rename_from, rename_to, exclude_file):
    # Zip all files and directories in the given path
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, os.path.join(path, '..'))
            # Rename specific file inside the zip
            if file == rename_from:
                arcname = arcname.replace(rename_from, rename_to)
            # Skip excluded file
            if file == exclude_file:
                continue
            ziph.write(full_path, arcname)

import datetime
# Create a zip file with a timestamp
timeLabel = datetime.datetime.now().strftime("%m%d%Y")
zipf = zipfile.ZipFile('../DwellScanningEyeTrackVer2_' + timeLabel + '.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir_with_file_operations('.', zipf, 'main_v2.py', 'main.py', 'main_green_red.py')
zipf.close()

# Remove the temporary lock file
try:
    os.remove(".tmp/version2Lock.txt")
except Exception as e:
    print(f"Error removing lock file: {e}")

# Move the 'music' folder back to its original location
move("../music", ".")