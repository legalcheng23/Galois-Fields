# Galois-Fields

### Implementation of Galois Field's Applications

1. **Install Dependencies**:
    - Ensure you have Python 3.x installed.
    - Install NumPy, SymPy, and Matplotlib by running:
    ```sh
    pip install numpy sympy matplotlib
    ```

2. **Clone the Repository**:
    - Clone the repository to your local machine using:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

3. **Run the AES S-box Script**:
    - S-box (Substitution box): In AES encryption, the S-box is a non-linear transformation used for byte substitution, which is critical for the security of the encryption process. Each value in the S-box is the multiplicative inverse of an element in GF(\(2^8\)), followed by an affine transformation.
    - Finite Field GF(\(2^8\)): This is a field with 256 elements. Each element can be represented as an 8-bit binary number.
    ```sh
    python AES_Sbox.py
    ```

4. **Run the RSA Script**:
    - Algorithms such as RSA and Elliptic Curve Cryptography (ECC) rely on the arithmetic of finite fields to secure communications.
    ```sh
    python RSA.py
    ```
5. **Run the Reed_solomon Script**:
    - Error Detection and Correction
    - Reed-Solomon Codes: These codes are used for error detection and correction in digital communication and storage systems, such as CDs, DVDs, QR codes, and deep space communication.
    ```sh
    python Reed_solomon.py
    ```
6. **Run the CRC for DSP Script**:
    - Galois Fields are used in DSP algorithms for error correction and data integrity verification, playing a crucial role in ensuring reliable data transmission and storage.
    ```sh
    python CRCforDSP.py
    ```

7. **Run the Networking Script**:
    - Network coding techniques utilize Galois Fields to improve the efficiency and reliability of data transmission over networks.
    ```sh
    python Networking.py
    ```

### Detailed Explanation

1. **AES S-box**:
    - **Functions**:
        - `gf_mult(a, b, mod=0x11b)`: Performs multiplication in \( GF(2^8) \) using the irreducible polynomial \( x^8 + x^4 + x^3 + x + 1 \).
        - `gf_inv(a)`: Finds the multiplicative inverse of a given element in \( GF(2^8) \).
        - `affine_transform(x)`: Applies the affine transformation to an element in \( GF(2^8) \).
        - `generate_sbox()`: Generates the AES S-box by finding the multiplicative inverse of each byte and applying the affine transformation.

    - **Example Output**:
        - ```plaintext
        AES S-box:
        [[ 99 124 119 123 242 107 111 197  48   1 103  43 254 215 171 118]
        [202 130 201 125 250  89  71 240 173 212 162 175 156 164 114 192]
        [183 253 147  38  54  63 247 204  52 165 229 241 113 216  49  21]
        [  4 199  35 195  24 150   5 154   7  18 128 226 235  39 178 117]
        [  9 131  44  26  27 110  90 160  82  59 214 179  41 227  47 132]
        [ 83 209   0 237  32 252 177  91 106 203 190  57  74  76  88 207]
        [208 239 170 251  67  77  51 133  69 249   2 127  80  60 159 168]
        [ 81 163  64 143 146 157  56 245 188 182 218  33  16 255 243 210]
        [205  12  19 236  95 151  68  23 196 167 126  61 100  93  25 115]
        [ 96 129  79 220  34  42 144 136  70 238 184  20 222  94  11 219]
        [224  50  58  10  73   6  36  92 194 211 172  98 145 149 228 121]
        [231 200  55 109 141 213  78 169 108  86 244 234 101 122 174   8]
        [186 120  37  46  28 166 180 198 232 221 116  31  75 189 139 138]
        [112  62 181 102  72   3 246  14  97  53  87 185 134 193  29 158]
        [225 248 152  17 105 217 142 148 155  30 135 233 206  85  40 223]
        [140 161 137  13 191 230  66 104  65 153  45  15 176  84 187  22]]
        ```
2. **RSA Public Key Cryptography**:
    - **Functions**:
        - `generate_large_prime(bits=1024)`: Generates a large prime number with the specified number of bits.
        - `generate_rsa_keys(bits=1024)`: Generates RSA public and private keys.
        - `rsa_encrypt(plaintext, public_key)`: Encrypts the plaintext message using the public key.
        - `rsa_decrypt(ciphertext, private_key)`: Decrypts the ciphertext message using the private key.

    - **Example Output**:
        - The script generates RSA keys, encrypts a test message, and then decrypts the message to verify the correctness of the implementation.
        ```plaintext
        Original message: Hello, this is a test message.
        Encrypted message: 473821576237504847371738947293497229849709327383738472929389225491820398457201390281740...
        Decrypted message: Hello, this is a test message.
        ```
3. **Reed-Solomon Error Detection and Correction**:
    - **Functions**:
        - `rs_encode(message)`: Encodes the message using Reed-Solomon encoding.
        - `rs_decode(codeword)`: Decodes the codeword and corrects errors using Reed-Solomon decoding.

    - **Example Output**:
        - The script encodes a message, introduces an error, and then decodes the message to demonstrate error detection and correction.
        ```plaintext
        Original message: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        Encoded codeword: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 12, 9, 5]
        Codeword with error: [1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 11, 15, 12, 9, 5]
        Decoded message: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        ```
4. **CRC for DSP**:
    - **Functions**:
        - `crc_encode(data, crc_poly)`: Encodes the data using a CRC polynomial by appending the CRC remainder to the data.
        - `crc_decode(codeword, crc_poly)`: Decodes the codeword and checks for errors by verifying the CRC remainder.      

    - **Example Output**:
        - The script encodes data, introduces an error, and then decodes the data to demonstrate error detection.

        ```plaintext
        Original data: [1, 0, 1, 1, 0, 0, 1, 0]
        Encoded codeword: [1 0 1 1 0 0 1 0 1 0 1 1 0 0]
        Codeword with error: [1 0 0 1 0 0 1 0 1 0 1 1 0 0]
        Is the received codeword valid? False
        Error detected! Original codeword was: [1 0 1 1 0 0 1 0 1 0 1 1 0 0]
        ```

5. **Network Coding**:
    - **Functions**:
        - `network_encode(packets, coefficients)`: Encodes multiple packets into a single packet using linear combinations of the packets with given coefficients.
        - `network_decode(encoded_packets, coefficients)`: Decodes the encoded packets back into the original packets by solving a system of linear equations.      

    - **Example Output**:
        - The script encodes packets, simulates transmission, and decodes the packets to demonstrate the benefits of network coding.

        ```plaintext
        Original packets:
        [1, 0, 1, 1]
        [0, 1, 0, 1]
        [1, 1, 0, 0]

        Encoded packets:
        [1, 1, 1, 1]
        [0, 0, 1, 0]
        [1, 1, 1, 1]

        Decoded packets:
        [1, 0, 1, 1]
        [0, 1, 0, 1]
        [1, 1, 0, 0]

                ```