def recur_sum(x, y):
    if (y == 1):
        return x
    else:
        return x + recur_sum(x, y - 1)


print(recur_sum(5,5))
