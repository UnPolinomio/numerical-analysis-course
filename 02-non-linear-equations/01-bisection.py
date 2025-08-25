import math
import argparse

def sign(value):
    '''
    Returns the sign of a value (-1, 0, 1)
    '''
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0

def bisection(f, a, b, tol = 1e-8, N = 100, log = False):
    '''
    Bisection method for finding roots of a function.
    '''
    if sign(f(a)) * sign(f(b)) >= 0:
        raise ValueError('Values at the endpoints must have opposite signs.')

    fa = f(a)

    for iteration in range(N): # Up to N iterations
        x = (a + b) / 2
        fx = f(x)

        if log: # Log the current iteration details
            print(f'[{iteration}] Interval = [{a}, {b}], mid = {x}')

        if fx == 0 or (b - a) / 2 < tol: # Check for convergence
            return x

        if sign(fa) * sign(fx) < 0: # Halve the interval
            b = x
        else:
            a = x
            fa = f(a)

    raise Exception('Max iterations exceeded')

# Define the functions to find roots for
def f1(x):
    return x*x - 3

def f2(x):
    return math.tan(x) - x

def f3(x):
    return x * math.exp(x) - 1

def f4(x):
    return math.cos(x) - x

def f5(x):
    return x**3 - 2*x - 5

if __name__ == "__main__":
    # Build parser
    parser = argparse.ArgumentParser(description='Bisection Method')
    parser.add_argument(
        'function',
        choices=['f1', 'f2', 'f3', 'f4', 'f5'],
        help='The function to use'
    )
    parser.add_argument(
        'interval', nargs=2, type=float,
        help='The interval to search for roots'
    )
    parser.add_argument('--tolerance', type=float, default=1e-8)
    parser.add_argument('--max_iterations', type=int, default=100)
    args = parser.parse_args()

    # Extract function and parameters
    f = globals()[args.function]
    a, b = args.interval
    tol = args.tolerance
    N = args.max_iterations

    # Find root using bisection method
    root = bisection(f, a, b, tol, N)
    print(f'Root found: {root}')
