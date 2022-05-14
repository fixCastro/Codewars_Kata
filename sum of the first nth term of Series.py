def series_sum(n):
    # Happy Coding ^_^
    return '{:.2f}'.format(sum(1/(1+i*3) for i in range(n)))

print(series_sum(100000))