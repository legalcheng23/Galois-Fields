import numpy as np

def gf_mult(a, b, mod=0x11b):
    """Multiplication in GF(2^8)"""
    p = 0
    while b:
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= mod
        b >>= 1
    return p

def gf_inv(a):
    """Find multiplicative inverse in GF(2^8)"""
    for i in range(256):
        if gf_mult(a, i) == 1:
            return i
    return 0

def affine_transform(x):
    """Affine transformation"""
    matrix = [
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 1],
    ]
    vector = [int(b) for b in f'{x:08b}']
    result = 0
    for i in range(8):
        bit = 0
        for j in range(8):
            bit ^= vector[j] * matrix[i][j]
        result |= (bit ^ 1) << (7 - i) 
    return result

# Generate the AES S-box
def generate_sbox():
    sbox = np.zeros(256, dtype=int)
    for i in range(256):
        inv = gf_inv(i)
        sbox[i] = affine_transform(inv)
    return sbox

sbox = generate_sbox()
print("AES S-box:")
print(sbox.reshape((16, 16)))

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
plt.imshow(sbox.reshape((16, 16)), cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('AES S-box')
plt.show()
