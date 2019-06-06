def hello():
    print('=== hello ===')
    print('当前hello的name: %s ' % __name__)


def hello_one():
    print('== hello one ==')


def get_c(a, b):
    return lambda x: a*x + b


if __name__ == '__main__':
    c = get_c(12, 13)
    print(c(3))
    hello()

