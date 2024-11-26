import glob
import os
import zipfile
import datetime
from shutil import move

# Remove all result files
fileList = glob.glob('result/CSV/*.csv')
for F in fileList:
    os.remove(F)
fileList = glob.glob('result/EDF/*.edf')
for F in fileList:
    os.remove(F)

# Remove the temporary lock file if it exists
try:
    os.remove(".tmp/version2Lock.txt")
except FileNotFoundError:
    pass

# Function to zip the directory with specific file modifications
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

# Create a zip file with a timestamp
timeLabel = datetime.datetime.now().strftime("%m%d%Y")
zip_file_name = f'../DwellScanningEyeTrack_Green_Blue_{timeLabel}.zip'
zipf = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
zipdir_with_file_operations('.', zipf, 'main_green_red.py', 'main.py', 'main_v2.py')
zipf.close()

# Print the full path of the created zip file
zip_file_path = os.path.abspath(zip_file_name)
print(f"Zip file created at: {zip_file_path}")
