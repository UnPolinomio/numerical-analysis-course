import argparse

def ieee_to_float(bits: str) -> float:
    '''
    Convert a binary string in IEEE 754 format to a floating-point number.
    '''
    # Check if the input is a valid 32 or 64-bit binary string
    if not all(b in '01' for b in bits) or len(bits) not in (32, 64):
        raise ValueError('Input must be a 32 or 64-bit binary string.')

    # Handle not normalized numbers
    character = bits[1:9] if len(bits) == 32 else bits[1:12]
    if character == '0' * len(character) or character == '1' * len(character):
        raise ValueError('Input must be a normalized floating-point number.')

    # Get exponent and mantissa
    if len(bits) == 32: # Single precision
        exponent = int(bits[1:9], 2) - 127

        mantissa = 2**23 + int(bits[9:], 2)
        exponent -= 23 # Adjust exponent for mantissa
    else: # Double precision
        exponent = int(bits[1:12], 2) - 1023

        mantissa = 2**52 + int(bits[12:], 2)
        exponent -= 52

    if bits[0] == '1': # Sign
        mantissa = -mantissa

    return mantissa * (2 ** exponent)


if __name__ == '__main__':
    # Build argument parser
    default_bits = '0100000000111011100100010000000000000000000000000000000000000000'
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'bits',
        nargs='?',
        help=f'Binary string (32 or 64 bits).',
        default=default_bits
    )
    args = parser.parse_args()

    # Print IEEE 754 representation
    bits = args.bits
    print(f"IEEE 754 representation of {bits}: \n{ieee_to_float(bits)}")
