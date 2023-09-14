import os
from bs4 import BeautifulSoup


def copy_and_modify_html(source_dir, backup_dir):
    # 创建 backup 文件夹，如果不存在
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # 获取所有的文件
    for file_name in os.listdir(source_dir):
        # 仅处理 html 文件
        if file_name.endswith(".html"):
            # 获取完整的文件路径
            file_path = os.path.join(source_dir, file_name)

            # 读取原始文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                contents = file.read()
                soup = BeautifulSoup(contents, 'html.parser')

                # 删除所有 <img> 标签
                for img_tag in soup.find_all('img'):
                    img_tag.decompose()

                # 保存修改后的内容到 backup 文件夹
                backup_path = os.path.join(backup_dir, file_name)
                with open(backup_path, 'w', encoding='utf-8') as backup_file:
                    backup_file.write(str(soup))

# 使用方法：
copy_and_modify_html('xxx', 'xxx')