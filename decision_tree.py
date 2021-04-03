import numpy as np
import pandas as pd
import datetime
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans

class BlueBikes:

    def read_data(self):
        """
        Reads in the blue bikes data and converts the columns with datetimes to time

        Returns:
            A dataframe containing the formatted data
        """

        # data source: https://s3.amazonaws.com/hubway-data/index.html
        blue_bikes_csv = pd.read_csv("data/202102-bluebikes-tripdata.csv")

        blue_bikes_csv['starttime'] = pd.to_datetime(blue_bikes_csv['starttime'])
        blue_bikes_csv['stoptime'] = pd.to_datetime(blue_bikes_csv['stoptime'])
        blue_bikes_csv['starttime'] = [datetime.datetime.time(d) for d in blue_bikes_csv['starttime']] 
        blue_bikes_csv['stoptime'] = [datetime.datetime.time(d) for d in blue_bikes_csv['stoptime']] 

        return blue_bikes_csv

    def prep_for_analysis(self, data):
        """
        Prep the given blue bikes data for regression analysis

        Params:
        - data : the data to prep

        Returns:
            The formatted data
        """
        # add cluster labels for end station
        coords = data[['end station latitude', 'end station longitude']].values
        data["end_station_cluster"] = self.make_clusters(coords, 40)

        # remove start and end time
        data = data.drop(['starttime', 'stoptime'], axis=1)

        # remove repetitive information
        data = data.drop(['start station name', 'end station name', 'start station latitude', 'start station longitude', 'end station latitude', 'end station longitude', 'end station id', "postal code", "bikeid"], axis=1)

        # convert categorical variables to dummies
        categorical_variables = ["usertype"]
        data = pd.get_dummies(data, columns = categorical_variables)

        return data

    def make_clusters(self, coords, num_clusters):
        """
        Uses KMeans to cluster the given coordinates

        Params:
        - coords : the coordinates to cluster
        - num_clusters : the number of clusters to make

        Returns:
            The labels of the clusters
        """
        kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(coords)
        cluster_labels = kmeans.labels_
        num_clusters = len(set(cluster_labels))
        print('Number of clusters: {}'.format(num_clusters))

        return cluster_labels

    def decision_tree_analysis(self, data, y_variable, save_results=True):
        """
        Performs a decision tree analysis using the given data

        Params:
        - data : the complete dataset
        - y_variable : the dependent variable 
        - save_results : save the model results to a file

        Returns:
            The decision tree model
        """

        # select variables
        x = data.drop([y_variable], axis=1)
        y = data[y_variable]

        # split into test and training data
        X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.25, random_state=0)

        # use a decision tree regressor to predict
        model = DecisionTreeRegressor().fit(X_train, Y_train)
        prediction = model.predict(X_test)

        # score = correct predictions / total number of data points
        score = model.score(X_test, Y_test)
        print("model score:", score)

        if save_results:
            results_dataset = X_test.copy()
            results_dataset['prediction'] = prediction
            results_dataset['actual'] = Y_test
            results_dataset.to_csv("results_dataset.csv")

        return model

b = BlueBikes()
print("Reading in data...")
data = b.read_data()
print("Data contains", len(data.index), "rows.")
print("Preparing data for analysis...")
data = b.prep_for_analysis(data)
print("Data for analysis contains", data.shape[1], "columns.")
print("Performing decision tree analysis...")
model = b.decision_tree_analysis(data, "end_station_cluster")
print("Analysis complete.")









