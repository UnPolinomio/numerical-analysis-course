import numpy as np

def power_method(A, num_iterations=100, tolerance=1e-6):
    '''
    Computes the dominant eigenvalue and corresponding eigenvector of matrix A.
    '''
    assert A.shape[0] == A.shape[1], 'Matrix must be square'

    n = A.shape[0]
    v = np.random.rand(n) # Random initial vector

    for _ in range(num_iterations):
        v = v / np.linalg.norm(v)
        eigenvalue = v @ A @ v
        v_prod = A @ v

        error = np.linalg.norm(eigenvalue * v - v_prod)
        if error < tolerance:
            print('Converged')
            break

        v = v_prod

    return eigenvalue, v


A = np.array([
    [-4, -14, 0],
    [-5, 10, 0],
    [-1, 0, 2]
])
eigenvalue, eigenvector = power_method(A)
print("Dominant Eigenvalue:", eigenvalue)
print("Corresponding Eigenvector:", eigenvector)
