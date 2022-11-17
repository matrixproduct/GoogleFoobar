# Idea of the algorithm:
#
# 1. Calculate the cycle index polynomials Z(S_w) and Z(S_h) for the corresponding symmetric groups (see e.g. [1])
# 2. Using the above result, calculate the cycle index polynomials Z(S_w x S_h) for their direct product and
# evaluate it at all arguments equal to s (see e.g. [2]).
#
# Polynomials are represented by lists of monomials, which have a structure [[n_1,...,n_r], c] corresponding to
# the term c * x_1^{n_1}...x_r^{n_r}

# References:
# [1] F. Harary "Graph Theory"
# [2] A. Atmaca, A.Y. Oruc "On The Number Of Unlabeled Bipartite Graphs"  https://arxiv.org/pdf/1705.01800.pdf

from copy import copy
from fractions import Fraction as frac
from fractions import gcd


def simplify_poly(P):
    ''' Simplifies polynomial by summing up similar monomials'''
    S = []
    for elem in P:
        new = True
        for term in S:
            if elem[0] == term[0]:
                term[1] += elem[1]
                new = False
                break
        if new:
            S.append(copy(elem))
    return S


def cycle_index(n, m):
    ''' Generates recursively the cycle index polynomials for
    the symmetric groups S_i for all i <= n assuming that n >= m.'''
    cycle_index_list = [[[[0 for _i in range(n)], 1]]] # list of  all cycle index polynomials up to certain degree
    for r in range(1, n + 1):  # number of recursive steps to generate Z(S_n)
        Z = []
        for i, poly in enumerate(cycle_index_list):
             Z += [[[elem[0][j] + 1 if j == r - i - 1 else elem[0][j] for j in range(n)], elem[1] * frac(1, r)]
                  for elem in poly]
        cycle_index_list.append(Z)
    return simplify_poly(cycle_index_list[n]), simplify_poly(cycle_index_list[m])


def solution(w, h, s):
    n, m = max(w, h), min(w, h)
    Z1, Z2 = cycle_index(n, m)
    gcd_matrix = [[gcd(j1 + 1, j2 + 1) for j2 in range(m)] for j1 in range(n)]
    return str(sum(elem1[1] * elem2[1] *
               s ** sum( q1 * q2 * gcd_matrix[j1][j2] for j1, q1 in enumerate(elem1[0]) for j2, q2 in enumerate(elem2[0][:m]))
               for elem1 in Z1 for elem2 in Z2))

# print(len(cycle_index(12, 12)[0]))
# print easter egg :)

# print(cycle_index(4, 1)[0])
# print(simplify_poly(cycle_index(4, 1)[0]))

# n = 12; m = 1
# print(len(cycle_index(n, m)[0]))
# print(len(simplify_poly(cycle_index(n, m)[0])))

n = 12; m = 12; s = 10
# print(cycle_index(n, m)[0])
print(solution(n, m, s))

# print(solution(2, 3, 4))
# output: 430