import os

# 替换为你想要检查目录的路径
dir_path = '/Users/js/notes'

try:
    # 获取目录下的所有文件和目录
    items = os.listdir(dir_path)

    for item in items:
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            print(item)
except Exception as e:
    print(f"发生错误: {e}")


#def list_files_in_directory(directory):
    #########try:
