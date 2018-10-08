import numpy as np
from matplotlib import pyplot as plt
# Set three centers, the model should predict similar results
center_1 = np.array([1,1])
center_2 = np.array([5,5])
center_3 = np.array([8,1])

# Generate random data and center it to the three centers
data_1 = np.random.randn(200, 2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3

data = np.concatenate((data_1, data_2, data_3), axis = 0)


def kmeans(data, k):
    #assume 2d data
    [m, n] = data.shape
    c_old = np.zeros((k,2))
    c_new = np.zeros((k,2))
    for i in range(2):
        mean = np.mean(data, axis = 1)[i]
        std = np.std(data, axis = 1)[i]
        c_old[:,[i]] = std * np.random.rand(3,1) + mean

    distances = np.zeros((m, k))
    #print (distances.shape)
    clusters = np.zeros(m)
    error = 1e6
    ite = 0
    while error > 1e-6 and ite <=10000:
        for i in range(k):
            distances[:,i] = np.linalg.norm(data - c_old[i,:], axis = 1)
        clusters = np.argmin(distances, axis = 1)
        for i in range(k):
            c_new[i,:] =np.mean(data[clusters == i], axis = 0)
        error = np.linalg.norm(c_new-c_old)
        c_old = c_new

    return clusters


xxx = kmeans(data, 3)  







