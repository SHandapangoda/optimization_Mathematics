from collections.abc import Sequence

def simpson_rule(x: Sequence[float], f: Sequence[float]) -> float:
    N =len(x) - 1
    h = [x[i+1] - x[i] for i in range(0,N)]
    assert N>0

    res = 0.0

    for i in range(1, N, 2):
        h0, h1, = h[i-1], h[i]
        hph, hdh, hmh = h1 + h0, h1 / h0, h1 * h0
        res += (hph / 6 ) * ((2 - hdh) * f[i-1] + (hph ** 2 / hmh) * f[i] + (2 - 1 / hdh) * f[i+1])

    if N % 2 == 1:
        h0, h1 = h[N - 2], h[N - 1]
        res += f[N] * (2 * h1 ** 2 + 3 * h0 * h1) / (6 * (h0 + h1))
        res += f[N - 1] * (h1 ** 2 + 3 * h1 * h0) / (6 * h0)
        res += f[N - 2] * h1 ** 3 / (6 * h0 * (h0 + h1)) 
    
    return res
