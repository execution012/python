import os
from PIL import Image

def resize_image(folder_path, output_size, save_option):
    if save_option == 1:  # 保存到新文件夹
        new_folder_path = os.path.join(folder_path, "resized_images")
        os.makedirs(new_folder_path, exist_ok=True)
        target_path = new_folder_path
    else:  # 直接覆盖原图片
        target_path = folder_path

    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        if os.path.isfile(image_path):
            with Image.open(image_path) as img:
                resized_img = img.resize(output_size)
                if save_option == 1 or save_option == 2:
                    save_path = os.path.join(target_path, image_name)
                else:
                    # 原路径但不覆盖，创建带后缀的新文件名
                    base_name, ext = os.path.splitext(image_name)
                    save_path = os.path.join(folder_path, f"{base_name}_resized{ext}")
                resized_img.save(save_path)
