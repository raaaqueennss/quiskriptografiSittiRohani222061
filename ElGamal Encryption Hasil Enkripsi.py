def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

p = 61
g = 3
x = 23
y = mod_exp(g, x, p)
M = 2061
k = 15

c1 = mod_exp(g, k, p)
yk = mod_exp(y, k, p)
c2 = (M * yk) % p

print(f"Plaintext (M) = {M}")
print(f"Kunci Publik (p = {p}, g = {g}, y = {y})")
print(f"Bilangan Acak (k) = {k}")
print(f"Ciphertext (c1, c2) = ({c1}, {c2})")
