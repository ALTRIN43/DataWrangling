!pip install pandas
!pip install numpy
!pip install matplotlib
import pandas as pd
import matplotlib.pylab as plt 

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(file_path, name=headers)

df.head() # prints the first five rows 

# Identify and handle missing values

#convert "?" to NaN
import numpy as np

df.replace("?", np.nan, inplace=True)
df.head()

# Evaluate missing data
# .isnull()
missing_data = df.isnull()# True if null, False if not null
missing_data.head()
# .notnull()
missing_data = df.notnull()# True if not null, False if null
missing_data.head()

# Count missing values in each column
for column in missing_data.columns.values.tolist():
  print(column)
  print(missing_data[column].value_counts())
  print("")
