import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd
from statistics import mean
from sklearn.preprocessing import StandardScaler

health = pd.read_csv('health_quality_county_gps_coordinates.csv')
health.drop(['lon', 'lat'], axis=1, inplace=True)
print(health.head())

df = pd.read_csv('Zip_MedianRentalPricePerSqft_AllHomes.csv')
df.dropna(axis=1, inplace=True)
df.drop(['RegionName', 'City', 'State', 'SizeRank'], axis=1, inplace=True)

df = df[df.CountyName.isin(health.county_name)]
print(df.head())

df['weighted_metric'] = [np.nan] * len(df.index.values)

for _ in df.index.values:
    row = df.loc[_]
    df.set_value(_, 'weighted_metric', health[health.county_name == row['CountyName']].weighted_metric)

print(df.head())

'''
df.replace('?', np.nan, inplace=True)
df.drop('id', 1, inplace=True)
df.dropna(inplace=True)

x = np.array(df.drop(['class'], 1))
y = np.array(df['class'])
'''

x = np.array(df.drop(['CountyName', 'weighted_metric'], 1))
scaler = StandardScaler()
scaler.fit_transform(x)

y = np.array(df['weighted_metric'])
# y = np.array(df['weighted_metric'].rank(ascending=False))
lab_enc = preprocessing.LabelEncoder()
y = lab_enc.fit_transform(y)

accuracies = []

for i in range(100):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)

    # clf = svm.SVC()
    clf = svm.SVR()
    clf.fit(x_train, y_train)

    accuracy = clf.score(x_test, y_test)
    print('Accuracy:', accuracy)
    accuracies.append(accuracy)

    # sample_measures = np.array([[4,2,8,9,6,8,5,2,1],[2,3,1,2,3,4,3,5,1]])
    # sample_measures = sample_measures.reshape(len(sample_measures), -1)
    #
    # prediciton = clf.predict(sample_measures)
    # print(prediciton)

print(mean(accuracies))




