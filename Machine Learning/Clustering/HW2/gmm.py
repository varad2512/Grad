import numpy as np
from collections import defaultdict
import random
import math
from pprint import pprint
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
import itertools
from scipy import linalg
import matplotlib as mpl
from sklearn import mixture
filename = "clusters.txt"
mode = 'r'
input_data = open(filename, mode)
ip_data = []
for i in input_data.readlines():
    ip_data.append(map(float, i.rstrip('\r\n').split(',')))
np_matrix = np.array(ip_data)

mu  = {}
cv  = {}
pi  = {}
ric = {}
ric[0] = []
ric[1] = []
ric[2] = []
for i in range(150):
    a = np.random.random(3)
    a /= a.sum()
    ric[0].append(a[0])
    ric[1].append(a[1])
    ric[2].append(a[2])

def piCalc():
    global pi
    for i in range(3):
        pi[i] = sum(ric[i])/(sum(ric[0])+sum(ric[1])+sum(ric[2]))

def muCalc():
    global mu
    mu = {}
    mu_val = {}
    for c in range(3):
        mu_val[c] = [0,0]
        for i in range(150):
            mu_val[c] = mu_val[c] + np.array([ric[c][i]*np_matrix[i][0], ric[c][i]*np_matrix[i][1]])
        mu[c] = mu_val[c]/sum(ric[c])

def cvCalc():
    global cv
    cv = {}
    cv_val = {}
    for c in range(3):
        cv_val[c] = np.array([[0,0],[0,0]])
        for i in range(150):
            cv_val[c] = cv_val[c] + ric[c][i]*((np.array([np_matrix[i]-mu[c]]).T)*(np.array([np_matrix[i]-mu[c]])))
        cv[c] = cv_val[c]/sum(ric[c])

def nValue(x,m,c):
    det = np.linalg.det(c)
    x_minus_mu = np.array([x-m])
    inv = np.linalg.inv(c)
    expon = math.exp((((x_minus_mu).dot(inv)).dot((x_minus_mu).T)[0][0])*(-0.5))
    return ((det)**(-0.5))*(expon)/((2*22)/7)

def closeCon():
    total = 0
    for i in range(150):
        total = total + math.log(ric[0][i]+ric[1][i]+ric[2][i])
    return total

def plot_distribution():
    mean1 = list(mu[0])
    cov1  = list(cv[0])
    mean2 = list(mu[1])
    cov2  = list(cv[1])
    mean3 = list(mu[2])
    cov3  = list(cv[2])
    x1, y1 = np.random.multivariate_normal(mean1, cov1, 500).T
    x2, y2 = np.random.multivariate_normal(mean2, cov2, 500).T
    x3, y3 = np.random.multivariate_normal(mean3, cov3, 500).T
    plt.plot(x1, y1, 'x', color = "G", alpha = 0.4)
    plt.plot(x2, y2, 'x', color = "B", alpha = 0.4)
    plt.plot(x3, y3, 'x', color = "K", alpha = 0.4)
    plt.axis('equal')
    plt.scatter(np_matrix[:,0],np_matrix[:,1],color="R")
    plt.scatter(mu[0][0],mu[0][1],color="G")
    plt.scatter(mu[1][0],mu[1][1],color="B")
    plt.scatter(mu[2][0],mu[2][1],color="K")
    plt.show()

def plot_guassians(X,means, covariances, index, title):
        input_cv, input_mu = [], []
        for key, value in cv.iteritems():
            input_cv.append(value)
        for key, value in mu.iteritems():
            input_mu.append(value)
        means = np.array(input_mu)
        covariances = np.array(input_cv)
        splot = plt.subplot(2, 1, 1 + index)
        for i, (mean, c, color) in enumerate(zip(
                means, covariances, color_iter)):
            v, w = linalg.eigh(c)
            v = 2. * np.sqrt(2.) * np.sqrt(v)
            u = w[0] / linalg.norm(w[0])
            angle = np.arctan(u[1] / u[0])
            angle = 180. * angle / np.pi  # convert to degrees
            ell = mpl.patches.Ellipse(mean, v[0], v[1], angle, color=color)
            ell.set_clip_box(splot.bbox)
            ell.set_alpha(0.5)
            splot.add_artist(ell)
        plt.xlim(-10., 10.)
        plt.ylim(-10., 10.)
        plt.xticks(())
        plt.yticks(())
        plt.title(title)
        plt.scatter(np_matrix[:, 0], np_matrix[:, 1], color="R")
        plt.show()

epochs = 0
convergence_current,convergence_previous = 0,0
while(True):
    piCalc()
    muCalc()
    cvCalc()
    for c in range(3):
        lis = []
        for i in range(150):
            lis.append(pi[c]*nValue(np_matrix[i],mu[c],cv[c]))
        ric[c] = lis
    for i in range(150):
        ric_den_sum = 0
        for c in range(3):
            ric_den_sum = ric_den_sum + pi[c]*nValue(np_matrix[i],mu[c],cv[c])
        ric[0][i] = ric[0][i]/ric_den_sum
        ric[1][i] = ric[1][i]/ric_den_sum
        ric[2][i] = ric[2][i]/ric_den_sum
    convergence_previous = convergence_current
    convergence_current = closeCon()
    if epochs != 0:
        if convergence_current >= convergence_previous:
            break
    epochs+=1
    #print epochs,":","  ","Convergence Value:",convergence_current

#collecting results for each gaussian mean, amplitude and covaraince
i=1
for mean,cov,amp in zip(mu.values(),cv.values(),pi.values()):

    print 'Covariance of Gaussian:', i
    print cov
    print 'Mean of Gaussian:',i 
    print mean 
    print 'Amplitude of Gaussian:',i 
    print amp 
    i+=1
'''
#UNCOMMENT TO VISUALIZE DISTRIBUTION AND THE SHAPE AND LOCATION OF GUASSIANS*
plot_guassians(np_matrix, mu, cv, 0,'Gaussian Mixture')
plot_distribution()
'''










