import numpy as np

def hill_cipher_encrypt(plaintext, key):
    key_matrix = np.array(key)
    plaintext_vec = [ord(c) - ord('A') for c in plaintext]
    result = np.dot(key_matrix, plaintext_vec) % 26
    return ''.join(chr(int(r) + ord('A')) for r in result)

print(hill_cipher_encrypt("HEL", [[6, 24, 1], [13, 16, 10], [20, 17, 15]]))
