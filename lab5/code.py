import pandas as pd
import matplotlib
from sklearn import datasets, linear_model
import numpy as np

df = pd.read_csv('files/height_weight1.csv', header=0)
heights = df.ix[:,0]
weights = df.ix[:,1]

print heights
print weights

print np.polyfit(heights, weights, 1)
