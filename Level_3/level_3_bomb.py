# For a given state (M, F) we can generate two new possible states: (M+F, F) or (F, F+M).
# The key observation is that a given state (M, F) can be reached only from
# a unique state (M-F, F) for M > F or (M, F-M) for M < F.
# This implies i) a state of the type (M, M) can't be reached
# ii) it is easier to go backwards from the final state and check weather we can arrive
# to the initial state (1,1)
# If M > F, then we need to subtract F from M so many time until M becomes not larger than F and vice versa.


def solution(x, y):
    x, y = int(x), int(y)
    gens = 0
    while x != y:
        if x > y:
            steps = (x - y) // y + ((x - y) % y != 0)
            x -= steps * y
        else:
            steps = (y - x) // x + ((y - x) % x != 0)
            y -= steps * x
        gens += steps
    if (x, y) == (1, 1):
        return str(gens)
    return "impossible"


# print(solution(str(10 ** 50), '3'))
# print(solution('4', '7'))