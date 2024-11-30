def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result
p = 61
g = 3
x = 23
C1 = 60
C2 = 13
p_minus_1_minus_x = p - 1 - x
C1_exp = modular_exponentiation(C1, p_minus_1_minus_x, p)
M_mod = (C2 * C1_exp) % p
k = 33
M = M_mod + k * p
print("Hasil dekripsi:")
print(f"M_mod: {M_mod}")
print(f"Plaintext asli (M): {M}")
