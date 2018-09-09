import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style


def fadeColor(c1, c2, mix=0):
    # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    # assert len(c1) == len(c2)
    # assert 0 <= mix <= 1, 'mix='+str(mix)
    rgb1 = np.array([int(c1[ii:ii + 2], 16) for ii in range(1, len(c1), 2)])
    rgb2 = np.array([int(c2[ii:ii + 2], 16) for ii in range(1, len(c2), 2)])
    rgb = ((1 - mix) * rgb1 + mix * rgb2).astype(int)
    # cOld='#'+''.join([hex(a)[2:] for a in rgb])
    # print(11,[hex(a)[2:].zfill(2) for a in rgb])
    c = '#' + ('{:}' * 3).format(*[hex(a)[2:].zfill(2) for a in rgb])
    # print(rgb1, rgb2, rgb, cOld, c)
    return c


df = pd.read_csv('boroughs_gps_coordinates.csv')
# print(df.head())

demo_df = pd.read_csv('demographics_city.csv')
# print(demo_df.head())
# print(demo_df.columns.unique())

df = df[df.nta_code.isin(demo_df.nta_code)]

demo_df = demo_df[['nta_code', 'people_per_acre']]
# print(demo_df.head())

df.insert(len(df.columns), 'people_per_acre', np.NaN * len(df.index.values))
# print(df.head())

for _ in df.index.values:
    row = df.loc[_]
    demo_row = demo_df[demo_df.nta_code == row['nta_code']]
    # print(demo_row)
    print(demo_row['people_per_acre'])
    df.set_value(_, 'people_per_acre', demo_row['people_per_acre'])

print(df.head())
df.to_csv('ppa_boroughs_gps_coordinates.csv', index=False)

c1='#FFDFDF' #light red
c2='#E60000' #red
ppa_min = df.people_per_acre.min()
print(ppa_min)
ppa_range = df.people_per_acre.max() - ppa_min
df['percentile'] = (df.people_per_acre - ppa_min)/ppa_range

color_lst = []
for _ in df.percentile:
    color_lst.append(fadeColor(c1, c2, _))

plt.scatter(df.lon, df.lat, c=df.percentile, s=25, linewidths=5, alpha=0.5, cmap='Reds')
# plt.scatter(df.lon, df.lat, color=color_lst, s=15, linewidths=5)
# plt.legend(loc=4)
# mpl.rcParams['image.cmap'] = 'jet'
plt.colorbar()
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.savefig('nyc_demo.png', transparent=True)
plt.show()







