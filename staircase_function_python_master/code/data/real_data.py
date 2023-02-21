"""
Real data test 

Python script to generate the real results. The script loads the total-field anomaly of a real data from the file "real_data.xyz" and computes the 
non-regularized and regularized directional derivatives, S-function, S-function values linear model, analytical signal amplitude, and tilt derivative
using the functions in "filtering.py". The figures are generated using the function "plot_figure.py".

This code is released from the paper: Python programs to apply regularized derivatives in the magnetic tilt derivative and gradient intensity data 
processing: a graphical procedure to choose the regularization parameter.

The program is under the conditions terms in the file README.txt.

authors:Janaína A. Melo (IAG-USP), Carlos A. Mendonça (IAG-USP) and Yara R. Marangoni (IAG-USP) (2023)
email: janaina.melo@usp.br (J.A. Melo); carlos.mendonca@iag.usp.br (C.A. Mendonça); yaramaran@usp.br. (Y.R. Marangoni)
"""

"""
Input:

- input/real_data.dat: 2d-array with "n" rows by 3 columns, where "n" rows correspond to the size of the data.
            x-coordinate, y-coordinate, total-field anomaly.

Parameters:

- Variation range of the trial regularization parameters: 
            alpha_test - 1D-array 

- Linear variation interval limits of the S-function:
            inferior_limit - float
            upper_limit - float
"""

import numpy as np
from filtering import *
from plot_figure import *



# Input data
data = np.loadtxt("input/real_data.xyz")

x = data[:,0]                         # x coordinates (m)
y = data[:,1]                         # y coordinates (m)
tfa = data[:,2]                       # total-field anomaly (nT)

inc, dec = -20.84, -19.21             # geomagnetic inclination and declination (degrees)

dx = 125; dy = 125
xmin = np.min(x);xmax = np.max(x)
ymin = np.min(y);ymax = np.max(y)
nx = int((xmax-xmin)/dx)+1; ny = int((ymax-ymin)/dy)+1

area = [xmin, xmax, ymin, ymax]       # (x1, x2, y1, y2) - mesh boundaries
shape = (nx, ny)                      # number of points in the x and y axis
z = -100 * np.ones((nx,ny))           # z coordinates (m) - flight height


# The user establishes the interval of the trial regularization parameters
l = np.arange(-6,14.5,0.5)
alpha_test = 10**(l[:])

# Calculates the Euclidean norm of the directional derivatives to different regularization parameters 
norm_sol_dx, norm_sol_dy, norm_sol_dz = s_function(x, y, tfa, shape, alpha_test, order=1)

'''The user establishes the interval limits in which the S-function presents a linear variation to determine the regularization parameter 
associated with the Euclidean norm equal to 0.5.'''
upper_limit = 0.7
inferior_limit = 0.45

# Determines the regularization parameters of the directional derivatives
alpha_x = linear_regression(norm_sol_dx, alpha_test, upper_limit, inferior_limit)
alpha_y = linear_regression(norm_sol_dy, alpha_test, upper_limit, inferior_limit)
alpha_z = linear_regression(norm_sol_dz, alpha_test, upper_limit, inferior_limit)

alpha_vector = [alpha_x, alpha_y, alpha_z]

# Grid regularization parameter
alpha_grid = np.mean(alpha_vector)    

# Prints the exponents of the regularization parameters
print(np.round(alpha_vector[0], 1))
print(np.round(alpha_vector[1], 1))
print(np.round(alpha_vector[2], 1))
print(np.round(alpha_grid, 1))

# First non-regularized directional derivatives of the total-field anomaly (nT/m)
dx_tfa, dy_tfa, dz_tfa = nonregularized_derivative(x, y, tfa, shape, order=1)

# First regularized directional derivatives of the total-field anomaly (nT/m)
reg_dx_tfa, reg_dy_tfa, reg_dz_tfa = regularized_derivative(x, y, tfa, shape, order=1, alpha=10**(alpha_grid))

# Non-regularized ASA (nT/m) and TDR (rad)
asa, tdr = asa_tdr(dx_tfa, dy_tfa, dz_tfa)

# Regularized ASA (nT/m) and TDR (rad)
reg_asa, reg_tdr = asa_tdr(reg_dx_tfa, reg_dy_tfa, reg_dz_tfa)



'''
Plot the total-field anomaly, non-regularized and regularized ASA, and non-regularized and regularized TDR - Figure 3
'''
plot_figure3(x, y, tfa, asa, reg_asa, tdr, reg_tdr)


'''
Plot the S-function - Figure 4
'''
plot_figure4(alpha_test, norm_sol_dx, norm_sol_dy, norm_sol_dz, alpha_vector)


'''
Save the results: ASA, REG ASA, TDR, REG TDR
'''

np.savetxt('results/asa.xyz', asa, delimiter="\t")
np.savetxt('results/reg_asa.xyz', reg_asa, delimiter="\t")
np.savetxt('results/tdr.xyz', tdr, delimiter="\t")
np.savetxt('results/reg_tdr.xyz', reg_tdr, delimiter="\t")

