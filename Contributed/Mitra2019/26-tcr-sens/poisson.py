from pybnf import data
from scipy.stats import poisson
import numpy as np
import sys

def postprocess(simdata):
    exp_values = [0.000,0.291,0.475,0.798,0.929,1.318,1.543,2.136,2.926]
    
    # Use the poisson distribution to get the average bound ZAP at each of the experimental <MHC>s
    new_array = np.zeros((len(exp_values),2))
    for i,n in enumerate(exp_values):
        new_array[i,0] = n
        if n == 0:
            pdf = [0.]*6
        else:
            pdf = [poisson.pmf(j,n) for j in range(1,7)]
        print(i,n)
        
        new_array[i,1] = sum([pi*ni for pi,ni in zip(pdf, simdata['Bound_ZAP'])])
    
    # Normalize the data such that the max is 2.765 and the value at 0 is 0.394
    if max(new_array[:,1]) > 0:
        new_array[:,1] = (new_array[:,1] / max(10., max(new_array[:,1]))) * 2.371 + 0.394
    
    # Return as a new Data object
    new_data = data.Data(arr=new_array)
    new_data.cols = {'Ave_MHC':0, 'Ca':1}
    new_data.headers = {0:'Ave_MHC', 1:'Ca'}
    return new_data
