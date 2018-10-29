## Use Python3 - and need to actually get wroking!

import numpy as np
from numpy import array as arr

with open("./datasets/rosalind_cons.txt", 'r') as f:
    A = [arr(list(line.strip())) for line in f]
    A = arr(A)

print(A)

genes = arr(list('ACGT'))
P = arr([(A == g).sum(axis=0) for g in genes])
c = genes[P.argmax(axis=0)]
c = ''.join(c)

print(c)
for i, g in enumerate(genes):
    print('%s:' % g, ' '.join(map(str, P[i])))