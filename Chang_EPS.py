import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, UnidentifiedImageError


# 设置输入路径和输出路径
def select_folder():
    # 选择文件夹
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        input_folder_var.set(folder_selected)
        output_folder = os.path.join(folder_selected, "EPS_Output")
        output_folder_var.set(output_folder)
        os.makedirs(output_folder, exist_ok=True)  # 如果不存在，创建输出文件夹


def convert_images():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()

    if not input_folder:
        messagebox.showerror("错误", "请选择输入文件夹！")
        return

    if not os.path.exists(input_folder):
        messagebox.showerror("错误", "输入文件夹路径无效！")
        return

    # 支持的图片扩展名
    valid_extensions = ['.png', '.jpg', '.jpeg']

    # 最大输出分辨率（例如 150 DPI），可以根据需求调整
    MAX_DPI = 150

    # 限制图片最大尺寸，例如宽高都不超过 1024 像素
    MAX_SIZE = (1024, 1024)

    success_count = 0
    error_count = 0

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
                        img = img.convert('RGB')

                    # 降低分辨率，缩小图片尺寸
                    img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)

                    # 构建输出文件路径
                    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".eps")
                    # 保存为EPS格式，限制DPI
                    img.save(output_path, format='EPS', dpi=(MAX_DPI, MAX_DPI))
                    success_count += 1
                    print(f"成功转换并压缩: {filename} -> {output_path}")
            except UnidentifiedImageError:
                error_count += 1
                print(f"无法识别的图片文件: {filename}")
            except Exception as e:
                error_count += 1
                print(f"文件处理错误 {filename}: {e}")
        else:
            print(f"跳过非图片文件: {filename}")

    messagebox.showinfo("完成", f"图片转换与压缩完成！成功转换 {success_count} 张图片，失败 {error_count} 张。")


# 创建主界面
root = tk.Tk()
root.title("图片转换与压缩为EPS")

# 设置界面尺寸
root.geometry("400x300")

# 输入文件夹选择
input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()

input_folder_label = tk.Label(root, text="选择图片文件夹:")
input_folder_label.pack(pady=10)

input_folder_entry = tk.Entry(root, textvariable=input_folder_var, width=40)
input_folder_entry.pack(pady=5)

select_folder_button = tk.Button(root, text="选择文件夹", command=select_folder)
select_folder_button.pack(pady=10)

output_folder_label = tk.Label(root, text="输出文件夹:")
output_folder_label.pack(pady=10)

output_folder_entry = tk.Entry(root, textvariable=output_folder_var, width=40, state='readonly')
output_folder_entry.pack(pady=5)

# 转换按钮
convert_button = tk.Button(root, text="开始转换", command=convert_images)
convert_button.pack(pady=20)

# 运行界面
root.mainloop()
