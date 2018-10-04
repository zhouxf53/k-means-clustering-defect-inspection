#This file reads IR data in txt format

import numpy as np
import cv2
from numpy.polynomial import polynomial as P
from sklearn.cluster import KMeans as KMeans
import matplotlib.pyplot as plt
import glob
import os


# change the file directory to what you want
filepath = 'C:\Research\Root data\ir IMAGES\T2'
#
def IR_data_read(filepath, w1=160, w2=120):
    #input: filepath, the complete path of the .txt files for analysis
    #w1, the pixel resolution at the first dimension of the image
    #w2, the pixel resolution at the second dimension of the image
    os.chdir(filepath) #change working directory
    folder_name = os.path.basename(filepath)
    txt_filenum = len(glob.glob1(filepath,"*.txt"))
    #not including subsidiary directory
    T_data = np.zeros((w1, w2, txt_filenum))
    for i in range(1, txt_filenum + 1):
        file_name = folder_name + '_' + '{0:03}'.format(i) + '.txt'
        T_data[:,:,i-1] = np.loadtxt(open(file_name, "rb"), delimiter="	")
    return T_data

def fit_image(img_matrix, poly_d = 9):
    #fit polynominal equation of every image along the z dimension of the matrix
    [w1, w2, z] = img_matrix.shape
    fit_image_matrix = np.zeros(img_matrix.shape)
    x_data =  np.linspace(1, w1, w1)
    for i in range(z):
        c, _ = P.polyfit(x_data,T_data[:,:,i],poly_d,full=True)
        fit_image_matrix[:,:, i] = np.transpose(P.polyval(x_data, c, True))
    return fit_image_matrix


def edge_detection(img_matrix_r, ksize = 5):
    #perform sobel edge detection on all images
    #perform superimpose
    [w1, w2, z] = img_matrix_r.shape
    img_edge = np.zeros([w1, w2])
    for i in range(z):
        sobelx64f_x = cv2.Sobel(T_residual[:,:,i],cv2.CV_64F,1,0,ksize)
        sobelx64f_y = cv2.Sobel(T_residual[:,:,i],cv2.CV_64F,0,1,ksize)
        img_edge = img_edge + sobelx64f_x + sobelx64f_y
    
    return img_edge
    
T_data = IR_data_read(filepath, w1=160, w2=120)
fit_T_data = fit_image(T_data, poly_d = 9)
T_residual = np.subtract(T_data, fit_T_data)
T_residual_edge = edge_detection(T_residual, 5)
data_set = np.reshape(T_residual_edge,
                      [T_residual_edge.shape[0] * T_residual_edge.shape[1],
                      1])
kmeans = KMeans(n_clusters=2, random_state=0).fit(data_set)
cluster_res = kmeans.predict(data_set)
cluster_res = np.reshape(cluster_res, T_residual_edge.shape)
plt.imshow(cluster_res)
plt.show()




