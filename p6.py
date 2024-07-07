# model creation

# import lib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pickle import *

#load data
data = pd.read_csv("esmarch24.csv")

#feature and target

feature = data[["exp"]]
target = data["sal"]


#train and test
x_train, x_test, y_train, y_test = train_test_split(feature.values, target)


#model
model = LinearRegression()
model.fit(x_train, y_train)

#model creation
f = open("sal.pkl", "wb")
dump(model, f)
f.close()