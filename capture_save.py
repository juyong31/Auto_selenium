import time
import os
from PIL import ImageGrab #이미지 캡쳐

# 캡쳐 후 저장폴더에 저장
def capture_and_save():
  current_time = time.strftime("%Y%m%d_%H%M%S")
  file_name = f"screenshot_{current_time}.png"
  folder_path = "C:\MobileAppTest\Workspace\python\Auto_selenium\screenshot_cpature"
  screenshot = ImageGrab.grab()
  screenshot.save(os.path.join(folder_path, file_name), "PNG")