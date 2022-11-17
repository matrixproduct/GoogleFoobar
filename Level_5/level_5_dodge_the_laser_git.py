from decimal import Decimal, getcontext

getcontext().prec = 101  # Allow for at least 100 digits

SQRT2 = Decimal(2).sqrt()  # Use decimal for better precision


def beatty(n):
    """
    Return the sum of the integer portions of i * r for all numbers in the
    range 1..n inclusive.
    """
    r = SQRT2
    if n == 0:
        return 0

    # Calculate m and n'
    m = int(n * r)
    n_prime = int(m - (m / r))

    # m * (m + 1) / 2 - S(s, n')
    return (
        m * (m + 1) / 2
        - n_prime * (n_prime + 1)
        - beatty(n_prime)  # Recurse from n'
    )


def solution_git(str_n):
    n = int(str_n)

    # Initial bounds check
    #if n < 1 or n > 10**100:
    #   return str(0)

    # Special case for n = 1
    #if n == 1:
    #    return str(1)

    # Return the sum of the Beatty sequence S(sqrt(2), n)
    return str(beatty(n))