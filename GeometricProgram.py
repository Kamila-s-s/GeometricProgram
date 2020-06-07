import math
from itertools import *

def combination(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0

m, s = 2, 3
print("Шаг: ", 1)
print("m = ", m)
print("S = ", s)
for i in range(2, 15):
    print("Шаг: ", i)
    a = 2 * m + math.ceil(math.log2(combination(s * s, 2)))
    m = a
    s = s * s
    print("m = ", a)
    print("s = ", s)
