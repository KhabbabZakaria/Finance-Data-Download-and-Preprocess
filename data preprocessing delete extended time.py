import pandas as pd
import csv
import requests
import time
import copy
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def getdate_val(date_val):
    string = ''
    for i in date_val:
        if i != ' ':
            string = string + i
        else:
            break
    return string

folders = [name for name in os.listdir(".") if os.path.isdir(name) and name!= 'preprocessed_dir' and name!= 'NASDAQ data' and name!= 'large caps']
print(folders)

current_dir = os.getcwd()
ref_folder_name = 'DOW'
ref_folder = os.path.join(current_dir, ref_folder_name)

dir_list = []
years = [1]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
for year in years:
    for month in months:
        element = ref_folder_name + 'year' + str(year) + 'month' + str(month) + '.csv'
        dir_list.append(element)



for i in range(len(dir_list)):
    del_rows = []
    csv_file = dir_list[i]
    csv_path = os.path.join(ref_folder, csv_file)
    print(csv_path)
    df_csv = pd.read_csv(csv_path, delimiter=',')
    for j in range(len(df_csv)):
        date_val = getdate_val(df_csv['time'].iloc[j])
        highest = date_val + ' ' + '16:00:00'
        lowest = date_val + ' ' + '09:30:00'

        current_time = df_csv['time'].iloc[j]
        deltah = pd.to_datetime(highest) - pd.to_datetime(current_time)
        deltah = pd.Timedelta(deltah)
        deltal = pd.to_datetime(current_time) - pd.to_datetime(lowest)
        deltal = pd.Timedelta(deltal)

        if deltah.total_seconds() < 0 or deltal.total_seconds() <0:
            del_rows.append(j)
                        
    df_csv.drop(df_csv.index[del_rows], inplace=True)
    df_csv.to_csv(csv_path, index = False, header = True)
         


#print(df_csv)

         

