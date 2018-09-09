import pandas as pd
import numpy as np

df = pd.read_csv('Zip_MedianRentalpricePerSqft_AllHomes.csv')
print(df.head())

df.dropna(axis=1, inplace=True)
print(df.shape)

Man_zip = [10026, 10027, 10030, 10037, 10039, 10001,
           10011, 10018, 10019, 10020, 10036, 10029,
           10035, 10010, 10016, 10017, 10022,
           10012, 10013, 10014,
           10004, 10005, 10006, 10007, 10038, 10280,
           10002, 10003, 10009,
           10021, 10028, 10044, 10065, 10075, 10128,
           10023, 10024, 10025,
           10031, 10032, 10033, 10034, 10040]

Bronx_zip = [10453, 10457, 10460,
             10458, 10467, 10468,
             10451, 10452, 10456,
             10454, 10455, 10459, 10474,
             10463, 10471,
             10466, 10469, 10470, 10475,
             10461, 10462, 10464, 10465, 10472, 10473]

Brooklyn_zip = [11212, 11213, 11216, 11233, 11238,
                11209, 11214, 11228,
                11204, 11218, 11219, 11230,
                11234, 11236, 11239,
                11223, 11224, 11229, 11235,
                11201, 11205, 11215, 11217, 11231,
                11203, 11210, 11225, 11226,
                11207, 11208,
                11211, 11222,
                11220, 11232,
                11206, 11221, 11237]

Queens_zip = [11361, 11362, 11363, 11364,
              11354, 11355, 11356, 11357, 11358, 11359, 11360,
              11365, 11366, 11367,
              11412, 11423, 11432, 11433, 11434, 11435, 11436,
              11101, 11102, 11103, 11104, 11105, 11106,
              11374, 11375, 11379, 11385,
              11691, 11692, 11693, 11694, 11695, 11697,
              11004, 11005, 11411, 11413, 11422, 11426, 11427, 11428, 11429,
              11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421,
              11368, 11369, 11370, 11372, 11373, 11377, 11378]

SIsland_zip = [10302, 10303, 10310,
               10306, 10307, 10308, 10309, 10312,
               10301, 10304, 10305, 10314]

man_df = df[df.RegionName.isin(Man_zip)]
bronx_df = df[df.RegionName.isin(Bronx_zip)]
brook_df = df[df.RegionName.isin(Brooklyn_zip)]
queens_df = df[df.RegionName.isin(Queens_zip)]
sisland_df = df[df.RegionName.isin(SIsland_zip)]

# print(man_df.head())
# print(man_df.shape)
# print(bronx_df.head())
# print(bronx_df.shape)
# print(brook_df.head())
# print(brook_df.shape)
# print(queens_df.head())
# print(queens_df.shape)
# print(sisland_df.head())
# print(sisland_df.shape)

df.insert(0, 'Borough', ['NAN'] * len(df.index.values))

for _ in df.index.values:
    row = df.loc[_]
    zip = row['RegionName']

    if zip in Man_zip:
        df.set_value(_, 'Borough', 'Manhattan')

    elif zip in Bronx_zip:
        df.set_value(_, 'Borough', 'Bronx')

    elif zip in Brooklyn_zip:
        df.set_value(_, 'Borough', 'Brooklyn')

    elif zip in Queens_zip:
        df.set_value(_, 'Borough', 'Queens')

    elif zip in SIsland_zip:
        df.set_value(_, 'Borough', 'Staten Island')

df = df[df.Borough != 'NAN']
print(df.head())

df.to_csv('Borough_Zip_MedianRentalpricePerSqft_AllHomes.csv', index=False)








