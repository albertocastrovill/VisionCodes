import pandas as pd

df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")
gear_counts = df['# Gears'].value_counts()
#gear_counts.plot(kind='bar')

import seaborn as sns
sns.set()

#gear_counts.plot(kind='bar')

df.head()