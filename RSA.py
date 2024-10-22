def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def rsa_keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 2
    while e < phi and gcd(e, phi) != 1:
        e += 1
    
    d = pow(e, -1, phi)  # mod inverse of e
    return (e, n), (d, n)  # public and private keys

def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Example Usage:
p = 61  # example prime
q = 53  # example prime
public_key, private_key = rsa_keygen(p, q)

plaintext = "HELLO"
ciphertext = rsa_encrypt(plaintext, public_key)
print("Encrypted:", ciphertext)

decrypted_text = rsa_decrypt(ciphertext, private_key)
print("Decrypted:", decrypted_text)
