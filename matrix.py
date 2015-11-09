#!/usr/bin/python
import sys
def read_matrix(f, typee):
    """ read  matrix from file """
    A = []
    for line in f:
        # метод split() формирует список из слов строки
        # map(function, sequence) применяет функцию к каждому элементу
        # последовательности
        # list(sequence) формирует список из последовательности
        if typee == "int_t":
            A.append(list(map(int, line.split()))) 
        elif typee == "float_t":
            A.append(list(map(float, line.split()))) 
        else:
            print("Please, define the type of data")
            sys.exit()
    return A
def write_matrix(A):
    """ write matrix into console """
    for row in A:
        for elem in row:
            print(elem, end = ' ')
        print()
if __name__ == "__main__":
    print("This is a module! Please, import it")
