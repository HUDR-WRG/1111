import os

def rename_file_to_monochrome(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if len(files) == 1:
        old_file_path = os.path.join(folder_path, files[0])
        new_file_path = os.path.join(folder_path, "monochrome.png")
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {files[0]} -> monochrome.png")

def rename_files_in_subfolders(root_folder):
    for foldername in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, foldername)
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder_path}")
            rename_file_to_monochrome(folder_path)

if __name__ == "__main__":
    root_folder = os.getcwd()
    rename_files_in_subfolders(root_folder)
