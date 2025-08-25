import math
import argparse

def fixed_point(f, x0, tol=1e-8, N=1000):
    '''
    Fixed-point iteration method for finding fixed points.
    '''
    for iter in range(N):
        p = f(x0)
        print(f'[{iter}] p = {p}') # Log current p
        if abs(p - x0) < tol: # Check for convergence
            return p
        x0 = p # Update x0 for next iteration

    raise Exception('Max iterations exceeded')

# Define the functions to find fixed points
def f1(x):
    return math.exp(-x)

def f2(x): # Works on [1, 2]
    return (2 / x + x) / 2

def f3(x): # Works on [0, 1]
    return math.cos(x)

def f4(x): # Works on [0, a] with a >= 1
    return math.exp(-x*x)


if __name__ == "__main__":
    # Build parser
    parser = argparse.ArgumentParser(description='Fixed-point iteration method')
    parser.add_argument(
        'function',
        choices=['f1', 'f2', 'f3', 'f4'],
        help='The function to use'
    )
    parser.add_argument('x0', type=float, help='Initial guess')
    parser.add_argument('--tolerance', type=float, default=1e-8)
    parser.add_argument('--max_iterations', type=int, default=1000)
    args = parser.parse_args()

    # Extract parameters and compute fixed point
    func = globals()[args.function]
    p = fixed_point(func, args.x0, args.tolerance, args.max_iterations)
    print(f'Fixed point found: {p}')
