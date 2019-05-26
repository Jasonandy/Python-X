"""
我们来完成1~100000000求和的计算密集型任务，
这个问题本身非常简单，有点循环的知识就能解决，代码如下所示。

1.执行会比较慢
计算的结果时间大概在： 9.030秒左右 cpu 90%
4999999950000000

2.优化为多线程
 1.6980969905853271 秒左右
5000000050000000


使用多进程后由于获得了更多的CPU执行时间以及更好的利用了CPU的多核特性，明显的减少了程序的执行时间，而且计算量越大效果越明显。
当然，如果愿意还可以将多个进程部署在不同的计算机上，做成分布式进程，
具体的做法就是通过multiprocessing.managers模块中提供的管理器将Queue对象通过网络共享出来
（注册到网络上让其他计算机可以访问）

这部分内容也留到爬虫的专题再进行讲解
"""
from multiprocessing import Process, Queue
from time import time


def no_thread():
    total = 0
    number_list = [x for x in range(1, 100000000)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def has_thread():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    # queue 队列
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算 [分8个线程去跑]
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    # 将queue里面的8个结果+ 起来
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


def main():
    # no_thread()
    has_thread()


if __name__ == '__main__':
    main()

