"""
A manager wants to find the relationship between the number of hours 
that a plant is operational in a week and weekly production.

Production Hours(x) : 34, 35, 39, 42, 43, 47
Production volume(y): 102, 109, 137, 148, 150, 158
"""

from scipy.stats import linregress

x = [34, 35, 39, 42, 43, 47]
y = [102, 109, 137, 148, 150, 158]

slope = round(linregress(x, y).slope, 1)
intercept = round(linregress(x,y ).intercept, 1)

#formula
print(f" y = {intercept} + {slope}x")

"""
if manager wants to produce 125 units per week, then he should run
x = -46.0 + 4.5x
125 = -46.0 + 4.5x
x = 38 hours per week
"""
