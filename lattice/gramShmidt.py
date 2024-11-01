
v1=[4,1,3,-1];
v2=[2,1,-3,4];
v3=[1,0,-2,7];
v4=[6,2,9,-5];
v=[v1,v2,v3,v4]
import numpy as np

def gram_schmidt(vectors):
    """ Perform the Gram-Schmidt process on a set of vectors.
    
    Args:
        vectors (numpy.ndarray): A 2D array where each row represents a vector.
        
    Returns:
        numpy.ndarray: A 2D array of orthogonal vectors.
    """
    vectors=np.array(vectors,dtype=float)
    # Number of vectors
    n = vectors.shape[0]
    # Initialize an array for orthogonal vectors
    u = np.zeros_like(vectors,dtype=float)

    # Step 1: First vector
    u[0] = vectors[0]

    # Step 2: Loop through the remaining vectors
    for i in range(1, n):
        # Start with the current vector
        u[i] = vectors[i]
        # Subtract the projections onto the previously computed u vectors
        for j in range(i):
            mu_ij = np.dot(vectors[i], u[j]) / np.dot(u[j], u[j])
            u[i] -= mu_ij * u[j]

    return u
print(gram_schmidt(v))