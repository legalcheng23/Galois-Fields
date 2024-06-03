import galois
import numpy as np

GF = galois.GF(2)

def network_encode(packets, coefficients):
    encoded_packet = GF([0] * len(packets[0]))
    for packet, coefficient in zip(packets, coefficients):
        encoded_packet += GF(coefficient) * GF(packet)
    return encoded_packet

def network_decode(encoded_packets, coefficients):
    coeff_matrix = np.array(coefficients, dtype=int)
    encoded_matrix = np.array([packet.tolist() for packet in encoded_packets], dtype=int)

    decoded_packets = np.linalg.solve(coeff_matrix, encoded_matrix)
    return decoded_packets

if __name__ == "__main__":
    packets = [
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 0, 0]
    ]
    
    print("Original packets:")
    for packet in packets:
        print(packet)
    
    # Coefficients for linear combination
    coefficients = [
        [1, 0, 1],  # For the first encoded packet
        [0, 1, 1],  # For the second encoded packet
        [1, 1, 0]   # For the third encoded packet
    ]
    encoded_packets = [network_encode(packets, coeff) for coeff in coefficients]
    
    print("\nEncoded packets:")
    for packet in encoded_packets:
        print(packet.tolist())
    
    # Decode the packets
    decoded_packets = network_decode(encoded_packets, coefficients)
    
    print("\nDecoded packets:")
    for packet in decoded_packets:
        print(np.round(packet).astype(int).tolist())  # Convert to integers and round to handle numerical errors
