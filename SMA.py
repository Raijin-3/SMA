#Converted the excel file to csv for better operation


import pandas as pd


#reading the file
raw_data = pd.read_csv('data.csv')

#Reversing the dataframe
data = raw_data.loc[::-1]


#Just cleaning the file
data.pop("Unnamed: 5")
data.pop("Unnamed: 6")
data.pop("Unnamed: 7")
data.pop("Unnamed: 8")
data.pop("Unnamed: 9")
data.pop("Unnamed: 10")
data.pop("Unnamed: 11")


#Replacing the commas in values
data_close = data['Close'].str.replace(',','')


#Finding the simple mean average as well as assigning it into a different column
data['SMA'] = data_close.rolling(window =21).mean()



#Saving the result into a csv file
data.to_csv('simplemeanaverage.csv')