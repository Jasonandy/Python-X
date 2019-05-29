def hello():
    print('=== hello ===')
    print('当前hello的name: %s ' % __name__)


def hello_one():
    print('== hello one ==')


if __name__ == '__main__':
    hello()

