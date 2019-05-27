def rec_sum_digits(n):
    n=str(n)
    if len(n)==0:
        return 0
    return int(n[0])+rec_sum_digits(n[1:])
