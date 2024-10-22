import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['year'] = df['hour_beginning'].dt.year
filtered_df = df[df['year'] == 2019]


plt.figure(figsize=(10, 6))
sns.boxplot(data= filtered_df, x='weather_summary', y='Pedestrians')
plt.title('Pedestrian Counts by Weather Summary in 2019')
plt.xlabel('Weather Summary')
plt.ylabel('Pedestrian Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

