from rpy2 import robjects #в настройках основного интерпретатора нужно по классике закаать необходимый модуль (он так и называется pry2)

def function1(input, output):
    r = robjects.r
    r.source("rtest.R")
    p = r.rtest(input, output)
    return p

if __name__ == '__main__':
    a = function1(12, 12)