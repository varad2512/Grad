#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:05:58 2017
@author: priyambadajain
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 


filename = "/Users/priyambadajain/Desktop/Machine_Learning/hw2/clusters.txt"
mode = 'r'
input_data = open(filename, mode)
ip_data = []
for i in input_data.readlines():
    ip_data.append(map(float, i.rstrip('\r\n').split(',')))
np_matrix = np.array(ip_data)

y_pred = KMeans(n_clusters=3).fit_predict(np_matrix)
y_centroids = KMeans(n_clusters=3).fit(np_matrix)
print(y_centroids.cluster_centers_)
plt.figure()


plt.scatter(np_matrix[:, 0], np_matrix[:, 1], c=y_pred,alpha =0.8)
plt.title("Python K-means Library results")
plt.show()
plt.savefig('sklearn_kmeans.jpg')

