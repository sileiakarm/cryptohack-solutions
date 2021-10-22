b = 12 # Base
e = 65537 # Exponent
p, q = 17, 23 # Primes numbers
N = p * q # Modulus

print(pow(b, e, N))
