import numpy as np
import pandas as pd
from scipy import stats
# function to calculate the mean of x and y
def calculate_mean(arr):
    return np.mean(arr)
#end of function

#function to calculate covarience of x and y
def calculate_covariance(x, y):
    n = len(x)
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    cov_natrix=np.cov(x,y)
    covariance = cov_natrix[0,1]
    return covariance
#end of function
#function to calculate standard deviation of x and y
def calculate_std(arr):
    return np.std(arr, ddof=1)
#end of function

# To calculate Correlation Coefficient directly using numpy
def correaletion_coefficient(x, y):
    return np.corrcoef(x, y)[0, 1]
#end of function

x=np.array([65,66,67,67,68,69,70,72])
y=np.array([67,68,65,68,72,72,69,71])


mean_x = calculate_mean(x)
mean_y = calculate_mean(y)
print("Mean of x:", mean_x)
print("Mean of y:", mean_y)

covarience=calculate_covariance(x, y)

print("Covariance of x and y:", covarience)


std_x = calculate_std(x)
std_y = calculate_std(y)
print("Standard deviation of x:", std_x)
print("Standard deviation of y:", std_y)


r = correaletion_coefficient(x, y)


print("Correlation Coefficient (r):", r)

#Correlation Coefficient (r): 0.6030226891555273

#for lines of regression y on x

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(f"Regression line y on x: y =  {slope:.2f}x + {intercept:.2f}  ")

slope, intercept, r_value, p_value, std_err = stats.linregress(y, x)
print(f"Regression line x on y: x =  {slope:.2f}y + {intercept:.2f}  ")
