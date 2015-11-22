#!/usr/bin/python
# Systems of Linear Equations: Solving by Gaussian Elimination
import matrix
def main_elem(A):
    """ Выбор главного элемента """
    max_elem = 0
    row_max = 0
    for i in range(len(A)):
        """ Ищем максимальный по модулю элемент при Х1 """
        if abs(A[i][0]) > abs(max_elem):
            max_elem = A[i][0]
            row_max = i
    print(max_elem, end="  ")
    print(row_max)
    if row_max != 0:
        """ Ставим уравнение с максимальным первым членом на первое место """
        A[0], A[row_max] = A[row_max], A[0]
def main():
    with open("linear_sys.txt", "r", encoding='utf-8') as inf:
        A = matrix.read_matrix(inf, "float_t")
    # print(A)
    matrix.write_matrix(A)
    print()
    main_elem(A)
    matrix.write_matrix(A)
# start the programm
main()
