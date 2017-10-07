# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 08:47:33 2017

@author: zabbe
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pylab as plt
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor
from patsy import dmatrices

###PART 1###
dataBMI1 = pd.DataFrame(pd.read_csv('height_weight1.csv'))

dataBMI1.head()

dataBMI1.dtypes

plt.hist(dataBMI1.weight,20)

dataBMI1.describe()

modelBMI1 = smf.ols(formula='weight ~ 1 + height', data=dataBMI1).fit()
modelBMI1.summary()

modelBMI2 = smf.ols(formula='weight ~ height', data=dataBMI1).fit()
modelBMI2.summary()

### Test our residuals
residualBMI1 = modelBMI1.resid
residualBMI2 = modelBMI2.resid
# Test for normal residuals
plt.hist(residualBMI1, 20)
plt.hist(residualBMI2, 20)
# Test for heteroscedasticity
plt.plot(modelBMI1.predict(dataBMI1), residualBMI1, '.')
plt.plot(modelBMI2.predict(dataBMI1), residualBMI2, '.')

#With and without the intercept is the same



###PART 2###
dataBMI2 = pd.DataFrame(pd.read_csv('height_weight2.csv'))
dataBMI2.head()
dataBMI2.dtypes

plt.hist(dataBMI2.weight,20) #slightly skewed, but normal enough
dataBMI2.describe()

modelBMI = smf.ols(formula='weight ~ height', data=dataBMI2).fit()
modelBMI.summary()

residualBMI = modelBMI.resid
plt.hist(residualBMI, 20)
plt.plot(modelBMI.predict(dataBMI2), residualBMI, '.') 