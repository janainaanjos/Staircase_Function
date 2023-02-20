import numpy as np
from filtering import *
from plot_figure import *



# Input data
data = np.loadtxt("input/synthetic_data.dat")


x = data[:,0]                         # x coordinates (m)
y = data[:,1]                         # y coordinates (m)
z = data[:,2]                         # z coordinates (m)
tfa = data[:,3]                       # total anomaly field (nT)

inc, dec = -15, 30                    # geomagnetic inclination and declination (degrees)

area = (5000, 25000, 5000, 25000)     # (x1, x2, y1, y2) - mesh boundaries
nx, ny = 100, 100                     # number of points in the x and y axis
shape = (nx, ny)


# Polygon vertices (m)
dike = np.loadtxt("input/dike_vertices.dat")
sill = np.loadtxt("input/sill_vertices.dat")
batholith = np.loadtxt("input/batholith_vertices.dat")

model = [dike, sill, batholith]


# Test regularization parameters
l = np.arange(-6,14.5,0.5)
alpha_test = 10**(l[:])


# Calculate the S-function
norm_sol_dx, norm_sol_dy, norm_sol_dz = s_function(x, y, tfa, shape, alpha_test, order=1)

# Determine the regularization parameters
upper_limit = 0.6
inferior_limit = 0.4
alpha_x = linear_regression(norm_sol_dx, alpha_test, upper_limit, inferior_limit)
alpha_y = linear_regression(norm_sol_dy, alpha_test, upper_limit, inferior_limit)
alpha_z = linear_regression(norm_sol_dz, alpha_test, upper_limit, inferior_limit)

alpha_vector = [alpha_x, alpha_y, alpha_z]
alpha_grid = np.mean(alpha_vector)

# Print the exponents of the regularization parameters
print(np.round(alpha_vector[0], 1))
print(np.round(alpha_vector[1], 1))
print(np.round(alpha_vector[2], 1))
print(np.round(alpha_grid, 1))

# First non-regularized derivatives of the TFA (nT/m)
dx_tfa, dy_tfa, dz_tfa = nonregularized_derivative(x, y, tfa, shape, order=1)

# First regularized derivatives of the TFA (nT/m)
reg_dx_tfa, reg_dy_tfa, reg_dz_tfa = regularized_derivative(x, y, tfa, shape, order=1, alpha=10**(alpha_grid))

# ASA (nT/m) and TILT (rad)
asa, tilt = asa_tdr(dx_tfa, dy_tfa, dz_tfa)

# Regularized ASA (nT/m) and TILT (rad)
reg_asa, reg_tilt = asa_tdr(reg_dx_tfa, reg_dy_tfa, reg_dz_tfa)



'''
Plot input data, unregulated and regularized ASA, and unregulated and regularized TILT - Figure 1
'''
plot_figure1(x, y, tfa, asa, reg_asa, tilt, reg_tilt, model)


'''
Plot regularization parameters to derivatives in the x, y and z directions oof the TFA - Figure 2
'''
plot_figure2(alpha_test, norm_sol_dx, norm_sol_dy, norm_sol_dz, alpha_vector)
