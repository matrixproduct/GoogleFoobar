from fractions import Fraction as frac


def lup_decompose(A):
    ''' LUP decomposition of A
        returns L and U as parts of A and P '''
    n = len(A)
    pi = [i for i in range(n)]
    for k in range(n):
        p = 0
        for i in range(k, n):
            if abs(A[i][k]) > p:
                p = abs(A[i][k])
                k_prime = i
        pi[k], pi[k_prime] = pi[k_prime], pi[k]
        for i in range(n):
            A[k][i], A[k_prime][i] = A[k_prime][i], A[k][i]
        for i in range(k + 1, n):
            A[i][k] = A[i][k]/A[k][k]
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - A[i][k] * A[k][j]
    return A, pi


def lup_solve(L, U, pi, b):
    '''Solves Ax=b, where L, U and pi are the LUP
      decomposition of A'''
    n = len(L)
    x = [0 for _i in range(n)]
    y = [0 for _i in range(n)]
    y[0] = b[pi[0]]
    for i in range(1, n):
        y[i] = b[pi[i]] - sum(L[i][j] * y[j] for j in range(0, i))
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1,n)))/U[i][i]
    return x


def gcd(a, b):
    ''' Returns the greatest common divisor of a and b'''
    return a // frac(a,b).numerator


def reorder(m):
    ''' Reorders the states in such a way that all terminal states are at the end
        Returns the reordered matrix m and the permutation vector of indices'''
    n = len(m)
    norm = [sum(row[:i] + row[i + 1:]) for i, row in enumerate(m)]
    pi = [elem[0] for elem in sorted(enumerate(norm), key=lambda i:i[1], reverse=True)]
    m1= [m[pi[i]] for i in range(n)]
    m2 =[[m1[i][pi[j]] for j in range(n)] for i in range(n)]
    return m2, pi


def convert_to_list(x):
    ''' Converts the final vector consisting of fractions
        to the required output format'''
    if len(x) == 1:
        return [x[0].numerator, x[0].denominator]
    common_den = x[0].denominator
    for i in range(1,len(x) - 1):
        common_den *=  x[i].denominator // gcd(common_den, x[i].denominator)
    return [elem.numerator * common_den // elem.denominator for elem in x] + [common_den]


def solution(m):
    ''' Solves the problem using the fact the matrix of absorption
        probabilities B = (I-Q)^(-1)R, where Q and R are defined below.
        see e.g https://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/Chapter11.pdf'''

    m_reordered, ind = reorder(m)  # put all ter,inal states at the end
    # collect all non-terminal states
    trans_matrix = [[frac(elem, sum(row)) for elem in row] for i, row in enumerate(m_reordered) if sum(row[:i] + row[i+1:])]
    n, L = len(trans_matrix), len(m)
    if sum(m[0][1:]) == 0:  # initial state is terminal
        return [1 if i == 0 or i == L - n else 0 for i in range(L - n + 1)]
    Q = [[trans_matrix[i][j] for j in range(n)] for i in range(n)]
    R = [[trans_matrix[i][j] for j in range(n, L)] for i in range(n)]
    A = [[1 - Q[j][i] if i == j else -Q[j][i] for j in range(n)] for i in range(n)]  # A = (I-Q)^T
    A, pi = lup_decompose(A)
    b = [1 if ind[i] == 0 else 0 for i in range(n)]  # corresponds to the initiale state
    x = lup_solve(A, A, pi, b)
    result = [sum(x[j] * R[j][i] for j in range(n)) for i in range(L - n)]  # x*R - matrix multiplication
    return convert_to_list(result)


