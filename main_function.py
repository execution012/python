import os
import sys

# 添加当前目录到系统路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# 导入其他模块
from rename_images import rename_images, rename_method_original, rename_method_pinyin
from check_image_sizes import check_image_sizes_in_folder
from resize_images import resize_image

def get_valid_folder_path():
    """获取有效的文件夹路径"""
    while True:
        folder_path = input("请输入文件夹路径: ").strip('"')
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            return folder_path
        else:
            print("无效的文件夹路径，请重新输入。")

def get_valid_choice():
    """获取有效的功能选择"""
    valid_choices = ["1", "2", "3"]
    while True:
        choice = input("请选择功能：\n1. 重命名图片文件\n2. 检查图片尺寸\n3. 修改图片尺寸\n选择：")
        if choice in valid_choices:
            return choice
        else:
            print("无效的选择，请重新输入。")

def get_valid_method_choice():
    """获取有效的重命名方法选择"""
    valid_choices = ["1", "2"]
    while True:
        method_choice = input("请选择重命名方法（输入1使用原方法，输入2使用拼音方法）：")
        if method_choice in valid_choices:
            return method_choice
        else:
            print("无效的选择，请重新输入。")

def get_valid_save_option():
    """获取有效的保存选项"""
    valid_choices = [1, 2]
    while True:
        try:
            save_option = int(input("选择："))
            if save_option in valid_choices:
                return save_option
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的选择，请重新输入。")

def main():
    folder_path = get_valid_folder_path()
    choice = get_valid_choice()

    if choice == "1":
        method_choice = get_valid_method_choice()
        method = rename_method_original if method_choice == "1" else rename_method_pinyin
        rename_images(folder_path, method)
    elif choice == "2":
        check_image_sizes_in_folder(folder_path)
    elif choice == "3":
        width = int(input("请输入新的宽度："))
        height = int(input("请输入新的高度："))
        print("请选择保存选项：\n1. 保存到原路径的新文件夹内\n2. 直接覆盖原图片")
        save_option = get_valid_save_option()
        resize_image(folder_path, (width, height), save_option)
        print("修改图片尺寸完成。")

if __name__ == "__main__":
    main()