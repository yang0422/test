__author__ = 'libo.yang'
# @time: 2016/10/31 10:39
import base64
from Common import project_path

with open(project_path.png_path, "rb") as file:
    image_png = base64.b64encode(file.read()).decode('utf-8')