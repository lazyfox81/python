#!/usr/bin/python
# Input matrix from file
def read_matrix(f):
    """ read  matrix from file """
    A = []
    for line in f:
        # метод split() превращает строку в список
        # map преобразует аргумент в int
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

