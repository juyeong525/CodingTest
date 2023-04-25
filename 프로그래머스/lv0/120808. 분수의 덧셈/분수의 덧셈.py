import math
def solution(numer1, denom1, numer2, denom2):
    e,f = numer1*denom2+denom1*numer2,denom1*denom2
    a,b = e,f
    while b > 0:
        a, b = b, a % b
    gcd = a
    if gcd != 1:
        e//=gcd
        f//=gcd
    return [e, f]