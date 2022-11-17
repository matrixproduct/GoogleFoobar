# from fractions import Fraction as frac
from math import gcd


class Frac:
    def __init__(self, num, den):
        d = gcd(num, den)
        self.numerator = num // d
        self.denominator = den // d

    def __repr__(self):
        """repr(self)"""
        return '%s(%s, %s)' % (self.__class__.__name__,
                               self.numerator, self.denominator)

    def __str__(self):
        """str(self)"""
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return '%s/%s' % (self.numerator, self.denominator)


    def __add__(self, other):
        """a + b"""
        a, b = self, other
        da, db = a.denominator, b.denominator
        return Frac(a.numerator * db + b.numerator * da,
                        da * db)
    def __sub__(self, other):
        """a - b"""
        a, b = self, other
        da, db = a.denominator, b.denominator
        return Frac(a.numerator * db - b.numerator * da,
                        da * db)

    def __mul__(self, other):
        """a * b"""
        a, b = self, other
        return Frac(a.numerator * b.numerator, a.denominator * b.denominator)

    def __truediv__(self, other):
        """a / b"""
        a, b = self, other
        return Frac(a.numerator * b.denominator,
                        a.denominator * b.numerator)

    def __neg__(self):
        """-a"""
        return Frac(-self.numerator, self.denominator)

    def convert_to_real(self):
        return self.numerator / self.denominator

#print(Frac(1,2)/Frac(1,4))

def lup_decompose(A):
    n = len(A)
    pi = [i for i in range(n)]
    for k in range(n):
        p = 0
        for i in range(k, n):
            if abs(A[i][k].convert_to_real()) > p:
                p = abs(A[i][k].convert_to_real())
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
    n = len(L)
    x = [Frac(0,1) for _i in range(n)]
    y = [Frac(0,1) for _i in range(n)]
    y[0] = b[pi[0]]
    for i in range(1, n):
        s = Frac(0,1)
        for j in range(i):
            s = s + L[i][j] * y[j]
        y[i] = b[pi[i]] - s
#        y[i] = b[pi[i]] - sum(L[i][j] * y[j] for j in range(0, i))
    for i in range(n - 1, -1, -1):
        s = Frac(0, 1)
        for j in range(i + 1, n):
            s = s + U[i][j] * x[j]
        x[i] = (y[i] - s)/U[i][i]
    return x


def convert_to_list(x):
    if len(x) == 1:
        return [x[0].numerator, x[0].denominator]
    common_den = x[0].denominator
    for i in range(1,len(x) - 1):
        common_den *=  x[i].denominator // gcd(common_den, x[i].denominator)
    return [elem.numerator * common_den // elem.denominator for elem in x] + [common_den]


def solution(m):
    trans_matrix = [[Frac(elem, sum(row)) for elem in row] for row in m if sum(row)]
    n, L = len(trans_matrix), len(m)
    Q = [[trans_matrix[i][j] for j in range(n)] for i in range(n)]
    R = [[trans_matrix[i][j] for j in range(n, L)] for i in range(n)]
    A = [[Frac(1,1) - Q[j][i] if i == j else -Q[j][i] for j in range(n)] for i in range(n)]
    A, pi = lup_decompose(A)
    b = [Frac(0,1) for _i in range(n)]; b[0] = Frac(1,1)
    x = lup_solve(A, A, pi, b)
    result = []
    for i in range(L - n):
        s = Frac(0, 1)
        for j in range(n):
            s = s + x[j] * R[j][i]
        result.append(s)
    return convert_to_list(result)

#print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
#print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))# print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
# a = [0, 3, 2, 9, 14]
# # print([elem / a[-1] for elem in a])
# print(a)