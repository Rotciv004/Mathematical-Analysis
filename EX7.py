#import math

"""Arătați numeric că∑n≥1(−1)n+1n= ln 2. Schimbați ordinea însumării în această serie – de exemplu, adăugând mai întâi termeni pozitivi, apoi termeni
negativi și așa mai departe – și arătați numeric că rearanjarea dă o sumă diferită (în funcție de p, q)."""

def original_sum(N) -> float:
    """
    :param N: Number of the termens in our sum
    :return: Result is our sum
    """
    total = 0

    for i in range(1, N + 1):
        total += ((-1) ** (i + 1)) / i

    return total




def rearranged_sum(N, p, q) -> float:
    """
    :param N: Number of the terms in our sum
    :param p: Positive terms
    :param q: Negative terms
    :return: Result is our rearranged sum
    """

    total = 0
    pos_sum = 0
    neg_sum = 0

    for i in range(1, N + 1):
        if i % (p + q) <= p:
            pos_sum += 1 / i

        else:
            neg_sum += 1 / i

        total = pos_sum - neg_sum


    return total





# Number of terms to consider in the series
N = int(input("Input the number of terms from our sum -> "))

# Print the results
print("Original sum: " + str(original_sum(N)))
print("Rearranged sum (p=3, q=2): " + str(rearranged_sum(N,3,2)))
