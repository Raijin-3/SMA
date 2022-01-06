import pandas as pd
import numpy
import datetime

raw_data = pd.read_csv('data.csv')

#reversing the data
data = raw_data.iloc[::-1]


#deleting the empty columns
data.pop("Unnamed: 5")
data.pop("Unnamed: 6")
data.pop("Unnamed: 7")
data.pop("Unnamed: 8")
data.pop("Unnamed: 9")
data.pop("Unnamed: 10")
data.pop("Unnamed: 11")



clean_data = data.reset_index(drop=True)

#Getting rid of chained error occure due to multi dataframe calling
pd.options.mode.chained_assignment = None
data_close = clean_data['Close'].str.replace(',','')

#Calculating the simple mean average and assigning it to SMA column
clean_data['SMA'] = data_close.rolling(window =21).mean()


#converting the dates into days
clean_data['Day of Week'] = [datetime.datetime.strptime(item, '%b  %d, %Y').strftime("%A") for item in clean_data['Date'] ]


#calculating and assiging the value of net changes
#from friday closing to monday opening
friday_closings = clean_data.loc[clean_data['Day of Week'] == "Friday"] ['Close']
fc = friday_closings.str.replace(',','').astype(float)
fcr = fc.reset_index(drop=True)

monday_openings = clean_data.loc[clean_data['Day of Week'] == "Monday"] ['Open']
mo = monday_openings.str.replace(',','').astype(float)
mor = mo.reset_index(drop=True)

clean_data['Net Changes'] = fcr.sub(mor)

fcd= clean_data.loc[clean_data['Day of Week'] == "Friday"] ['Date']
clean_data['Friday Closing Date'] = fcd.reset_index(drop=True)
clean_data['Friday Closing'] = fcr
mod = clean_data.loc[clean_data['Day of Week'] == "Monday"] ['Date']
clean_data['Monday Opening Date'] =mod.reset_index(drop=True)
clean_data['Monday Opening'] = mor


  
    

#calculating the percentage of changes
perc_changes = clean_data['Net Changes']/fcr
clean_data['Net percentage of changes'] = perc_changes*100


 
#Ordring the column of output file   


clean_data =clean_data[['Friday Closing Date', 'Friday Closing', 'Monday Opening Date', 'Monday Opening', 'Net Changes', 'Net percentage of changes']]
clean_data.to_csv('NetChanges.csv')