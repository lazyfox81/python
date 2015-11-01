#!/usr/bin/python
# Решение уравнения методом касательных
import math, sys
def newtons_method(x0, f, f1, eps):
    """ Реaлизация метода Ньютона """
    #f1 - производная
    n = 0
    while True:
        x1 = x0 - (f(x0) / f1(x0))
        print("%d  %.5f  %.5f  %.5f" % (n, x0, f(x0), f1(x0)))
        if abs(x1 - x0) < eps:
            return x1
        x0 = x1
def f(x):
    """ В правой части решаемое уравнение """
    try:
        y = math.log(x) + 4 * x
        return y
    except ValueError:
        print ("Invalid argument")
        sys.exit()
def f1(x):
    try:
        y = 1 / x + 4
        return y
    except ValueError:
        print ("Invalid argument")
        sys.exit()
def f11(x):
    try:
        y = -1 / (x * x)
        return y
    except ValueError:
        print ("Invalid argument")
        sys.exit()
def main():
    x = .1; eps = .001
    if f(x) * f11(x) < 0:
        print("the root is not suitable")
        sys.exit()
    x = newtons_method(x, f, f1, eps)
    print("\n%.5f" % (x))
# запуск программы
main()
