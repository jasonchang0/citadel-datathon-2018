import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import seaborn as sns

style.use('fivethirtyeight')

df = pd.read_csv('avgmedrent_bytype.csv')
df.dropna(axis=0, inplace=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df['num_time'] = np.nan

for _ in df.index.values:
    row = df.loc[_]
    # time = int(row['time'].replace('-', ''))
    year = row['time'].split('-')[0]
    month = row['time'].split('-')[1]
    time = datetime.datetime(int(year), int(month), 1)
    df.set_value(_, 'num_time', time)

print(df.head())
print(df.shape)

type_lst = list(df.type.unique())
color_lst = []
# color_lst = ['r','g','b','c','k','y','m']
print(type_lst)

cmap = plt.cm.plasma
norm = mpl.colors.Normalize(vmin=1.5, vmax=4.5)
color_pal = sns.color_palette("hls", len(df.type.unique()))


for _ in df.type.unique():
    df_type = df[df.type == _]
    # color = cmap(norm(type_lst.index(_)))
    color = color_pal[type_lst.index(_)]
    plt.plot(df_type.num_time, df_type.avg_rent, c=color, label=type_lst.index(_))
    color_lst.append(color)

    # plt.plot_date(df_type.num_time, df_type.avg_rent, c=cmap(norm(type_lst.index(_))))

# plt.ylim(ymin=0)

# plt.plot(df.num_time, df.avg_rent, c=df.type)
# plt.legend(handles=color_lst, labels=df.type.unique())

# plt.plot(df.num_time, df.avg_rent, c=cmap(norm(type_lst.index(_))))
# plt.legend()

plt.legend(df.type.unique())

# average median housing cost (ft^2) rising overtime

plt.xlabel('Time')
plt.ylabel('Avg. Median Cost per ft^2 ($)')
plt.title('Average Median Housing Cost (ft^2) Rising Overtime')

plt.savefig('nyc_demo.png', transparent=True)
plt.show()



