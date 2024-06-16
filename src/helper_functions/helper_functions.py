
def luby_sequence(i):
    k = 1
    while (1 << (k - 1)) <= i + 1:
        k += 1
    k -= 1
    if i + 1 == (1 << k) - 1:
        return 1 << (k - 1)
    else:
        return luby_sequence(i - (1 << (k - 1)) + 1)
