import numpy as np
import matplotlib.pyplot as plt

def power_method(A, num_iterations=100, tolerance=1e-6, plot=True):
    '''
    Computes the dominant eigenvalue and corresponding eigenvector of matrix A.
    '''
    assert A.shape[0] == A.shape[1], 'Matrix must be square'

    n = A.shape[0]
    v = np.random.rand(n) # Random initial vector

    eigenvalues = []
    errors = []
    for _ in range(num_iterations):
        v = v / np.linalg.norm(v)
        eigenvalue = v @ A @ v
        v_prod = A @ v

        error = np.linalg.norm(eigenvalue * v - v_prod)

        # Save to plot later
        eigenvalues.append(eigenvalue)
        errors.append(error)

        # Check for convergence
        if error < tolerance:
            print('Converged')
            break

        v = v_prod

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

    return eigenvalue, v


# Ask the user for a matrix
if __name__ == "__main__":
    n = int(input("Enter the size of the square matrix (n): "))
    print("Enter the matrix row by row, with elements separated by spaces:")
    user_matrix = []
    for i in range(n): # Read n rows
        row = list(map(float, input(f"Row {i+1}: ").strip().split()))
        assert len(row) == n, "Row length must match the size of the matrix"
        user_matrix.append(row)

    A = np.array(user_matrix)
    eigenvalue, eigenvector = power_method(A)
    print("Dominant Eigenvalue:", eigenvalue)
    print("Corresponding Eigenvector:", eigenvector)
