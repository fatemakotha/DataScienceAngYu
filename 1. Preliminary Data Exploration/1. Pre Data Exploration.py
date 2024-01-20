import pandas as pd

#%%
#DATA EXPLORATION:
#Read the csv file and store it in the Pandas dataframe:
df = pd.read_csv("QueryResults (1).csv", names=["DATE", "TAG", "POSTS"], header=0)

#%%
#Next, we use .head() and .tail() to look at the first and last 5 rows.
#This allows us to verify that our column naming worked as intended.
df.head(5)
#%%
df.tail(5)


#%%
#Check the dimensions of the DataFrame, we use our old friend .shape. This tells us we have 1991 rows and 3 columns.
df.shape
#%%
