import random
import math
message = input("Enter a message to encrypt: ")

def generate_random_digits():
    # Choose a random length between 200 and 600 for the primes
    length = random.randint(200, 600)
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return int(random_digits)

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check for divisibility by small primes first
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Miller-Rabin primality test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, n - 1, n)
        if x != 1:
            return False
    return True

random1 = generate_random_digits()
random2 = generate_random_digits()
while (not is_prime(random1)):
    random1 = generate_random_digits()

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        print("attempt")
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)


rand1 = generate_random_digits()
while(not is_prime(rand1)):
    rand1 = generate_random_digits()
    print(rand1)
rand2 = generate_random_digits()
while(not is_prime(rand2)):
    rand2 = generate_random_digits()
    print(rand2)
print("Random1: " + str(rand1))
print("Random2: " + str(rand2))
print("product: " + str(rand1*rand2))

public, private = generate_keypair(rand1, rand2)
print("Public: " + str(public))
print("Private: " + str(private))

encrypted_msg = encrypt(private, message)
print("Your encrypted message is:\n")
print(''.join(map(lambda x: str(x), encrypted_msg)))
print("Your message is:\n")
print(decrypt(public, encrypted_msg))