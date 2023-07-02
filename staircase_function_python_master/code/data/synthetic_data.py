"""
Synthetic data test 

Python script to generate the synthetic results. The script loads the total-field anomaly of a synthetic model from the file "synthetic_data.dat"
and computes the non-regularized and regularized directional derivatives, S-function, regularization parameters, analytical signal 
amplitude, and tilt derivative using the functions in "filtering.py". The figures are generated using the function "plot_figure.py".

This code is released from the paper: Python programs to apply regularized derivatives in the magnetic tilt derivative and gradient intensity data 
processing: a graphical procedure to choose the regularization parameter.

The program is under the conditions terms in the file README.txt.

authors:Janaína A. Melo (IAG-USP), Carlos A. Mendonça (IAG-USP) and Yara R. Marangoni (IAG-USP) (2023)
email: janaina.melo@usp.br (J.A. Melo); carlos.mendonca@iag.usp.br (C.A. Mendonça); yaramaran@usp.br. (Y.R. Marangoni)
"""

"""
Input:

- input/synthetic_data.dat: 2d-array with "n" rows by 4 columns, where "n" rows correspond to the size of the data.
            x-coordinate, y-coordinate, z-coordinate, total-field anomaly.

- input/batholith_vertices: 2d-array with "n" rows by 2 columns.
		    x and y coordinates of the batholith vertices to plot on synthetic data figures.
  
- input/dike_vertices: 2d-array with "n" rows by 2 columns.
		    x and y coordinates of the dike vertices to plot on synthetic data figures.

- input/sill_vertices: 2d-array with "n" rows by 2 columns.
		    x and y coordinates of the sill vertices to plot on synthetic data figures.

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
data = np.loadtxt("input/synthetic_data.dat")

x = data[:,0]                         # x coordinates (m)
y = data[:,1]                         # y coordinates (m)
z = data[:,2]                         # z coordinates (m)
tfa = data[:,3]                       # total-field anomaly (nT)

inc, dec = -15, 30                    # geomagnetic inclination and declination (degrees)

area = (5000, 25000, 5000, 25000)     # (x1, x2, y1, y2) - mesh boundaries
nx, ny = 100, 100                     # number of points in the x and y axis
shape = (nx, ny)


# Polygon vertices (m)
dike = np.loadtxt("input/dike_vertices.dat")
sill = np.loadtxt("input/sill_vertices.dat")
batholith = np.loadtxt("input/batholith_vertices.dat")

model = [dike, sill, batholith]


# The user establishes the interval of the trial regularization parameters
l = np.arange(-6,14.5,0.5)
alpha_test = 10**(l[:])

# Calculates the Euclidean norm of the first directional derivatives to different regularization parameters
norm_sol_dx, norm_sol_dy, norm_sol_dz = s_function(x, y, tfa, shape, alpha_test)

'''The user establishes the interval limits in which the S-function presents a linear variation to determine the regularization parameter 
associated with the Euclidean norm value equal to 0.5, for example.'''
value_norm = 0.5
upper_limit = 0.7
inferior_limit = 0.45

# Determines the regularization parameters of the directional derivatives
alpha_x = regularization_parameter(norm_sol_dx, alpha_test, upper_limit, inferior_limit, value_norm)
alpha_y = regularization_parameter(norm_sol_dy, alpha_test, upper_limit, inferior_limit, value_norm)
alpha_z = regularization_parameter(norm_sol_dz, alpha_test, upper_limit, inferior_limit, value_norm)

alpha_vector = [alpha_x, alpha_y, alpha_z]

# Grid regularization parameter
alpha_grid = np.mean(alpha_vector)     

# Prints the exponents of the regularization parameters
print(np.round(alpha_vector[0], 1))
print(np.round(alpha_vector[1], 1))
print(np.round(alpha_vector[2], 1))
print(np.round(alpha_grid, 1))

# Non-regularized directional first-order derivatives of the total-field anomaly (nT/m)
dx_tfa, dy_tfa, dz_tfa = nonregularized_derivative(x, y, tfa, shape, order=1)

# Regularized directional first-order derivatives of the total-field anomaly (nT/m)
reg_dx_tfa, reg_dy_tfa, reg_dz_tfa = regularized_derivative(x, y, tfa, shape, alpha=10**(alpha_grid))

# Non-regularized ASA (nT/m) and TDR (rad)
asa, tdr = asa_tdr(dx_tfa, dy_tfa, dz_tfa)

# Regularized ASA (nT/m) and TDR (rad)
reg_asa, reg_tdr = asa_tdr(reg_dx_tfa, reg_dy_tfa, reg_dz_tfa)



'''
Plot the total-field anomaly, non-regularized and regularized ASA, and non-regularized and regularized TDR - Figure 1
'''
plot_figure1(x, y, tfa, asa, reg_asa, tdr, reg_tdr, model)


'''
Plot the S-function - Figure 2
'''
plot_figure2(alpha_test, norm_sol_dx, norm_sol_dy, norm_sol_dz, alpha_vector)
