import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

def time_of_day(time_stamp):
    if int(time_stamp) < 12:
        return "Morning"
    elif int(time_stamp) < 18:
        return "Afternoon"
    elif int(time_stamp) < 21:
        return "Evening"
    else:
        return "Night"
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['hour'] = df['hour_beginning'].dt.hour
df['time_of_day'] = df['hour'].apply(time_of_day)
print(df.head)

hourly_counts = df.groupby(df['time_of_day'])['Pedestrians'].sum()
plt.figure(figsize=(12, 6))
hourly_counts.plot(kind='bar', color='orange')
plt.title('Total Pedestrian Counts by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Pedestrian Count')
plt.grid(axis='y')  #grid created alone y axis
plt.tight_layout()
plt.show()