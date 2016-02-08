#!/usr/bin/python
# Решение уравнений методом дихотомии
import math, sys
def f(x):
    """ В правой части решаемое уравнение """
    try:
        y = math.log(x) + 4 * x
        return y
    except ValueError:
        print ("Invalid argument")
        sys.exit()
def div_half(a, b, f, eps):
    """ Метод дихотомии """
    n = 0
    if f(a) * f(b) > 0:
        print("No solution")
        sys.exit()
    while True:
        x = (a + b) / 2
        y = [f(a), f(b), f(x)]
        sign = ["0", "0", "0"]
        m = 0
        for yy in y:
            if yy > 0:
                sign[m] = "+"
            else:
                sign[m] = "-"
            m+=1
        print("%d   %.5f   %s   %s"  % ( n, a, sign[0], sign[1]), end=" ")
        print("%.5f   %.5f   %s" % (b, x, sign[2]))
        if y[0]*y[2] > 0:
            a = x
        else:
            b = x
        n+=1
        if (b - a) <= eps:
            break
    x = (a + b) / 2
    return x
def main():
    # a = float(input("Введите левую границу: "))
    # b = float(input("Введите правую границу: "))
    # eps = float(input("Введите точность: "))
    a = .000001; b = 1; eps = .001
    x = div_half(a, b, f, eps)
    print("\n%.5f" % (x))
# запуск программы
main()
