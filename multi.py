def multiplicative_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            num = ord(char.lower()) - ord('a')  # Convert to a number (0-25)
            encrypted_num = (num * key) % 26  # Multiply by key and mod 26
            encrypted_char = chr(encrypted_num + ord('a'))  # Convert back to a character
            result += encrypted_char
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

# Static example
plaintext = "wor"
key = 5  # Fixed key for encryption

encrypted_text = multiplicative_encrypt(plaintext, key)
print("Plain Text:", plaintext)
print("Encrypted Text:", encrypted_text)

