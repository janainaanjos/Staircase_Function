import numpy as np
from sklearn.linear_model import LinearRegression


def _nextpow2(i):

    # np.ceil: returns the next float element after the input element
    buf = np.ceil(np.log(i) / np.log(2))

    return int(2 ** buf)       # power of 2 to optimize the application of the Fourier transform



def _pad_data(data, shape):

    nx, ny = shape
    n = _nextpow2(np.max(shape))

    padx = (n - nx) // 2
    pady = (n - ny) // 2

    # np.pad: pads the edges of a matrix
    padded = np.pad(data.reshape(shape), ((padx, padx), (pady, pady)), mode='edge')

    return padded, padx, pady



def _fftfreqs(x, y, shape, padshape):

    nx, ny = shape

    # discretization range
    dx = (x.max() - x.min()) / (nx - 1)
    dy = (y.max() - y.min()) / (ny - 1)

    # wave numbers in the x and y directions
    fx = 2 * np.pi * np.fft.fftfreq(padshape[0], dx)
    fy = 2 * np.pi * np.fft.fftfreq(padshape[1], dy)

    return np.meshgrid(fy, fx)[::-1]



def nonregularized_derivative(x, y, data, shape, order):

    """
    Compute the non-regularized derivatives of a potential field in Fourier domain in the x, y and z directions.

    Parameters:

    * x, y: 1D-array
        grid of coordinates in x- and y- directions
    * data: 1D-array
        the input data set
    * shape: tuple = (nx, ny)
        the shape of the grid
    * order: integer
        derivative order

    Returns:

    * dx, dy, dz: 1D-array
        derivatives in x-, y- and z-directions
    """

    nx, ny = shape

    padded, padx, pady = _pad_data(data, shape)    # fills the matrix with the values of the edges
    kx, ky = _fftfreqs(x, y, shape, padded.shape)  # wave numbers in the x and y directions

    # calculate the derivatives in the Fourier domain
    derivx_ft = np.fft.fft2(padded) * ((kx * 1j) ** order)
    derivy_ft = np.fft.fft2(padded) * ((ky * 1j) ** order)
    derivz_ft = np.fft.fft2(padded) * (np.sqrt(kx ** 2 + ky ** 2) ** order)

    # np.real: returns the real part of the complex argument
    # np.fft.ifft2: calculates the two-dimensional inverse discrete Fourier transform
    derivx_pad = np.real(np.fft.ifft2(derivx_ft))
    derivy_pad = np.real(np.fft.ifft2(derivy_ft))
    derivz_pad = np.real(np.fft.ifft2(derivz_ft))

    # remove padding in derivative
    derivx = derivx_pad[padx: padx + nx, pady: pady + ny]
    derivy = derivy_pad[padx: padx + nx, pady: pady + ny]
    derivz = derivz_pad[padx: padx + nx, pady: pady + ny]

    # convert a matrix to a 1D vector
    dx = np.ravel(derivx)
    dy = np.ravel(derivy)
    dz = np.ravel(derivz)

    return dx, dy, dz



def regularized_derivative(x, y, data, shape, order, alpha):

    # wave numbers in the x and y directions
    kx, ky = [k for k in _fftfreqs(x, y, shape, shape)]

    # wavenumber module
    mod_k = np.sqrt(kx ** 2 + ky ** 2)

    # spectral characteristic low pass filter
    gamma_y = ((1j) * ky) / (1 + alpha * (ky ** 2))
    gamma_x = ((1j) * kx) / (1 + alpha * (kx ** 2))
    gamma_z = mod_k / (1 + alpha * (mod_k ** 2))

    # two-dimensional discrete Fourier transform of the observed total anomaly field
    fft_data = np.fft.fft2(np.reshape(data, shape))

    # regularized derivative in the Fourier domain
    fft_derivy = fft_data * (gamma_y ** order)
    fft_derivx = fft_data * (gamma_x ** order)
    fft_derivz = fft_data * (gamma_z ** order)
    #fft_derivz = fft_data * (gamma_z * gamma_z)
    # np.real: returns the real part of the complex argument
    # np.fft.ifft2: calculates the two-dimensional inverse discrete Fourier transform
    derivy = np.real(np.fft.ifft2(fft_derivy))
    derivx = np.real(np.fft.ifft2(fft_derivx))
    derivz = np.real(np.fft.ifft2(fft_derivz))

    # convert a matrix to a 1D vector
    dy = np.ravel(derivy)
    dx = np.ravel(derivx)
    dz = np.ravel(derivz)

    return dx, dy, dz



def s_function(x, y, data, shape, alpha, order):

    norm_sol_dx = []
    norm_sol_dy = []
    norm_sol_dz = []

    for i in range(len(alpha)):

        dx, dy, dz = regularized_derivative(x, y, data, shape, order, alpha[i])

        soma_x = 0
        soma_y = 0
        soma_z = 0

        for i in range(len(dx)):

            elem_dx = dx[i] ** 2
            elem_dy = dy[i] ** 2
            elem_dz = dz[i] ** 2

            soma_x = soma_x + elem_dx
            soma_y = soma_y + elem_dy
            soma_z = soma_z + elem_dz

        norm_dx = np.sqrt(soma_x)
        norm_dy = np.sqrt(soma_y)
        norm_dz = np.sqrt(soma_z)

        norm_sol_dx.append(norm_dx)
        norm_sol_dy.append(norm_dy)
        norm_sol_dz.append(norm_dz)

    norm_sol_dx = np.ravel(norm_sol_dx)
    norm_sol_dy = np.ravel(norm_sol_dy)
    norm_sol_dz = np.ravel(norm_sol_dz)

    norm_sol_dx = norm_sol_dx/max(norm_sol_dx)
    norm_sol_dy = norm_sol_dy/max(norm_sol_dy)
    norm_sol_dz = norm_sol_dz/max(norm_sol_dz)

    return norm_sol_dx, norm_sol_dy, norm_sol_dz



def linear_regression(norm_sol, alpha_test, upper_limit, inferior_limit):

    norm = []
    alpha = []

    for i in range (len(norm_sol)):

        if  (inferior_limit <= np.round(norm_sol[i],1) <= upper_limit):
            norm.append(norm_sol[i])
            alpha.append(alpha_test[i])

    alpha = np.array(alpha).reshape(-1,1)

    # fit a linear regression model
    linreg = LinearRegression().fit(alpha, norm)

    # calculate the angular and linear coefficients for the linear regression
    a = linreg.coef_
    b = linreg.intercept_

    # calculate the regularization parameter associate to Euclidean norm equal to 0.5
    alpha_value = np.log10((0.5 - b)/a)

    return alpha_value



def asa_tdr(dx, dy, dz):

    horiz_deriv = np.sqrt(dx ** 2 + dy ** 2)

    tilt = np.arctan2(dz, horiz_deriv)
    asa = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    return asa, tilt
