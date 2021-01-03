# This is an oversimplified representation of
# linear Vs logistic regression

# linear regression ## (continuos values)
# y = bx + a

# logistic regression ## (discrete values)
# y = f(bx + a)

# where:
# y = the output
# b = slope
# a = intercept on y axis
# x = the input

# singular value decomposition


from math import exp
import matplotlib.pyplot as plt
# %matplotlib inline

x_values = range(-6, 7)
lin_values = [(0 + 1*x) / 13 for x in range(0, 13)]
log_values = [exp(0 + 1*x) / (1 + exp(0 + 1*x)) for x in x_values]

plt.plot(x_values, lin_values, 'b-^')
plt.plot(x_values, log_values, 'g-*')
plt.legend(['Linear', 'Logistic'])
plt.show()
