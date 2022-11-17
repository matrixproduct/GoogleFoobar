# n = num_buns, k = num_required - 1
# The key observation: if S ={1,..., m} is a set of all keys
# and S[j] is a subset of S representing an individual bunny's set of keys, then defining D[j] as S - S[j],
# we notice that D[j] have two properties:
# i) intersection of any k sets from {D[j]} is empty
# ii) intersection of any (k-1) sets from {D[j]} is not empty
# From this observation we conclude that elements of D[j] are given by D[j][i_1][i_2]...[i_(k-1)],
# where  D[j][i_1][i_2]...[i_(k-1)] is a common element for sets D[j], D[i_1], ...,D[i_(k-1)]
# This allows us to construct a solution using the following algorithm:

# 1. Define A = {0,...,n-1}
# 2. Define m = C(n,k) and S = {0,1,..., m-1}
# 3. Define P = {combinations of k elements from A}, notice that |P| = m
# 4. Define f: P -> S, f(a[0], a[1],..., a[k-1]) is a reverse index of (a[0],...,a[k-1]) in set P.
# 5. For j in A define D[j] = {f(a[0], a[1],..., a[m-1]), where a[0] = j}
# 6. Define S[j] = S - D[j], sort it and return [list(S[0]), list(S[1]), ..., list(S[n-1])]


from itertools import combinations


def solution(num_buns, num_required):
    n, k = num_buns, num_required - 1
    if k == -1:
        return [[] for _i in range(n)]
    if n < k + 1:
        return "impossible"
    D = [set() for _i in range(n)]
    A = range(n)
    P = list(combinations(A, k))
    m = len(P)
    S = set(range(m))
    for ind, comb in enumerate(P):
        for elem in comb:
            D[elem].add(m - 1 - ind)
    return [sorted(list(S - Dj)) for Dj in D]


from itertools import combinations
from math import factorial


def nCr(n,r):
    f = factorial
    return f(n) // f(r) // f(n-r)


def solution_first(num_buns, num_required):
    n, k = num_buns, num_required - 1
    if k == -1:
        return [[] for _i in range(n)]
    if num_buns < num_required:
        return "impossible"
    D = [set() for _i in range(n)]
    A = range(n)
    m = nCr(n, k)
    S = set(range(m))
    P = combinations(A, k)
    for ind, comb in enumerate(P):
        for elem in comb:
            D[elem].add(m - 1 - ind)
    return [sorted(list(S - Dj)) for Dj in D]


def solution_check(num_buns, num_required):
    n, k = num_buns, num_required - 1
    if k == -1:
        return [[] for _i in range(n)]
    if num_buns < num_required:
        return "impossible"
    D = [set() for _i in range(n)]
    A = range(n)
    P = list(combinations(A, k))
    m = len(P)
    S = set(range(m))
    for ind, comb in enumerate(P):
        for elem in comb:
            D[elem].add(m - 1 - ind)
    res = [sorted(list(S - Dj)) for Dj in D]
    is_order = True
    for i in range(n - 1):
        for k in range(len(res[0])):
            if res[i][k] < res[i + 1][k]:
                break
            if res[i][k] > res[i + 1][k]:
                return False
    # print(is_order)
    return is_order
#    return [list(S - Dj) for Dj in D]


# for n in range(1, 10):
#     for req in range(1, n + 1):
#         if not solution(n, req):
#             print (n, req, 'no order')
#
# print(solution_first(5, 4))

# print(solution(5, 3))
# [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]

# n = num_buns, k = num_required - 1
# The key observation: if S ={1,..., m} is a set of all keys
# and S[j] is a subset of S representing an individual bunny's set of keys, then defining D[j] as S - S[j],
# we notice that D[j] have two properties:
# i) intersection of any k sets from {D[j]} is empty
# ii) intersection of any (k-1) sets from {D[j]} is not empty
# From this observation we conclude that elements of D[j] are given by D[j][i_1][i_2]...[i_(k-1)],
# where  D[j][i_1][i_2]...[i_(k-1)] is a common element for sets D[j], D[i_1], ...,D[i_(k-1)]
# This allows us to construct a solution using the following algorithm:

# 1. Define A = {0,...,n-1}
# 2. Define m = C(n,k) and S = {0,1,..., m-1}
# 3. Define P = {combinations of k elements from A}, notice that |P| = m
# 4. Define f: P -> S, f(a[0], a[1],..., a[k-1]) is a reverse index of (a[0],...,a[k-1]) in set P.
# 5. For j in A define D[j] = {f(a[0], a[1],..., a[m-1]), where a[0] = j}
# 6. Define S[j] = S - D[j], sort it and return [list(S[0]), list(S[1]), ..., list(S[n-1])]


from itertools import combinations


def solution(num_buns, num_required):
    n, k = num_buns, num_required - 1
    if k == -1:
        return [[] for _i in range(n)]
    if n < k + 1:
        return "impossible"
    D = [set() for _i in range(n)]
    A = range(n)
    P = list(combinations(A, k))
    m = len(P)
    S = set(range(m))
    for ind, comb in enumerate(P):
        for elem in comb:
            D[elem].add(m - 1 - ind)
    return [sorted(list(S - Dj)) for Dj in D]