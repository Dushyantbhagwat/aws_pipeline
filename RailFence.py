def rail_fence_encrypt(plaintext, rails):
    rail = [''] * rails
    row = 0
    down = True

    for char in plaintext:
        rail[row] += char
        if down:
            row += 1
        else:
            row -= 1
        if row == 0 or row == rails - 1:
            down = not down

    return ''.join(rail)

print(rail_fence_encrypt("HELLO", 2))
