def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result
def rsa_decrypt(ciphertext, d, n):
    return ''.join(chr(mod_exp(char, d, n)) for char in ciphertext)
e = 5  
d = 77  
n = 119  
ciphertext = [mod_exp(ord(char), e, n) for char in "Sitti"]
plaintext = rsa_decrypt(ciphertext, d, n)
print(f"Ciphertext: {ciphertext}")
print(f"Plaintext (ASCII): {[ord(char) for char in plaintext]}")
print(f"Plaintext (String): {plaintext}")
