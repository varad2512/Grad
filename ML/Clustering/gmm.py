import numpy as np
from collections import defaultdict
import random
import math
from pprint import pprint
filename = "clusters.txt"
mode = 'r'
input_data = open(filename, mode)
ip_data = []
for i in input_data.readlines():
    ip_data.append(map(float, i.rstrip('\r\n').split(',')))
np_matrix = np.array(ip_data)
mu = {}
cv = {}
pi = {}

# random fractions 150 X 3
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


# amplitude calculation according to YT video
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
            cv_val[c] = cv_val[c] + ric[c][i]*(np.array([np_matrix[i]-mu[c]])*(np.array([np_matrix[i]-mu[c]]).T))
        cv[c] = cv_val[c]/sum(ric[c])


# N(x(i), mu, cv)
def nValue(x,m,c):
    det = np.linalg.det(c)
    x_minus_mu = np.array([x-m])
    inv = np.linalg.inv(c)
    expon = math.exp((((x_minus_mu).dot(inv)).dot((x_minus_mu).T)[0][0])*(-0.5))
    return ((det)**(-1))*(expon)/((2*22)/7)


# closure condition according to YT video
def closeCon():
    total = 0
    for i in range(150):
        total = total + math.log(ric[0][i]+ric[1][i]+ric[2][i])
    return total
epochs = 0
convergence_current,convergence_previous = 0,0
# ric calculation
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

    print epochs,":","  ","Convergence Value:",convergence_current

pprint(ric)







