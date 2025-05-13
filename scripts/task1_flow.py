import os
import sys
import re


def check_folder(student_id) -> tuple[bool, list]:
    folder_path = f"Class_member/{student_id}"
    error_list = []

    # 1. 檢查資料夾是否存在
    if not os.path.isdir(folder_path):
        error_list.append(f"錯誤：{folder_path} 資料夾不存在")

    # 如果資料夾存在，才進行後續檢查
    if os.path.isdir(folder_path):
        contents = os.listdir(folder_path)

        # 2. 檢查是否有 .md 文件
        md_files = [f for f in contents if f.endswith('.md')]
        if not md_files:
            error_list.append(f"錯誤：{folder_path} 中沒有 .md 文件")
        elif len(md_files) > 1:
            error_list.append(f"錯誤：{folder_path} 中有多個 .md 文件")

        # 3. 檢查是否有 images 資料夾
        if 'images' not in contents or not os.path.isdir(os.path.join(folder_path, 'images')):
            error_list.append(f"錯誤：{folder_path} 中沒有 images 資料夾")

        # 4. 檢查是否只有 .md 文件和 images 資料夾
        if md_files:  # 確保有 .md 文件才檢查
            allowed_items = {md_files[0], 'images'}
            if set(contents) != allowed_items:
                error_list.append(f"錯誤：{folder_path} 中包含不允許的文件或資料夾")

        # 5. 檢查 .md 文件內容
        if md_files:  # 只有在有 .md 文件時才檢查內容
            md_file_path = os.path.join(folder_path, md_files[0])
            with open(md_file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            name_pattern = r"姓名:\s*[^\n]+"
            id_pattern = rf"學號:\s*{student_id}"
            github_pattern = r"Github 帳號:\s*!\[\]\(\./images/[^\)]+\)"

            if not re.search(name_pattern, content):
                error_list.append(f"錯誤：{md_file_path} 中缺少 '姓名' 欄位或格式不正確")
            if not re.search(id_pattern, content):
                error_list.append(f"錯誤：{md_file_path} 中的學號與資料夾名稱 {student_id} 不符")
            if not re.search(github_pattern, content):
                error_list.append(f"錯誤：{md_file_path} 中的圖片不正確，應為 ![](./images/...)")

    # 如果沒有錯誤，則成功
    success = len(error_list) == 0
    if success:
        print(f"{student_id} 符合")
    return success, error_list

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("錯誤：請提供 student_id 作為參數")
        sys.exit(1)

    student_id = sys.argv[1]
    success, errors = check_folder(student_id)
    if success:
        sys.exit(0)
    else:
        print("提交不符合：")
        for error in errors:
            print(error)
        sys.exit(1)