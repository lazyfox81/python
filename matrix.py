#!/usr/bin/python
# Input matrix from file
def read_matrix(f):
    """ read  matrix from file """
    A = []
    for line in f:
        # метод split() формирует список из слов строки
        # map(function, sequence) применяет функцию к каждому элементу
        # последовательности
        # list(sequence) формирует список из последовательности
        A.append(list(map(int, line.split()))) 
    return A
def write_matrix(A):
    for row in A:
        for elem in row:
            print(elem, end = ' ')
        print()
with open("matrix.txt", "r", encoding='utf-8') as inf:
    A = read_matrix(inf)
print(A)
write_matrix(A)

