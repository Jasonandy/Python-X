def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print("--- 返回指定文件名的后缀 ---")
    print(get_suffix("deepv_for_1604_docker_1.4.3_20181022_2.tgz", True))
    print("== 文件的后缀名如上所示 ===")

