"""
A pharmacy delivers medications to the surrounding community.
Drivers can make several stops per delivery.
The owner would like to predict the length of time a delivery will take based on one or two related variables.
"""

from sklearn.linear_model import LinearRegression

x1, x2 = [1,3,2,3,1], [8,4,9,6,3]
y = [29, 31, 36, 35, 19]

reg = LinearRegression()
reg.fit(list(zip(x1,x2)), y)
b1, b2 = reg.coef_[0], reg.coef_[1]
b0 = reg.intercept_

print(f'y = {b0:.{3}} + {b1:.{3}}x1 + {b2:.{3}}x2')