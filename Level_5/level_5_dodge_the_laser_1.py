# Algorithm is based on Rayleigh's theorem for a Beatty sequence (https://en.wikipedia.org/wiki/Beatty_sequence)
# # if r>1 is irrational, define s = r/(r-1), then any positive integer number k is an element of one of
# the sequences [r*n] or [s*n].
# If S(r, n) = sum_{k=1}^n [r*k] and m=[r*n] then it follows from the above theorem that
# S(r, n) + S(s, [m/s]) = sum_{k=1}^m = m(m+1)/2
# [m/s] = [m(1-1/r)] = m - [m/r] = m - n = [(r-1)*n] =: l =>
# S(r,n) = (l+n)(l+n+1)/2 - S(s,l)
# In particular, for r=sqrt(2) , s= 2+sqrt(2) and hence
# S(sqrt(2), n) = (l+n)(l+n+1)/2 - S(2+sqrt(2), l) = (l+n)(l+n+1)/2 -l(l+1) - S(sqrt(2), l)
# and therefore the sum can be calculated recursively
# The only thing we need to be able to calculate accurately is l = [(sqrt(2)-1)*n]
# This can be done using the continued fraction representation sqrt(2) - 1 = 1/(2+1/(2+1/(2+...

from math import floor


def cont_frac(num_digits):
    '''Returns sqrt(2) - 1 with the correct num_digits digits after the decimal point '''
    f1, f2 = 0, 0.5
    while str(f1)[:num_digits + 3] != str(f2)[:num_digits + 3]:
        f1, f2 = f2,  1. / (2 + f2)
    return f2


def rec_sum(n):
    if n == 0:
        return 0
    num_digits = len(str(n)) + 1
    l = int(floor(cont_frac(num_digits) * n))
    return (l + n) * (l + n + 1) / 2 - l * (l + 1) - rec_sum(l)

def solution(str_n):
    return str(rec_sum(int(str_n)))



# for i in range(20):
#     print(cont_frac(i+1))
#
# print('cont_frac')
# print(cont_frac(5))

print(solution('1'))

# print(solution('1'*100))
#print(solution('23223423'))
# output 381362049543566

#
# Input:
# solution.solution('77')
# Output:
#     4208
#
# Input:
# solution.solution('5')
# Output:
#     19