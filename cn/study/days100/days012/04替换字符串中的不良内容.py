import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[艹操]|fuck|shit|傻[比吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)


if __name__ == '__main__':
    main()

