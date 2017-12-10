"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples_of(max_num, mutliples_of=[3, 5]):
    total = 0
    for i in range(max_num):
        for m in mutliples_of:
            if i % m == 0:
                total += i
                break

    return total
