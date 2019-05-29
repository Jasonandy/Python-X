import os
import sys
import cn.study.days100.days019.hello as aa


def print_file_path():
    parent_dir_name = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(parent_dir_name)
    print(parent_dir_name)
    return parent_dir_name


def print_a():
    print(print_file_path())
    print('=== a ===')
    print(__name__)
    aa.hello()
    aa.hello_one()


if __name__ == '__main__':
   print_a()



















