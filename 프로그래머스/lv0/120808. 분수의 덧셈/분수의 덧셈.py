import math
def solution(numer1, denom1, numer2, denom2):
    e,f = numer1*denom2+denom1*numer2,denom1*denom2
    gcd = math.gcd(e,f)
    if gcd != 1:
        e//=gcd
        f//=gcd
    print(e,f)
    return [e, f]
