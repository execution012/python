import os
import re
from PIL import Image
from xpinyin import Pinyin

def get_image_size(file_path):
    """
    获取图片的宽度和高度
    """
    try:
        with Image.open(file_path) as img:
            width, height = img.size
        return width, height
    except Exception as e:
        print(f"无法获取图片大小: {e}")
        return None, None

def rename_images(folder_path, method):
    """
    重命名图片文件
    """
    try:
        # 检查输入路径是否有效
        if not os.path.isdir(folder_path):
            print("文件夹路径无效，请重新输入有效路径。")
            return

        # 获取文件夹中的所有文件列表
        file_list = os.listdir(folder_path)

        # 遍历文件夹中的文件
        for file_name in file_list:
            # 构建文件的完整路径
            file_path = os.path.join(folder_path, file_name)

            # 检查是否是文件
            if os.path.isfile(file_path):
                # 使用正则表达式提取文件名中的数字
                digits = re.search(r'(\d+)', file_name)
                if not digits:
                    print(f"文件名格式不符合要求，无法重命名：{file_name}")
                    continue

                # 提取数字部分
                digits = digits.group(1)

                # 使用正则表达式去除数字部分
                new_file_name = re.sub(r'\d+-\d+', '', file_name)

                # 获取图片的宽度和高度
                width, height = get_image_size(file_path)
                if width is None or height is None:
                    continue

                # 根据方法选择不同的重命名规则
                new_file_name = method(new_file_name, width, height)

                # 获取文件后缀
                file_extension = os.path.splitext(file_name)[1]

                # 重命名文件
                new_file_path = os.path.join(folder_path, f"{new_file_name}{file_extension}")
                os.rename(file_path, new_file_path)

                print(f"重命名文件: {file_name} -> {new_file_name}{file_extension}")
    except Exception as e:
        print(f"重命名过程中发生错误: {e}")

def rename_method_original(file_name, width, height):
    """
    使用原方法重命名
    """
    # 获取文件后缀
    file_extension = os.path.splitext(file_name)[1]

    # 根据比较结果修改文件名
    if width > height:
        file_name += "横图"
    elif height > width:
        file_name += "竖图"

    # 将 ".jpg横图" 或 ".jpg竖图" 部分改为 "横图" 或 "竖图"
    file_name = re.sub(r'\.jpg横图', '横图', file_name)
    file_name = re.sub(r'\.jpg竖图', '竖图', file_name)

    return file_name

def rename_method_pinyin(file_name, width, height):
    """
    使用拼音重命名
    """
    pin = Pinyin()
    # 使用正则表达式去除 xxx-xxx 这一串数字
    obj_no_digits = re.sub(r'\d+-\d+', '', file_name)

    # 使用正则表达式保留汉字、大小写英文字母和数字
    pinyin_name = ''.join(re.findall(r'[\u4e00-\u9ffa-zA-Z0-9]', obj_no_digits))

    # 将汉字转换为大写拼音首字母
    pinyin_name = pin.get_initials(pinyin_name, "").upper()

    # 根据比较结果修改文件名
    if width > height:
        pinyin_name += 'H'
    elif height > width:
        pinyin_name += 'S'

    # 重新组合文件名
    pinyin_name = pinyin_name.replace('.JPGS', 'S').replace('.JPGH', 'H')
    return pinyin_name
