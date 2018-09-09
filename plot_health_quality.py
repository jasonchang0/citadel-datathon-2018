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

df = pd.read_csv('aggregated_health_quality.csv')

df_ref = pd.read_csv('food_service_establishment_inspections.csv')

df_ref['county'] = df_ref.county.str.lower()
df_ref['county'] = df_ref.county.str.capitalize()
print(df_ref.head())

# avg_df = pd.DataFrame(columns=('lon', 'lat', 'weighted_metric'))
#
# for _ in avg_df.columns:
#     avg_df[_] = [np.nan] * len(df.county_name.unique())

df['lon'] = [np.nan] * len(df.county_name.unique())
df['lat'] = [np.nan] * len(df.county_name.unique())

print(df.head())

for _ in df.index.values:
    row = df.loc[_]
    df.set_value(_, 'lon', df_ref[df_ref.county == row['county_name']].longitude.mean())
    df.set_value(_, 'lat', df_ref[df_ref.county == row['county_name']].latitude.mean())

print(df.head())

df.to_csv('health_quality_county_gps_coordinates.csv', index=False)

c1='#FFDFDF' #light red
c2='#E60000' #red

wm_min = df.weighted_metric.min()
print(wm_min)
wm_range = df.weighted_metric.max() - wm_min
df['percentile'] = (df.weighted_metric - wm_min)/wm_range

color_lst = []
for _ in df.percentile:
    color_lst.append(fadeColor(c1, c2, _))

plt.scatter(df.lon, df.lat, c=df.percentile, s=25, linewidths=5, cmap='Reds')

plt.colorbar()
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.savefig('county_health_demo.png', transparent=True)
plt.show()







