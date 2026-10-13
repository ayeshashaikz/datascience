# SciPy Example Program Covering Important Functions

import numpy as np
from scipy import stats
from scipy import linalg
from scipy import optimize
from scipy import integrate
from scipy import interpolate
from scipy import signal
from scipy import spatial
from scipy import fft
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg
from scipy import special
from scipy import constants
from scipy import ndimage
from scipy import io


# ---------------------------------------------------
# 1. scipy.stats - Statistical Functions
# ---------------------------------------------------

print("\n1. scipy.stats - Statistical Functions")

data = [10, 20, 20, 30, 40, 50]

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=True))
print("Standard Deviation:", np.std(data))
print("Skewness:", stats.skew(data))
print("Kurtosis:", stats.kurtosis(data))

# Pearson correlation
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation, p_value = stats.pearsonr(x, y)
print("Pearson Correlation:", correlation)
print("P-value:", p_value)

# One sample t-test
t_stat, p_val = stats.ttest_1samp(data, 25)
print("T-test Statistic:", t_stat)
print("T-test P-value:", p_val)


# ---------------------------------------------------
# 2. scipy.linalg - Linear Algebra Functions
# ---------------------------------------------------

print("\n2. scipy.linalg - Linear Algebra Functions")

A = np.array([[3, 2], [1, 4]])
B = np.array([7, 9])

solution = linalg.solve(A, B)
print("Solution of Linear Equations:", solution)

print("Determinant:", linalg.det(A))
print("Inverse Matrix:\n", linalg.inv(A))
print("Eigenvalues:", linalg.eigvals(A))


# ---------------------------------------------------
# 3. scipy.optimize - Optimization Functions
# ---------------------------------------------------

print("\n3. scipy.optimize - Optimization Functions")

# Minimize function: f(x) = x^2 + 5x + 6
def objective_function(x):
    return x**2 + 5*x + 6

minimum = optimize.minimize(objective_function, x0=0)
print("Minimum Value Found At:", minimum.x)
print("Minimum Function Value:", minimum.fun)

# Root finding: x^2 - 4 = 0
def equation(x):
    return x**2 - 4

root = optimize.root(equation, x0=1)
print("Root of Equation:", root.x)


# ---------------------------------------------------
# 4. scipy.integrate - Integration Functions
# ---------------------------------------------------

print("\n4. scipy.integrate - Integration Functions")

# Integrate f(x) = x^2 from 0 to 3
def function_to_integrate(x):
    return x**2

integral_value, error = integrate.quad(function_to_integrate, 0, 3)
print("Integral of x^2 from 0 to 3:", integral_value)
print("Integration Error:", error)

# Solving differential equation: dy/dt = -2y
def differential_equation(t, y):
    return -2 * y

solution_ode = integrate.solve_ivp(
    differential_equation,
    t_span=(0, 5),
    y0=[1],
    t_eval=np.linspace(0, 5, 6)
)

print("ODE Time Points:", solution_ode.t)
print("ODE Solution:", solution_ode.y)


# ---------------------------------------------------
# 5. scipy.interpolate - Interpolation Functions
# ---------------------------------------------------

print("\n5. scipy.interpolate - Interpolation Functions")

x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 4, 8, 16, 32])

# Cubic spline interpolation
cubic_model = interpolate.CubicSpline(x_data, y_data)

new_x = 2.5
new_y = cubic_model(new_x)

print("Interpolated Value at x = 2.5:", new_y)


# ---------------------------------------------------
# 6. scipy.signal - Signal Processing Functions
# ---------------------------------------------------

print("\n6. scipy.signal - Signal Processing Functions")

signal_data = np.array([1, 3, 7, 1, 2, 6, 0, 1])

peaks, properties = signal.find_peaks(signal_data)

print("Signal Data:", signal_data)
print("Peak Positions:", peaks)
print("Peak Values:", signal_data[peaks])

# Smoothing using Savitzky-Golay filter
smooth_signal = signal.savgol_filter(signal_data, window_length=5, polyorder=2)
print("Smoothed Signal:", smooth_signal)


# ---------------------------------------------------
# 7. scipy.spatial - Distance and Spatial Functions
# ---------------------------------------------------

print("\n7. scipy.spatial - Distance Functions")

point1 = [1, 2]
point2 = [4, 6]

euclidean_distance = spatial.distance.euclidean(point1, point2)
cityblock_distance = spatial.distance.cityblock(point1, point2)

print("Euclidean Distance:", euclidean_distance)
print("Manhattan Distance:", cityblock_distance)

points = np.array([[1, 2], [3, 4], [5, 6]])
distance_matrix = spatial.distance_matrix(points, points)

print("Distance Matrix:\n", distance_matrix)


# ---------------------------------------------------
# 8. scipy.fft - Fourier Transform Functions
# ---------------------------------------------------

print("\n8. scipy.fft - Fourier Transform Functions")

time_signal = np.array([1, 2, 3, 4])

fft_result = fft.fft(time_signal)
inverse_fft = fft.ifft(fft_result)

print("Original Signal:", time_signal)
print("FFT Result:", fft_result)
print("Inverse FFT Result:", inverse_fft)


# ---------------------------------------------------
# 9. scipy.sparse - Sparse Matrix Functions
# ---------------------------------------------------

print("\n9. scipy.sparse - Sparse Matrix Functions")

dense_matrix = np.array([
    [0, 0, 3],
    [4, 0, 0],
    [0, 5, 0]
])

sparse_matrix = sparse.csr_matrix(dense_matrix)

print("Dense Matrix:\n", dense_matrix)
print("Sparse Matrix:\n", sparse_matrix)
print("Sparse Matrix Converted Back to Dense:\n", sparse_matrix.toarray())

# Sparse linear equation solving
A_sparse = sparse.csr_matrix([[3, 2], [1, 4]])
B_sparse = np.array([7, 9])

sparse_solution = sparse_linalg.spsolve(A_sparse, B_sparse)
print("Sparse Matrix Solution:", sparse_solution)


# ---------------------------------------------------
# 10. scipy.special - Special Mathematical Functions
# ---------------------------------------------------

print("\n10. scipy.special - Special Functions")

print("Gamma Function gamma(5):", special.gamma(5))
print("Factorial of 5:", special.factorial(5))
print("Error Function erf(1):", special.erf(1))
print("Combination 5C2:", special.comb(5, 2))
print("Permutation 5P2:", special.perm(5, 2))


# ---------------------------------------------------
# 11. scipy.constants - Scientific Constants
# ---------------------------------------------------

print("\n11. scipy.constants - Scientific Constants")

print("Speed of Light:", constants.c)
print("Acceleration Due to Gravity:", constants.g)
print("Planck Constant:", constants.h)
print("Pi Value:", constants.pi)


# ---------------------------------------------------
# 12. scipy.ndimage - Image Processing Functions
# ---------------------------------------------------

print("\n12. scipy.ndimage - Image Processing Functions")

image = np.array([
    [10, 10, 10],
    [10, 100, 10],
    [10, 10, 10]
])

blurred_image = ndimage.gaussian_filter(image, sigma=1)
rotated_image = ndimage.rotate(image, angle=45, reshape=False)

print("Original Image Matrix:\n", image)
print("Blurred Image:\n", blurred_image)
print("Rotated Image:\n", rotated_image)


# ---------------------------------------------------
# 13. scipy.io - Input and Output Functions
# ---------------------------------------------------

print("\n13. scipy.io - Input and Output Functions")

sample_data = {
    "marks": np.array([80, 85, 90]),
    "attendance": np.array([75, 80, 95])
}

# Save data in MATLAB .mat format
io.savemat("student_data.mat", sample_data)

# Load the saved .mat file
loaded_data = io.loadmat("student_data.mat")

print("Data Saved and Loaded Successfully")
print("Loaded Marks:", loaded_data["marks"])
print("Loaded Attendance:", loaded_data["attendance"])


print("\nSciPy Program Completed Successfully")
