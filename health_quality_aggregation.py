import pandas as pd
import numpy as np

df = pd.read_csv('out.csv')
print(df.head())

# [2, 6, 1, 2, 3, 5, 6, 2, 6, 5, 2, 4, 5, 4]

weight_vec = {'Family Planning/Natality Indicators': 2, 'Cancer Indicators': 6,
              'Oral Health Indicators': 1, 'Maternal and Infant Health Indicators': 2,
              'Injury Indicators': 3,
              'Socio-Economic Status and General Health Indicators': 5,
              'Cardiovascular Disease Indicators': 6,
              'Child and Adolescent Health Indicators': 2,
              'Obesity and Related Indicators': 6, 'Cirrhosis/Diabetes Indicators': 5,
              'HIV/AIDS and Other Sexually Transmitted Infection Indicators': 2,
              'Respiratory Disease Indicators': 4,
              'Tobacco, Alcohol and Other Substance Abuse Indicators': 5,
              'Communicable Disease Indicators': 4,
              'Occupational Health Indicators': 1}

df['weighted_metric'] = np.nan

for _ in df.index.values:
    row = df.loc[_]
    df.set_value(_, 'weighted_metric', row['rate']/10000*weight_vec[row['health_topic']])

health_dict = dict(zip(df.county_name.unique(), [np.nan]*len(df.county_name.unique())))

ag_df = pd.DataFrame(columns=('county_name', 'weighted_metric'))

for _ in ag_df.columns:
    ag_df[_] = [np.nan] * len(df.county_name.unique())

i = 0
for key, value in health_dict.items():
    sum_metric = df[df.county_name == key].weighted_metric.sum()

    ag_df.iloc[i] = [key, sum_metric]
    i += 1
    print(key + ':', sum_metric)


print(ag_df.head())


# for _ in range(len(df.county_name.unique())):
#    df.loc[_] = []

ag_df.to_csv('aggregated_health_quality.csv', index=False)







