import os
import shutil
from pathlib import Path

script_dir = Path(__file__).parent

for img_path in script_dir.glob("*.png"):
    img_name = img_path.stem
    subfolder_path = script_dir / img_name
    subfolder_path.mkdir(exist_ok=True)
    new_img_path = subfolder_path / "monochrome.png"
    shutil.move(img_path, new_img_path)

print("操作完成！")
