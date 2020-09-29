import time
import sys
import os
from multiprocessing import Process, freeze_support


def info(title):
    if hasattr(os, 'getppid'):  # only available on Unix
        print('{0}:\tPID={1} PPID={2}'.format(title, os.getpid(), os.getppid()))
    else:
        print('{0}:\tPID={1}'.format(title, os.getpid()))


def fun(name):
    info('порождённый процесс')
    print('процесс {0} выполняет функцию с параметром {1}'.format(os.getpid(), name))
    time.sleep(0.5)


if __name__ == '__main__':
    freeze_support()
    nproc = len(sys.argv) > 1 and int(sys.argv[1]) or 3
    print('число дочерних процессов ', nproc)
    info('родительский процесс')
    procs = []
    for i in range(nproc):
        procs.append(Process(target=fun, args=(i,)))
    for i in range(nproc):
        procs[i].start()
    for i in range(nproc):
        procs[i].join()
    print('завершается родительский процесс')

    None