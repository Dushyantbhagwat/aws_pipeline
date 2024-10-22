def vigenere_encrypt(plaintext, key):
    key = (key * len(plaintext))[:len(plaintext)]  # repeat key
    ciphertext = ''
    for i in range(len(plaintext)):
        c = (ord(plaintext[i]) + ord(key[i]) - 2 * ord('A')) % 26
        ciphertext += chr(c + ord('A'))
    return ciphertext

print(vigenere_encrypt("HELLO", "KEY"))
