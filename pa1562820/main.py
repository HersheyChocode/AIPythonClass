import time
import pandas as pd
"""
startTime = time.time()
print("Hello")
seconds = time.time()-startTime
print("Time taken", seconds)
print('Time Taken:', time.strftime("%H:%M:%S", time.gmtime(seconds)))
"""
dataset = pd.read_csv('nba.csv')
print(dataset.head())
print(dataset.dtypes)


print("Iloc print", dataset.iloc[10,5])

dropped_df = dataset.drop(['Name','Team'], axis=1)
print(dropped_df)

dfObj = pd.DataFrame(columns =["Name","Team"])
dfObj = dfObj.append({"Name":"Harshini","Team":"yay"}, ignore_index=True)
