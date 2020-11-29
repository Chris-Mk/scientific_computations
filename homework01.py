from numpy import *
from matplotlib.pyplot import *


# Task 1

# Returns the approximation of the natural logarithm of a real number x after n
# iterations by computing arithmetic and geometric means.

# input:
# x: the number to approximate the natural logarithm of
# n: the number of iterations

# output:
# approximation of ln(x)

def approx_ln(x, n):  # defining a function for approximating ln
    a0 = (1 + x) / 2  # the initial value for a
    g0 = sqrt(x)  # the initial value for g

    # The for-loop computes the next arithmetic an geometric means by iteration
    # method.

    for i in range(n):  # the for-loop performs the iterations
        a = (a0 + g0) / 2  # computing a with previous values for a and g
        g = sqrt(a * g0)  # computing g with the current value of a and the
        a0 = a  # reassigning a to a0
        g0 = g  # reassigning g to g0

    return (x - 1) / a  # returning the approximation


print(approx_ln(2, 100))
# %%
# Task 2

# Plots of the natural logarithm-function and the approximation for various
# numbers of iterations

x = linspace(1, 1000, 1000)  # the values on the x-axis

ln = log(x)  # the natural log of the x-values
y = [approx_ln(x, m) for m in range(1, 7)]  # the approximation of the natural log of the x-values for m iterations

plot(x, ln, label="ln(x)")  # the plot of the natural log
legend()
xlabel("x-axis")
ylabel("ln")
title("Graph of ln and its approximations")

for m in range(2, 6):  # for different numbers of iterations
    plot(x, (y[m]), label=f"{m} iterations")  # the plot of the approximation of ln
    legend()

# %%
# Task 2 continuation

# The error of the approximated function for different numbers of iterations


for m in range(2, 6):  # different numbers of iterations
    err = (abs(ln - (y[m])))  # the error between the approximation and ln
    plot(x, err, label=f"{m} iterations")  # the plot of the errors
    xlim(0, 10)
    ylim(-0.001, 0.0025)
    legend()

# %%
# Task 3

# Plot of the error of the approximation of ln(1.41) for different numbers of
# iterations.

iterations = linspace(1, 20, 19)  # the values on the x-axis

app_ln = [approx_ln(1.41, b) for b in
          range(1, 20)]  # the approximation of ln at x=1.41 for different numbers of iterations

err2 = [abs((app_ln[int(g)]) - log(1.41)) for g in range(0, 19)]  # the error between the approximation and ln
xlabel("n")
ylabel("error")
title("The error of the approximation for x=1.41")
plot(iterations, err2)  # the plot of the error vs iterations


# %%

# Task 4

# An accelerated method for computing the natural logarithm of x for n iterations
# using Carlsson's method.

# input:
# x: the number to approximate the natural logarithm of
# n: the number of iterations

# output:
# approximation of ln(x)

def fast_approx_ln(x, n):  # defining a function for approximating ln
    a0 = (1 + x) / 2  # the initial value for a
    g0 = sqrt(x)  # the initial value for g

    d = [[a0]]  # a list containg the list of a's

    # The for-loop computes the next arithmetic an geometric means by iteration
    # method and adds them to the first list in the list d.

    for i in range(n):
        a = (a0 + g0) / 2  # computing a with previous values for a and g
        g = sqrt(a * g0)  # computing g with the current value of a and the
        a0 = a  # reassigning a to a0
        g0 = g  # reassigning g to g0
        d[0].append(a)  # appending the a-values to the first list in the list d

    # Creating lists of a's and appending to d

    for k in range(1, n + 1):
        d.append([])  # appends an empty list to d
        for i in range(0, n + 1):
            d[k].append(
                (d[k - 1][i] - (4 ** (-k) * d[k - 1][i - 1])) / (1 - 4 ** (-k)))  # fills the empty list with a's
    return (x - 1) / (d[n][n])  # returns the approximation of ln(x) for n iterations


print(fast_approx_ln(2, 100))
# %%
# Task 5

# A plot of the speed of convergence of the fast approximation of ln,
# similar to the one given in the assignment

x = linspace(0, 20, 100)  # the values on the x-axis

nat_log = log(x)  # the natural log of the x-values
ln_approx = [fast_approx_ln(x, m) for m in range(2, 10)]  # the fast approximation
# of ln of the x-values


for z in range(1, 5):  # different numbers of iterations
    err3 = (abs(nat_log - (ln_approx[z])))  # the error between the approximation and ln
    yscale("log")
    xlabel("x")
    ylabel("Error")
    title("Error behavior of the accelerated Carlsson Method for the log")
    xlim(0, 20)
    # ylim(1e-19, 1e-5)
    xticks(arange(0, 21, 5))
    # yticks([10 ** (-i) for i in range(5, 20)])
    plot(x, err3, label=f"{z + 1} iterations")  # plot of the errors
    legend()
