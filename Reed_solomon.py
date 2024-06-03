import galois

# Parameters for Reed-Solomon code
n = 15  # Length of the codeword
k = 11  # Length of the message

# Define the finite field GF(2^4)
GF = galois.GF(2**4)

# Define the generator polynomial for the Reed-Solomon code
generator_poly = galois.Poly.Str("x^4 + x + 1", field=GF)

# Reed-Solomon encoding
def rs_encode(message):
    message_poly = galois.Poly(message, field=GF)
    padded_message = message_poly * galois.Poly.Str("x^4", field=GF)  # Multiply by x^(n-k)
    remainder = padded_message % generator_poly
    codeword = padded_message + remainder
    return codeword.coeffs

# Reed-Solomon decoding
def rs_decode(codeword):
    codeword_poly = galois.Poly(codeword, field=GF)
    syndrome = codeword_poly % generator_poly
    if syndrome == 0:
        return codeword[:k]  # No errors
    corrected_codeword = codeword_poly - syndrome
    return corrected_codeword.coeffs[:k]

if __name__ == "__main__":
    message = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    print(f"Original message: {message}")

    codeword = rs_encode(message)
    print(f"Encoded codeword: {codeword}")

    codeword_with_error = codeword.copy()
    codeword_with_error[2] ^= 1 
    print(f"Codeword with error: {codeword_with_error}")

    decoded_message = rs_decode(codeword_with_error)
    print(f"Decoded message: {decoded_message}")
