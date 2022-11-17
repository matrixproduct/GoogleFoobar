import numpy as np


def is_divisible(nums, factor):
    ''' nums is a np.array of numerators
       The function returns True is all of them are divisible by factor '''
    for elem in np.nditer(nums):
        if not elem % factor == 0:
            return False
    return True


def simplify(nums, den):
    ''' nums is a np.array of numerators, den is a denominator.
        The function cancels out all common factors '''
    factor = 2
    while factor < den:
        if den % factor == 0 and is_divisible(nums, factor):
            den = den // factor
            nums = nums // factor
        else:
            factor += 1
    return nums, den


def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        #  expanding along the first column i = 0
        #  index of the element is i+1,j+1 <-->  A[i][j]
        return sum([((-1) ** j) * A[0][j] * det(np.delete(np.delete(A, 0, 0), j, 1)) for j in range(n)])


def inverse(nums, den):
    ''' nums is a np.array of numerators, den is a denominator.
        The function returns the inverse matrix '''
    n = len(nums)
    if n == 1:
        return np.array([[den]]), nums[0,0]
    inv = np.zeros((n,n), dtype=np.int32)  # inverse matrix
    for i in range(n):
        for j in range(n):
            M = np.delete(nums, i, 0)
            M = np.delete(M, j, 1)
            inv[j][i] = ((-1) ** (i + j)) * np.rint(np.linalg.det(M)).astype(np.int32)
            # inv[j][i] = ((-1) ** (i + j)) * det(M)
    inv *= den
    return inv, np.rint(np.linalg.det(nums)).astype(np.int32)
    #return inv, det(nums)


def solution(m):
    # a = np.array([[1,5],[2,3]]); dena = 5
    # inva, new_den = inverse(a, dena)
    # print('inva/new_den = ', inva / new_den)
    # print('direct inverse ', np.linalg.inv(a/dena))
    # return
    #  trans_matrix = np.array([row / row.sum() for row in np.array(m) if sum(row)])
    # np.savetxt('test.out', m, delimiter=',')
    trans_matrix = np.array([row for row in m if sum(row)])
    den = 1  # common denominator for all matrix elements
    for row in trans_matrix:
        den *= row.sum()  # denominator is a product of denominators for each row
    for row in trans_matrix:  # properly normalise transition probabilities
        row *= den // row.sum()
    n = len(trans_matrix)
    Q, denQ = simplify(trans_matrix[:, :n], den)
    R, denR = simplify(trans_matrix[:, n:], den)
    N, denN = inverse(np.identity(n, dtype=np.int32) * denQ - Q, denQ)
    # print('N/new_den = ', N / new_den)
    # print('direct inverse ', np.linalg.inv(np.identity(n) - Q / den ))
    B, denB = simplify(np.matmul(N, R), denN * denR)
    # result = B[0].tolist() + [den]
    # print(result)
    return B[0].tolist() + [denB]


# solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
#print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
# a = [0, 3, 2, 9, 14]
# # print([elem / a[-1] for elem in a])
# print(a)