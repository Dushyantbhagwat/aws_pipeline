def keyed_transposition_encrypt(plaintext, key):
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    grid = [''] * num_cols

    for i, char in enumerate(plaintext):
        grid[int(key[i % num_cols]) - 1] += char

    return ''.join(grid)

print(keyed_transposition_encrypt("HELLO", "45213"))
