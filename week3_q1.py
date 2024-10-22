from calendar import day_name

import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['day_name'] = df['hour_beginning'].dt.day_name()
print(df.groupby('day_name')['Pedestrians'].sum())
#print(df['day_name'].head())
weekday_df = df[((df['day_name']!= 'Saturday') & (df['day_name'] != 'Sunday'))]

plt.figure(figsize=(12, 6))
#plt.plot(weekday_df['day_name'], weekday_df['Pedestrians'], color='blue')
weekday_df.groupby('day_name')['Pedestrians'].sum().plot()
plt.title('Pedestrian Counts Over Time')
plt.xlabel('Day of Week')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()
