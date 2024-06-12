import os
import shutil
import zipfile
from datetime import datetime

def modify_and_copy_files(src_dir, dest_dir, modify=False):
    """Copy all files from src_dir to dest_dir, applying modifications to main.py for NYU version."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)  # Ensure all directories are copied
        else:
            if item == 'main.py' and modify:
                # Apply modifications to main.py for NYU version
                with open(src_path, 'r') as file:
                    lines = file.readlines()
                with open(dest_path, 'w') as file:
                    for line in lines:
                        if 'userInput.addField(\'Port\':' in line and 'choices=[' in line:
                            # Change the default port to "LPT1" for NYU version
                            line = line.replace('"COM4"', '"LPT1"')
                        file.write(line)
            else:
                shutil.copy2(src_path, dest_path)

def zip_folder(folder_path, output_path):
    """Compress the folder at folder_path into a zip file saved to output_path."""
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                                           os.path.join(folder_path, '..')))

def main():
    # Format current date
    date_str = datetime.now().strftime("%m%d%Y")

    current_dir = os.getcwd()  # Get the current working directory
    downloads_path = os.path.expanduser('~/Downloads')  # Path to save the zip files

    # Setup temporary directories
    temp_umd_dir = os.path.join(downloads_path, f'AuditoryOddball_UMD_{date_str}')
    temp_nyu_dir = os.path.join(downloads_path, f'AuditoryOddball_NYU_{date_str}')

    # Copy files for UMD version without modifications
    modify_and_copy_files(current_dir, temp_umd_dir, modify=False)
    # Copy and modify files for NYU version
    modify_and_copy_files(current_dir, temp_nyu_dir, modify=True)

    # Zip both versions with formatted names including the date
    umd_zip_name = f'Auditory_Oddball_UMD_{date_str}.zip'
    nyu_zip_name = f'Auditory_Oddball_NYU_{date_str}.zip'
    zip_folder(temp_umd_dir, os.path.join(downloads_path, umd_zip_name))
    zip_folder(temp_nyu_dir, os.path.join(downloads_path, nyu_zip_name))

    # Clean up temporary directories
    shutil.rmtree(temp_umd_dir)
    shutil.rmtree(temp_nyu_dir)

    print(f'UMD version zip file created at {os.path.join(downloads_path, umd_zip_name)}')
    print(f'NYU version zip file created at {os.path.join(downloads_path, nyu_zip_name)}')

if __name__ == "__main__":
    main()
