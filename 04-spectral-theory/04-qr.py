import numpy as np

def qr_decomposition(A, tolerance = 1e-8):
    '''
    Perform QR decomposition of a mxn matrix A (m >= n) using
    Householder reflections. Returns pair (Q, R).
    '''
    A = A.copy().astype(float)
    m = A.shape[0] # Rows
    n = A.shape[1] # Columns

    assert m >= n, 'Matrix A must be tall and skinny (m >= n)'

    # Resulting orthogonal matrix
    Q = np.eye(m)

    for j in range(n): # Make zero below diagonal in column j
        x = A[j:, j]
        y = np.zeros_like(x)
        y[0] = -np.copysign(np.linalg.norm(x), x[0])
        v = x - y # Get direction vector

        if np.linalg.norm(v) <= tolerance: # Skip if already zero
            continue
        
        # Build Householder reflection
        v /= np.linalg.norm(v)
        v = v[:, np.newaxis]
        P = np.eye(m)
        P[j:, j:] -= 2 * (v @ v.T)

        # Apply reflection to A and accumulate in Q
        A = P @ A
        Q = Q @ P

    return Q, A

# Example usage
np.set_printoptions(suppress=True, precision=8)
A = np.array([
    [0.2113249, -1.9048581],
    [0.7560439, 0.8851428],
    [0.0002211, -2.943175],
    [0.3303271, -1.2348996],
    [0.6653811, 0.1974177]
])
Q, R = qr_decomposition(A)
print('Q=\n', Q)
print('R=\n', R)

print('Orthogonality error:', np.linalg.norm(Q @ Q.T - np.eye(Q.shape[0])))
print('Decomposition error:', np.linalg.norm(Q @ R - A))

Q1 = Q[:, :2]
R1 = R[:2, :]

print('Alternative decomposition error:', np.linalg.norm(Q1 @ R1 - A))
