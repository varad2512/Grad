#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import numpy as np
import sys

input_file = open(sys.argv[1],"r")#open("pca-data.txt","r")
data_list=[]
for point in input_file:
    data_list.append(map(float,point.split("\t")))
N = len(data_list)             #no_of_points

data_points = np.array(data_list).T     #transpose_of_data_points


cov = (data_points.dot(data_points.T))/N

# finding eigenvectors and eigenvalues for the from the covariance matrix
eig_val, eig_vec = np.linalg.eig(cov)

e_v = list(eig_val)
directions = ['X', 'Y', 'Z']
print "First Principal Component Direction ", directions[np.where(eig_val==max(e_v))[0][0]]
e_v.remove(max(e_v))
print "Second Principal Component Direction ", directions[np.where(eig_val==max(e_v))[0][0]]

#now sorting and finding the maximum eigen value that impact the dimensions majorlys 
eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range(len(eig_val))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# choosing 2-dimensional eigen vectors
weighted_matrix = np.hstack((eig_pairs[0][1].reshape(3,1), eig_pairs[1][1].reshape(3,1)))

#dot product with the weighted_matix 
reduced_result = (weighted_matrix.T.dot(data_points)).T


op = open("PCA_output.txt", "w")
for i in range(len(reduced_result)):
	op.write("%f, %f\n" %(reduced_result[i][0], reduced_result[i][1]))

op.close()
