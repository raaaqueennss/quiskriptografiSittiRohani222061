def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result
def rsa_encrypt(plaintext, e, n):
    return [mod_exp(ord(char), e, n) for char in plaintext]
e = 5  
n = 119  
plaintext = "Sitti"
ciphertext = rsa_encrypt(plaintext, e, n)
print(f"Plaintext (ASCII): {[ord(char) for char in plaintext]}")
print(f"Ciphertext: {ciphertext}")
