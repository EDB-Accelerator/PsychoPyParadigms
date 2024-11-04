import os

def rename_files_in_directory(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Define the new filename transformations
            new_file_name = file_name.replace(" ", "").replace("block", "Block").replace("matrix", "Matrix")

            # Only rename if there's a difference
            if new_file_name != file_name:
                old_path = os.path.join(root, file_name)
                new_path = os.path.join(root, new_file_name)

                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed '{old_path}' to '{new_path}'")
                except Exception as e:
                    print(f"Error renaming '{old_path}' to '{new_path}': {e}")


# Example usage
folder_path = "/Users/jimmy/Downloads/Matrices"
rename_files_in_directory(folder_path)
