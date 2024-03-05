import os
import glob
from PIL import Image

def check_image_sizes_in_folder(folder_path):
    try:
        # 获取当前目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 定义输出文件路径为当前目录下的image_sizes.txt
        output_path = os.path.join(current_dir, "图片尺寸.txt")

        # 打开要写入的txt文件
        with open(output_path, "w") as output_file:
            # 定义要查找的文件类型模式
            patterns = ['*.jpg', '*.png']
            for pattern in patterns:
                # 使用glob模块在文件夹中搜索匹配的文件
                for image_path in glob.glob(os.path.join(folder_path, pattern)):
                    try:
                        # 使用Pillow库打开并读取图片信息
                        with Image.open(image_path) as img:
                            width, height = img.size
                            # 写入图片路径和尺寸到txt文件
                            output_file.write(f"{image_path}: {width}x{height} 像素 \n")
                    except IOError:
                        # 如果图片无法打开，打印错误信息
                        output_file.write(f"Error opening {image_path}\n")
        print("图片尺寸信息已保存到文件:", output_path)
    except Exception as e:
        print(f"保存文件时发生错误: {e}")
