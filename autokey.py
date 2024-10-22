def autokey_encrypt(plaintext, key):
    key += plaintext  # append plaintext to key
    ciphertext = ''
    for i in range(len(plaintext)):
        c = (ord(plaintext[i]) + ord(key[i]) - 2 * ord('A')) % 26
        ciphertext += chr(c + ord('A'))
    return ciphertext

print(autokey_encrypt("HELLO", "KEY"))
