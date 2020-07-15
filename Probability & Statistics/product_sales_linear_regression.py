"""
A company wants to determine the linear relationship between the selling price of their product in US dollars
 and the number of units sold in thousands. 
Perform a linear regression on the following data to determine the linear predictor function
"""

from scipy.stats import linregress

x = [12, 14, 16, 18, 20]
y = [54, 57, 49, 48, 42]

slope = round(linregress(x, y).slope, 1)
intercept = round(linregress(x, y).intercept, 1)

#formula
print(f" y = {intercept} + {slope}x")
