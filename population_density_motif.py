import pandas as pd

df = pd.read_csv('geographic.csv')
print(df.head())

df = df.T
df.dropna(axis=1, inplace=True)
# df['index1'] = df.index

print(df.head())
print(df.shape)
print(df.columns)

bk_df = df[df.index.str.contains('BK')]
print(bk_df.head())
print(bk_df.shape)

qn_df = df[df.index.str.contains('QN')]
print(qn_df.head())
print(qn_df.shape)

bx_df = df[df.index.str.contains('BX')]
print(bx_df.head())
print(bx_df.shape)

mn_df = df[df.index.str.contains('MN')]
print(mn_df.head())
print(mn_df.shape)

si_df = df[df.index.str.contains('SI')]
print(si_df.head())
print(si_df.shape)

boroughs = [bk_df, qn_df, bx_df, mn_df, si_df]
boroughs_str = ['bk', 'qn', 'bx', 'mn', 'si']

lon_col = [i*2 for i in range(5)]
lat_col = [i*2 + 1 for i in range(5)]

# print(bk_df[bk_df.columns.isin(lon_col)].head())
# print(bk_df.filter(items=lat_col).head())

# bk_df['lon'] = bk_df.filter(items=lon_col).mean(axis=1)
# bk_df['lat'] = bk_df.filter(items=lat_col).mean(axis=1)
# bk_df.drop(lon_col + lat_col, axis=1, inplace=True)

# print(bk_df.head())

for _, __ in zip(boroughs, boroughs_str):
    _['lon'] = _.filter(items=lon_col).mean(axis=1)
    _['lat'] = _.filter(items=lat_col).mean(axis=1)
    _.drop(lon_col + lat_col, axis=1, inplace=True)
    _.to_csv(__ + '_gps_coordinates.csv', index=False)

df['lon'] = df.filter(items=lon_col).mean(axis=1)
df['lat'] = df.filter(items=lat_col).mean(axis=1)
df.drop(lon_col + lat_col, axis=1, inplace=True)
print(df.head())
df.to_csv('boroughs_gps_coordinates.csv', index=True)





