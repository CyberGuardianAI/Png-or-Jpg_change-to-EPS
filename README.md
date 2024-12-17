# Png-or-Jpg_change-to-EPS
When submitting the final manuscript to IEEE, it is common to encounter image format requirements specifying EPS format. However, directly converting images from formats such as PNG or JPG to EPS may result in excessively large file sizes or compatibility issues. To address this challenge, I developed a Python program that efficiently converts PNG and JPG images to EPS while also performing compression and optimization. The program reduces the size of the resulting EPS files by adjusting the image resolution (DPI) and dimensions (with maximum width and height limits), ensuring that the output image quality meets IEEE requirements. This tool is user-friendly and automatically processes images in batch from a specified folder, saving the converted EPS files in a designated directory, thereby significantly improving the efficiency and controllability of image format conversion.
界面设置：

使用 tkinter 创建了一个窗口，包含了三个控件：
input_folder_entry：显示和选择输入文件夹路径。
output_folder_entry：显示输出文件夹路径（不可编辑，只显示）。
convert_button：点击按钮，开始执行转换过程。
文件夹选择功能：

使用 filedialog.askdirectory() 来让用户选择输入文件夹，该方法会弹出文件夹选择对话框。
输入文件夹选择后，自动生成输出文件夹路径，并显示在界面中。
图片转换与压缩：

通过 PIL （Pillow）库对选中的文件夹中的图片进行处理，转换为 EPS 格式，压缩图片并调整分辨率。
信息反馈：

处理完所有图片后，显示一个弹窗，告知用户成功转换了多少张图片，多少张图片转换失败。
可以修改的地方：
输入输出路径：

input_folder 和 output_folder 路径可以根据需要修改，或允许用户在界面中修改。
图片格式：

当前代码支持 .png, .jpg, .jpeg 格式的图片，如果需要支持其他格式，可以在 valid_extensions 中添加其他扩展名。
DPI 和图像尺寸限制：

你可以调整 MAX_DPI 和 MAX_SIZE 变量的值，以控制生成的 EPS 文件的质量和最大尺寸。
异常处理：

当前代码中如果出现无法识别的图片或文件格式，会输出错误信息。可以根据需求进一步优化异常处理机制，例如对不支持的文件类型做更多处理。
界面美化：

目前界面非常简单，可以使用 ttk 等模块增加控件的样式，或者对界面进行进一步的布局和优化。
日志和输出：

目前的输出在控制台中。如果你希望将处理日志显示在界面中，可以使用 Text 控件来实时显示处理信息。
运行步骤：
安装依赖：
PIL 可以通过命令 pip install pillow 安装。
运行脚本：
启动脚本后，会弹出 GUI 窗口，用户可以选择文件夹并开始图片转换。
这样，你就有了一个简单的 GUI 工具来处理图片的转换和压缩，可以轻松地上传图片并进行处理。
