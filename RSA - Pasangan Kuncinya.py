from math import gcd


def modular_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None
p = 7
q = 17
n = p * q
phi = (p - 1) * (q - 1)
e = 5  
if gcd(e, phi) != 1:
    raise ValueError("e dan φ(n) harus coprime!")
d = modular_inverse(e, phi)
if d is None:
    raise ValueError("Tidak ditemukan invers modular untuk e dan φ(n)!")
print("Pasangan Kunci RSA:")
print(f"Kunci Publik: (e={e}, n={n})")
print(f"Kunci Privat: (d={d}, n={n})")
