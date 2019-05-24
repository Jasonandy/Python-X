import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 最后一个字符的位置 size - 1
    last_pos = len(all_chars) - 1
    # 验证码
    code = ''
    # 需要遍历的长度 默认为4
    for _ in range(code_len):
        # 字符串里面随机取出一个字符 循环拼接
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    for _ in range(1, 10):
        print(generate_code().lower())
        print(generate_code(12).upper())

