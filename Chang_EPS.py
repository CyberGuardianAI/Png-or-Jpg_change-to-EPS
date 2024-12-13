import os
from PIL import Image, UnidentifiedImageError

# 设置输入路径和输出路径
input_folder = r"C:\Users\xxxxx"  # 修改为你的文件夹路径
output_folder = os.path.join(input_folder, "EPS_Output")
os.makedirs(output_folder, exist_ok=True)  # 如果不存在，创建输出文件夹

# 支持的图片扩展名
valid_extensions = ['.png', '.jpg', '.jpeg']

# 最大输出分辨率（例如 150 DPI），可以根据需求调整
MAX_DPI = 150
# 限制图片最大尺寸，例如宽高都不超过 1024 像素
MAX_SIZE = (1024, 1024)

# 遍历文件夹
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    # 检查文件是否是图片格式
    if any(filename.lower().endswith(ext) for ext in valid_extensions):
        try:
            # 打开图片
            with Image.open(file_path) as img:
                # 转换为RGB模式（去除透明通道）
                if img.mode not in ['RGB', 'L']:
                    print(f"转换模式: {filename} 从 {img.mode} 到 RGB")
                    img = img.convert('RGB')

                # 降低分辨率，缩小图片尺寸
                img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)

                # 构建输出文件路径
                output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".eps")
                # 保存为EPS格式，限制DPI
                img.save(output_path, format='EPS', dpi=(MAX_DPI, MAX_DPI))
                print(f"成功转换并压缩: {filename} -> {output_path}")
        except UnidentifiedImageError:
            print(f"无法识别的图片文件: {filename}")
        except Exception as e:
            print(f"文件处理错误 {filename}: {e}")
    else:
        print(f"跳过非图片文件: {filename}")

print("图片转换与压缩完成。")
