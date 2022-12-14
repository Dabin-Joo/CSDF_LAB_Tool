def LD(x):
    leng = 2
    z = list(map(''.join, zip(*[iter(x.hex())]*leng)))
    s = ''.join(reversed(z))
    return s