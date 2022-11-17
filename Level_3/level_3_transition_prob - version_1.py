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
    while factor < den // 2 + 2:
        if den % factor == 0 and is_divisible(nums, factor):
            den = den // factor
            nums = nums // factor
        else:
            factor += 1
    return nums, den


def solution(m):
    trans_matrix = np.array(m)
    terminal_indx = []  # list of terminal states
    den = 1  # common denominator for all matrix elements
    for i, row in enumerate(trans_matrix):
        if row.sum():
            den *= row.sum()  # denominator is a product of denominators for each row
        else:
            row[i] = 1  # redefine terminal states correctly assigning 1 as the transition probability from s_i to s_i
            terminal_indx.append(i)  # save the index of a terminal state
    for row in trans_matrix:  # properly normalise transition probabilities
        row *= den // row.sum()
    trans_matrix = np.transpose(trans_matrix)
    trans_matrix, den = simplify(trans_matrix, den)
    # print(trans_matrix, den)
    x0 = np.zeros_like(trans_matrix[0]); x0[0] = 1  # initial state
    d0 = 1  # initial denominator for the state
    while True:
        x1 = np.matmul(trans_matrix, x0)
        d1 = d0 * den
        x1, d1 = simplify(x1, d1)
        if np.array_equal(x0, x1):
            result = []
            for ind in terminal_indx:
                result.append(x1[ind])
            result.append(d1)
            return result
        x0, d0 = x1, d1


print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))