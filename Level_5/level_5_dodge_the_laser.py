# Algorithm is based on Rayleigh's theorem for a Beatty sequence (https://en.wikipedia.org/wiki/Beatty_sequence)
# If r>1 is irrational, define s = r/(r-1), then any positive integer number is either an element of
# the sequences [r*n] or [s*n].
# If S(r, n) = sum_{k=1}^n [r*k] and m=[r*n] then it follows from the above theorem that
# S(r, n) + S(s, [m/s]) = sum_{k=1}^m = m(m+1)/2
# [m/s] = [m(1-1/r)]=: l =>
# S(r,n) = m(m+1)/2 - S(s,l)
# In particular, for r=sqrt(2) , s= 2+sqrt(2) and hence
# S(sqrt(2), n) = m(m+1)/2  - S(2+sqrt(2), l) = m(m+1)/2 -l(l+1) - S(sqrt(2), l)
# and therefore the sum can be calculated recursively
# The only thing we need to be able to calculate accurately is m = [(sqrt(2)*n] and l = m - [m/sqrt(2)].
# This can be done using Decimal module.


from decimal import Decimal, getcontext

getcontext().prec = 101


def rec_sum(n):
    if n == 0:
        return 0
    m = int(n * Decimal(2).sqrt())
    l = int(m - m / Decimal(2).sqrt())
    return m * (m + 1) / 2 - l * (l + 1) - rec_sum(l)


def solution(str_n):
    return str(rec_sum(int(str_n)))



# for i in range(20):
#     print(cont_frac(i+1))
#
# print('cont_frac')
# print(cont_frac(5))

# print(solution('77'))

# print(solution('1'*100))
#print(solution('23223423'))
#print(solution_git('23223423'))
# str_n = '9'*70
# n =Decimal(str_n)
# sq = Decimal(2).sqrt()
# print(int(int(n * sq) / sq) == n)
# print(solution(str_n) == solution_git(str_n))
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