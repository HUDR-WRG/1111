#将图标文件夹复制到图标包中
import os
import shutil

def move_folders(source_dir):
    folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]
    target_folders = [f for f in folders if len(f) < 8]

    for folder in folders:
        folder_path = os.path.join(source_dir, folder)
        if len(folder) > 8:
            for target_folder in target_folders:
                target_path = os.path.join(source_dir, target_folder)
                dest_folder_path = os.path.join(target_path, folder)
                if os.path.exists(dest_folder_path):
                    shutil.rmtree(dest_folder_path)
                shutil.copytree(folder_path, dest_folder_path)
            shutil.rmtree(folder_path)

if __name__ == "__main__":
    source_directory = os.path.dirname(os.path.abspath(__file__))
    move_folders(source_directory)
