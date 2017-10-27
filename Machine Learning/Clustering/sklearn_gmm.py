#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:55:21 2017

@author: priyambadajain
"""
import numpy as np
from sklearn import mixture


        

filename = "clusters.txt"
mode = 'r'
input_data = open(filename, mode)
ip_data = []
for i in input_data.readlines():
    ip_data.append(map(float, i.rstrip('\r\n').split(',')))
np_matrix = np.array(ip_data)


gmix = mixture.GMM(n_components=3, covariance_type='tied',init_params='random')
gmix.fit(np_matrix)
print (gmix.means_)

