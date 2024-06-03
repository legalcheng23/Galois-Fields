import random
from sympy import isprime, mod_inverse

def generate_large_prime(bits=1024):
    while True:
        prime_candidate = random.getrandbits(bits)
        if isprime(prime_candidate):
            return prime_candidate

# RSA Key Generation
def generate_rsa_keys(bits=1024):
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi_n)
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# Encryption
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    plaintext_int = int.from_bytes(plaintext.encode('utf-8'), 'big')
    ciphertext_int = pow(plaintext_int, e, n)
    return ciphertext_int

# Decryption
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext_int = pow(ciphertext, d, n)
    plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big')
    return plaintext_bytes.decode('utf-8')

if __name__ == "__main__":
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys(1024)
    
    # Original
    message = "Hello, this is a test message."
    print(f"Original message: {message}")
    
    # Encrypt
    ciphertext = rsa_encrypt(message, public_key)
    print(f"Encrypted message: {ciphertext}")
    
    # Decrypt
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print(f"Decrypted message: {decrypted_message}")

