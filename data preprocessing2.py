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

def time_val(date_val):
    string = ''
    for i in date_val:
        if i != ' ':
            string = string + i
        else:
            break
    return date_val.replace(string+ ' ', '')

folders = [name for name in os.listdir(".") if os.path.isdir(name) and name!= 'preprocessed_dir' and name!= 'NASDAQ data']
print(folders)

current_dir = os.getcwd()
ref_folder_name = 'DOW'
ref_folder = os.path.join(current_dir, ref_folder_name)

dir_list = []
years = [1,2]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
for year in years:
    for month in months:
        element = ref_folder_name + 'year' + str(year) + 'month' + str(month) + '.csv'
        dir_list.append(element)


hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
hours.reverse()

minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', 
'33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
minutes.reverse()

highest = '16:00:00'
lowest = '09:30:00'

all_time = []
for hour in hours:
    for minute in minutes:
        current_time = hour + ':' + minute + ':00'
        deltah = pd.to_datetime(highest) - pd.to_datetime(current_time)
        deltah = pd.Timedelta(deltah)
        deltal = pd.to_datetime(current_time) - pd.to_datetime(lowest)
        deltal = pd.Timedelta(deltal)

        if deltah.total_seconds() >= 0 and deltal.total_seconds() >=0:
            all_time.append(current_time)
all_time_initial = all_time

for i in range(len(dir_list)):
    csv_file = dir_list[i]
    csv_path = os.path.join(ref_folder, csv_file)
    print(csv_path)
    df_csv = pd.read_csv(csv_path, delimiter=',')
    all_time = all_time_initial
    working_days = []
    for k in range(len(df_csv)):
        working_day = getdate_val(df_csv['time'].iloc[k])
        if working_day not in working_days:
            working_days.append(working_day)
    print(len(working_days))
    all_time = all_time*len(working_days)
    print(len(all_time))
    all_lists = []
    df_csv_num = 0
    for j in range(len(all_time)):
        
        #print(len(all_time), df_csv_num, j, len(df_csv))

        if df_csv_num<len(df_csv):
            date = getdate_val(df_csv['time'].iloc[df_csv_num])
            temp_list = []
            if time_val(df_csv['time'].iloc[df_csv_num]) == all_time[j] : #and df_csv_num < len(df_csv)
                temp_list.append(date + ' ' + all_time[j])
                temp_list.append(df_csv['open'].iloc[df_csv_num])
                temp_list.append(df_csv['high'].iloc[df_csv_num])
                temp_list.append(df_csv['low'].iloc[df_csv_num])
                temp_list.append(df_csv['close'].iloc[df_csv_num])
                temp_list.append(df_csv['volume'].iloc[df_csv_num])
                #temp_list.append(df_csv.iloc[df_csv_num])
                df_csv_num = df_csv_num + 1

            else:
                temp_list.append(date + ' ' + all_time[j])
                temp_list.append(0)
                temp_list.append(0)
                temp_list.append(0)
                temp_list.append(0)
                temp_list.append(0)
            
            #temp_list.append(df_csv.iloc[df_csv_num])
        all_lists.append(temp_list)

    print(len(all_lists))
    df = pd.DataFrame(all_lists,columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    outputpath = os.path.join('D:\maot\Masters Thesis\codes - Student only\data', ref_folder_name, csv_file)
    df.to_csv(outputpath, index = False, header = True)
