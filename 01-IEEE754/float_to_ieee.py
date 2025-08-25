import argparse

def float_to_ieee(value: float, precision: int) -> str:
    '''
    Convert a floating-point number to its IEEE 754 binary representation.
    '''
    if precision not in (32, 64):
        raise ValueError('Precision must be 32 or 64 bits.')
    if not (value < float('inf') and value > float('-inf')):
        raise ValueError('Input must be a finite real number')

    exponent_length = 8 if precision == 32 else 11
    mantissa_length = 23 if precision == 32 else 52

    if value == 0: # Special case for zero
        return '0' * (1 + exponent_length + mantissa_length)

    sign = '0' if value >= 0 else '1'
    value = abs(value)

    # Value will be in [ 2^m, 2^(m+1) )
    exponent = 0
    while value < 2 ** mantissa_length:
        value *= 2
        exponent -= 1
    while value >= 2 ** (mantissa_length + 1):
        value /= 2
        exponent += 1

    # Get mantissa
    value = int(value) # Note: IEEE 754 doesn't truncate
    exponent += mantissa_length
    mantissa = bin(value)[3:]

    # Calculate exponent and its binary representation
    exponent += 2 ** (exponent_length - 1) - 1
    if exponent <= 0 or exponent >= 2 ** exponent_length - 1:
        raise OverflowError('Exponent out of range')
    character = bin(exponent)[2:]
    character = character.zfill(exponent_length)

    return sign + character + mantissa

if __name__ == '__main__':
    # Build parser
    parser = argparse.ArgumentParser()
    default_value = 27.56640625
    default_precision = 64
    parser.add_argument(
        'value', type=float, nargs='?', default=default_value,
        help='The floating-point value to convert (default: %(default)s)'
    )
    parser.add_argument(
        'precision', type=int, nargs='?', default=default_precision,
        choices=[32, 64], help='The precision (32 or 64 bits, default: %(default)s)'
    )

    # Print float 
    args = parser.parse_args()
    value = args.value
    precision = args.precision
    print(f"IEEE 754 representation of {value} in {precision} bits: \n{float_to_ieee(value, precision)}")
