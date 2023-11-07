from PIL import Image
import os

# 指定图片文件夹的路径
image_folder = 'D:/ImageNet/.encoding/data/ILSVRC2012/val_1-50000'

# 遍历文件夹中的所有文件
for filename in os.listdir(image_folder):

    if filename.endswith(('.jpg', '.JPEG', '.png', '.gif', '.bmp')):  # 可以根据需要扩展支持的图片格式
        # 拼接文件的完整路径
        file_path = os.path.join(image_folder, filename)
        # 打开图片文件
        img = Image.open(file_path)

        # 调整图片大小为224x224
        img = img.resize((224, 224))

        # 保存调整后的图片
        img.save(file_path)

        # 关闭图片文件
        img.close()
