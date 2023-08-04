import os
import shutil


def organize_files(directory_path):
    # Mapping of file extensions to corresponding folders
    
    extension_mapping = {
        'pdf': 'PDFs',
        'png': 'Images',
        'jpg': 'Images',
        'jpeg': 'Images',
        'gif': 'Images',
        'bmp': 'Images',
        'tiff': 'Images',
        'doc': 'Documents',
        'docx': 'Documents',
        'txt': 'Documents',
        'rtf': 'Documents',
        'odt': 'Documents',
        'csv': 'Data',
        'xlsx': 'Data',
        'xls': 'Data',
        'ods': 'Data',
        'zip': 'Archives',
        'rar': 'Archives',
        'tar': 'Archives',
        'gz': 'Archives',
        '7z': 'Archives',
        'exe': 'Executables',
        'msi': 'Executables',
        'bat': 'Executables',
        'ipynb': 'Jupyter',
        'py': 'Python',
        'lnk': 'Shortcuts',
        'mp3': 'Music',
        'wav': 'Music',
        'flac': 'Music',
        'aac': 'Music',
        'mp4': 'Videos',
        'avi': 'Videos',
        'flv': 'Videos',
        'mkv': 'Videos',
        'mov': 'Videos',
        'wmv': 'Videos'
        # Add more extensions and categories as needed
    }

    # Check if the directory exists
    if not os.path.exists(directory_path):
        print("The specified directory does not exist")
        return

    # Iterate through each file in the directory
    for filename in os.listdir(directory_path):
        # Construct the full path of the file
        file_path = os.path.join(directory_path, filename)

        # Continue only if it's a file
        if not os.path.isfile(file_path):
            continue

        # Get the file extension (without the dot)
        file_extension = os.path.splitext(filename)[1][1:]

        # Get the corresponding folder name from the mapping
        folder_name = extension_mapping.get(file_extension, "Others")

        # Construct the folder path where the file will be moved
        folder_path = os.path.join(directory_path, folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Construct the destination path and move the file
        dest_path = os.path.join(folder_path, filename)
        shutil.move(file_path, dest_path)

        print(f"Moved {filename} to {folder_name}")


# Directory path you want to organize
directory_path = "C:\\users\\kaleb\\Downloads"

organize_files(directory_path)
