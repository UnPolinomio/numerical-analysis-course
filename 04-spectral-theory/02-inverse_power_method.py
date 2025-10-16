import numpy as np
import matplotlib.pyplot as plt

def _solve_upper_triangular(A, b):
    '''
    Solve Ax = b where A is an upper triangular matrix.
    '''
    n = A.shape[0]
    x = np.zeros(n)

    for i in range(n - 1, -1, -1): # Solve x[n-1] to x[0]
        x[i] = b[i] - (A[i, i+1:] @ x[i+1:])
        x[i] /= A[i, i]

    return x

def _gaussian_elimination(A, b):
    '''
    Solve Ax = b using Gaussian elimination with partial pivoting.
    '''
    A = A.copy()
    b = b.copy()
    n = A.shape[0]

    for i in range(n - 1): # For each column
        max_row = np.argmax(np.abs(A[i:, i])) + i # Find pivot
        A[[i, max_row]] = A[[max_row, i]]
        b[i], b[max_row] = b[max_row], b[i]

        if A[i, i] == 0:
            raise ValueError('Matrix is not invertible')

        for j in range(i + 1, n): # Elimination
            factor = A[j, i] / A[i, i]
            A[j] -= A[i] * factor
            b[j] -= b[i] * factor

    if A[n - 1, n - 1] == 0:
        raise ValueError('Matrix is not invertible')

    return _solve_upper_triangular(A, b)

def inverse_power_method(A, delta = 0, num_iterations=100, tolerance=1e-6, plot=True):
    '''
    Computes the eigenvalue and corresponding eigenvector of matrix A closest
    to the given delta.
    '''

    assert A.shape[0] == A.shape[1], 'Matrix must be square'

    n = A.shape[0]
    v = np.random.rand(n) # Random initial vector

    eigenvalues = []
    errors = []

    B = A - delta * np.eye(n) # Shifted matrix
    for _ in range(num_iterations):
        v = v / np.linalg.norm(v)
        eigenvalue = v @ A @ v

        error = np.linalg.norm(eigenvalue * v - A @ v)
        
        # Save for plotting
        eigenvalues.append(eigenvalue)
        errors.append(error)

        # Check for convergence
        if error < tolerance:
            print('Converged')
            break

        try:
            v = _gaussian_elimination(B, v)
        except ValueError:
            raise ValueError('Shift led to a singular matrix (A - delta I). Choose a different delta.')

    if plot:
        _, (ax1, ax2) = plt.subplots(1, 2)
        ax1.plot(eigenvalues, marker='o')
        ax1.set_title('Eigenvalue Convergence')
        ax1.set_xlabel('Iteration')
        ax1.set_ylabel('Eigenvalue')

        ax2.plot(errors, marker='o')
        ax2.set_title('Error Convergence')
        ax2.set_xlabel('Iteration')
        ax2.set_ylabel('Error')

        plt.tight_layout()
        plt.show()

    return eigenvalue, v / np.linalg.norm(v)

# Ask the user for a matrix
if __name__ == "__main__":
    n = int(input("Enter the size of the square matrix (n): "))
    print("Enter the matrix row by row, with elements separated by spaces:")
    user_matrix = []
    for i in range(n): # Read n rows
        row = list(map(float, input(f"Row {i+1}: ").strip().split()))
        assert len(row) == n, "Row length must match the size of the matrix"
        user_matrix.append(row)

    delta = float(input("Enter the shift value (delta): "))

    A = np.array(user_matrix)
    eigenvalue, eigenvector = inverse_power_method(A, delta=delta)
    print("Eigenvalue:", eigenvalue)
    print("Eigenvector:", eigenvector)
