#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:23:13 2017

@author: priyambadajain
"""

import numpy as np
from collections import defaultdict
import math

class GMM:
    
    file = "/Users/priyambadajain/Desktop/Machine_Learning/hw2/clusters.txt"
    data_file = open(file,'r')
    data_points =[]
    array = np.array([])
    soft_membership = defaultdict(dict) #3*150 matrix
    mu_cluster = {}   #3 * 2 matrix
    clusters = 3
    co_variance_matrix={}
    pi_c ={}
    
    def _init_(self):
        pass
        
    
    def preprocessing(self):
        for line in self.data_file:
            self.data_points.append([float(x) for x in line.split(",")])
        self.array = np.array(self.data_points)
        self.array = self.array.transpose()  #2*150 matrix
        self.initialization()
        #print(self.soft_membership[0])
        self.mean_calculation()
        
        self.co_variance_matrix_calculation()
        self.amplitude_calculation()
        self.soft_membership_calculation()
        print(self.soft_membership[0])
        
    
    def initialization(self):
        for point in range(150):
            rand_prob = np.random.rand(3)
            rand_prob /= sum(rand_prob)
            self.soft_membership[0][point]=rand_prob[0]
            self.soft_membership[1][point]=rand_prob[1]
            self.soft_membership[2][point]=rand_prob[2]
    
            
    def mean_calculation(self):
        for cluster in range(self.clusters):
            weighted_avg_x = sum(self.soft_membership[cluster][point] * self.array[0][point] for point in range(150))
            weighted_avg_y = sum(self.soft_membership[cluster][point] * self.array[1][point] for point in range(150))
            weighted_avg = np.array([(weighted_avg_x,weighted_avg_y)])
            norm_term = sum(self.soft_membership[cluster])
            self.mu_cluster[cluster] = weighted_avg/norm_term

    
    def co_variance_matrix_calculation(self):
        for cluster in range(self.clusters):
            x = np.array([self.soft_membership[cluster][point]*(self.array[0][point] - self.mu_cluster[cluster][0][0]) for point in range(150)])
            y = np.array([self.soft_membership[cluster][point]*(self.array[1][point] - self.mu_cluster[cluster][0][1]) for point in range(150)])
            N = np.matrix(np.array([x,y]))
            x = np.array([self.array[0][point] - self.mu_cluster[cluster][0][0] for point in range(150)])
            y = np.array([self.array[1][point] - self.mu_cluster[cluster][0][1] for point in range(150)])
            M = np.matrix(np.array([x,y])).T
            num = N * M
            norm_term = sum(self.soft_membership[cluster])
            self.co_variance_matrix[cluster] = num/norm_term
    
    def amplitude_calculation(self):
        for cluster in range(self.clusters):
            self.pi_c[cluster]= sum(self.soft_membership[cluster][point] for point in range(150))/150
        
            
    
    def guassian_calculation(self,cluster,point):
        
        det = np.linalg.det(self.co_variance_matrix[cluster])
        co_var_inv = np.linalg.inv(self.co_variance_matrix[cluster])
        
        x_minus_mu_x = np.array([self.array[0][point]- self.mu_cluster[cluster][0][0]])
        x_minus_mu_y = np.array([self.array[1][point]- self.mu_cluster[cluster][0][1]])
        x_minus_mu =  (np.array([x_minus_mu_x,x_minus_mu_y])).T
        
        term = math.exp(((x_minus_mu*(co_var_inv))*(x_minus_mu).T))
        term **=(-0.5)
        
        return (det**(-0.5)*term)/(2*math.pi)
    
    def soft_membership_calculation(self):
        #den = sum(self.pi_c[cluster]*self.guassian_calculation(cluster,point) for cluster in range(self.clusters) for point in range(150))
        for cluster in range(self.clusters):
            for point in range(150):
                self.soft_membership[cluster][point] = self.pi_c[cluster]*self.guassian_calculation(cluster,point)
                #self.soft_membership[cluster][point]
        
        
            
        
            
            
            
            
        
                
        
    
       
        