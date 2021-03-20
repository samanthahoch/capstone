import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# data source: https://s3.amazonaws.com/hubway-data/index.html
blue_bikes_csv = pd.read_csv("data/202102-bluebikes-tripdata.csv")

# print column names
print(list(blue_bikes_csv))

# remove start and end time
blue_bikes_csv = blue_bikes_csv.drop(['starttime', 'stoptime'], axis=1)

# remove repetitive information
blue_bikes_csv = blue_bikes_csv.drop(['start station name', 'end station name', 'start station latitude', 'start station longitude', 'end station latitude', 'end station longitude'], axis=1)

categorical_variables = ["usertype", "postal code"]
y_variable = "end station id"

bike = blue_bikes_csv.copy()
bike = pd.get_dummies(bike, columns = categorical_variables)
print(bike)
x = bike.drop([y_variable], axis=1)
y = bike[y_variable]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

DT_model = DecisionTreeRegressor(max_depth=3).fit(X_train, y_train)
DT_predict = DT_model.predict(X_test)
print(DT_predict)

print("max end station id", max(blue_bikes_csv['end station id']))
print("max predicted end station id", max(DT_predict))



