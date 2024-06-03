import galois

GF = galois.GF(2)

# CRC polynomial
crc_poly = galois.Poly.Str("x^8 + x^2 + x + 1", field=GF)

# CRC encoding function
def crc_encode(data, crc_poly):
    data_poly = galois.Poly(data, field=GF)
    padded_data = data_poly * galois.Poly.Str("x^8", field=GF)  # Multiply by x^n
    remainder = padded_data % crc_poly
    codeword = padded_data + remainder
    return codeword.coeffs

# CRC decoding function
def crc_decode(codeword, crc_poly):
    codeword_poly = galois.Poly(codeword, field=GF)
    syndrome = codeword_poly % crc_poly
    return syndrome == 0 

if __name__ == "__main__":
    data = [1, 0, 1, 1, 0, 0, 1, 0]

    print(f"Original data: {data}")

    codeword = crc_encode(data, crc_poly)
    print(f"Encoded codeword: {codeword}")

    codeword_with_error = codeword.copy()
    codeword_with_error[2] ^= 1 
    print(f"Codeword with error: {codeword_with_error}")

    is_valid = crc_decode(codeword_with_error, crc_poly)
    print(f"Is the received codeword valid? {is_valid}")

    if not is_valid:
        print("Error detected! Original codeword was:", codeword)
