import tempfile


def subject_files_repository(file_suffix: str, file_list: list):
    temp_path = tempfile.TemporaryDirectory(prefix="./", suffix=file_suffix)
    for i in file_list:
        if str(i[0]).endswith(file_suffix):
            temp_file = open(temp_path.name + "/" + i[0], "w", encoding="utf-8")
            temp_file.write(i[1])
            temp_file.close()
    return temp_path
