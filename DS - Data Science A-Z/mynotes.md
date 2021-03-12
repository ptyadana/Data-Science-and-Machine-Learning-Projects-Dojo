# Stats Refresher

## Types of Variables
+ Categorical
    + Nominal (example: Red, Green, Blue)
    + Oridnal (example: Small, Medium, Large)
+ Numerical
    + Discrete (example: 585 people, 2 dogs)
    + Continuous (example: Age, height, temperature)

## Regressions
+ Linear Regression
    + Simple Linear Regression
        + `y = b0 + b1*x1`
        + `y` is dependent variable, `x` is independent variable, `b1` is coefficient, `b0` is constant.
        + Example can be "relationship between Exprience and Salary($)"
        + ![1.png](02_Modelling/img/1.png)
    + Multiple Linear Regression
        + `y = b0 + b1*x1 + b2*x2+ bn*xn`
+ Logisitic Regression
    + Simple Logistic Regression
    + Multiple Logistic Regression

## Ordinary Least Square
+ Simple Linear Regression draws many lines and tries to find the best fit line with Minium value of Sum of squre of difference between Actual Value and Predicted Value (the smallest sum value). This method is called Ordinary Least Square.

+ y - y^ is the difference between Actual Value - Predicted Value.

+ ![2.png](02_Modelling/img/2.png)

# R Squared
+ **Sum of Square of Residual** : Sum of differences between Acutal values and Predicted values
+ **Total Sum of Square**: Sum of differences between Average line and Actual values
+ `R Squared = 1 - (SSres / SStot)`
+ R Squared value tells us how good is our best fit line compared to Average line.
+ The closer R squared value is to 1, the better our model is.
+ ![3.png](02_Modelling/img/3.png)

## Adjusted R-Squared
+ ![4.png](02_Modelling/img/4.png)

# Using Tool Gretl
+ [gretl](http://gretl.sourceforge.net/)

-----------

# Simple Linear Regression Model
## Interpreting Ordinary Least Squares values via Gretl
+ Open File in gretl. Model > Ordinary Least Squares
    + Dependent Variable: Salary, Independent Variable: Year of Experiences
    + Coefficient: 1 unit increase in Year of Experiences will result in 9449.96$ increase in Salary.
    + p-value: tells the statistically significance between the variables. the smaller the p-value, the better. In this case 1.14e-020.
+ Graphs > Fitted, Actual Plots > Fitted Vs Actual
+ Forcasts > 