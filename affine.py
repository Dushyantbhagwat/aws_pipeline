def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    # Find modular inverse of a under modulo m using Extended Euclidean Algorithm
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None  # Inverse doesn't exist if gcd(a, m) != 1

def affine_encrypt(plaintext, a, b):
    # Encrypts the text using Affine Cipher formula: (a * x + b) % 26
    result = ""
    for char in plaintext:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')  # Convert char to number 0-25
            encrypted_char = chr(((a * x + b) % 26) + ord('a'))  # Apply encryption formula
            result += encrypted_char
        else:
            result += char  # Non-alphabetic characters are not changed
    return result

def affine_decrypt(ciphertext, a, b):
    # Decrypts the text using the formula: a_inverse * (x - b) % 26
    result = ""
    a_inv = mod_inverse(a, 26)  # Find modular inverse of a
    if a_inv is None:
        return "Inverse of a doesn't exist, choose another a."
    
    for char in ciphertext:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')  # Convert char to number 0-25
            decrypted_char = chr(((a_inv * (x - b)) % 26) + ord('a'))  # Apply decryption formula
            result += decrypted_char
        else:
            result += char  # Non-alphabetic characters are not changed
    return result

# Example usage
plaintext = "hello"
a = 5  # Key 'a' must be coprime with 26
b = 8  # Key 'b'

if gcd(a, 26) == 1:  # 'a' must be coprime with 26
    encrypted_text = affine_encrypt(plaintext, a, b)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = affine_decrypt(encrypted_text, a, b)
    print("Decrypted Text:", decrypted_text)
else:
    print("'a' is not coprime with 26, choose another value for 'a'.")

