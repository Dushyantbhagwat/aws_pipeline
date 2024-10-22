def playfair_encrypt(plaintext, key):
    matrix = []
    for c in key.upper():
        if c not in matrix and c != 'J':
            matrix.append(c)
    for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if c not in matrix:
            matrix.append(c)
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_pos(c):
        for i, row in enumerate(matrix):
            if c in row:
                return i, row.index(c)

    def encrypt_pair(a, b):
        r1, c1 = find_pos(a)
        r2, c2 = find_pos(b)
        if r1 == r2:
            return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        if c1 == c2:
            return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        return matrix[r1][c2] + matrix[r2][c1]

    ciphertext = ""
    plaintext = plaintext.upper().replace("J", "I")
    for i in range(0, len(plaintext), 2):
        if i+1 >= len(plaintext) or plaintext[i] == plaintext[i+1]:
            ciphertext += encrypt_pair(plaintext[i], 'X')
        else:
            ciphertext += encrypt_pair(plaintext[i], plaintext[i+1])
    return ciphertext

print(playfair_encrypt("HELLO", "KEYWORD"))
