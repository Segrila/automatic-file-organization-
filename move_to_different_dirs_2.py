import os
import shutil

source_folder = "your_working_directory_path"
dest_folder = "your_working_directory_path"

for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):
        source_path = os.path.join(source_folder, filename)
        folder_name = filename[0].lower()
        destination_path = os.path.join(dest_folder, folder_name, filename)
        
        # Check if the destination folder is the same as the source folder
        if os.path.abspath(os.path.dirname(source_path)) == os.path.abspath(os.path.dirname(destination_path)):
            continue
        
        os.makedirs(os.path.join(dest_folder, folder_name), exist_ok=True)
        shutil.move(source_path, destination_path)
        
print("Files moved successfully!")