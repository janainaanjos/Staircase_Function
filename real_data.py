import numpy as np
from filtering import *
from plot_figure import *



# Input data
data = np.loadtxt("input/data.xyz")

x = data[:,0]                         # x coordinates (m)
y = data[:,1]                         # y coordinates (m)
tfa = data[:,2]                       # total anomaly field (nT)

inc, dec = -20.84, -19.21             # geomagnetic inclination and declination (degrees)

dx = 125; dy = 125
xmin = np.min(x);xmax = np.max(x)
ymin = np.min(y);ymax = np.max(y)
nx = int((xmax-xmin)/dx)+1; ny = int((ymax-ymin)/dy)+1

area = [xmin, xmax, ymin, ymax]       # (x1, x2, y1, y2) - mesh boundaries
shape = (nx, ny)
z = -100 * np.ones((nx,ny))           # z coordinates (m) - flight height


# Test regularization parameters
l = np.arange(-6,14.5,0.5)
alpha_test = 10**(l[:])


# Regularization parameters for the first derivatives of the TFA
norm_sol_dx, norm_sol_dy, norm_sol_dz = estimate_alpha(x, y, tfa, shape, alpha_test, order=1)

# Determine the regularization parameter
upper_limit = 0.7
inferior_limit = 0.5
alpha_x = linear_regression(norm_sol_dx, alpha_test, upper_limit, inferior_limit)
alpha_y = linear_regression(norm_sol_dy, alpha_test, upper_limit, inferior_limit)
alpha_z = linear_regression(norm_sol_dz, alpha_test, upper_limit, inferior_limit)

alpha_vector = [alpha_x, alpha_y, alpha_z]
alpha_grid = (max(alpha_vector) + min(alpha_vector))/2

# Print the exponents of the regularization parameters
print(np.round(alpha_vector[0], 1))
print(np.round(alpha_vector[1], 1))
print(np.round(alpha_vector[2], 1))
print(np.round(alpha_grid, 1))

# First derivatives of the TFA (nT/m)
dx_tfa, dy_tfa, dz_tfa = derivative(x, y, tfa, shape, order=1)

# First regularized derivatives of the TFA (nT/m)
reg_dx_tfa, reg_dy_tfa, reg_dz_tfa = regularized_derivative(x, y, tfa, shape, order=1, alpha=10**(alpha_grid))

# ASA (nT/m) and TILT (rad)
asa, tilt = inclination_amplitude_analytical_signal(dx_tfa, dy_tfa, dz_tfa)

# Regularized ASA (nT/m) and TILT (rad)
reg_asa, reg_tilt = inclination_amplitude_analytical_signal(reg_dx_tfa, reg_dy_tfa, reg_dz_tfa)



'''
Plot regularization parameters to derivatives in the x, y and z directions oof the TFA - Figure 1
'''
plot_figure1(x, y, tfa, asa, reg_asa, tilt, reg_tilt)


'''
Plot regularization parameters to derivatives in the x, y and z directions oof the TFA - Figure 2
'''
plot_figure2(alpha_test, norm_sol_dx, norm_sol_dy, norm_sol_dz, alpha_vector)


'''
Export the results: ASA, REG ASA, TILT, REG TILT
'''

np.savetxt('results/asa.xyz', asa, delimiter="\t")
np.savetxt('results/reg_asa.xyz', reg_asa, delimiter="\t")
np.savetxt('results/tilt.xyz', tilt, delimiter="\t")
np.savetxt('results/reg_tilt.xyz', reg_tilt, delimiter="\t")

