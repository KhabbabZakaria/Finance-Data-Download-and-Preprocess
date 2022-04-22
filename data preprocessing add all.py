import pandas as pd
import csv
import requests
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

folders = [name for name in os.listdir(".") if os.path.isdir(name) and name!= 'preprocessed_dir']
print(folders)

current_dir = os.getcwd()
preprocessed_dir = os.path.join(current_dir, 'preprocessed_dir')
if not os.path.exists(preprocessed_dir):
    os.mkdir(preprocessed_dir)


ref_folder_name = 'DOW'
ref_folder = os.path.join(current_dir, ref_folder_name)

dir_list = []
years = [1]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
for year in years:
    for month in months:
        element = ref_folder_name + 'year' + str(year) + 'month' + str(month) + '.csv'
        dir_list.append(element)

csv_path = os.path.join(ref_folder, dir_list[0])
df_csv = pd.read_csv(csv_path, delimiter=',')

for i in range(1, len(dir_list)):
    csv_path = os.path.join(ref_folder, dir_list[i])
    #print(csv_path)
    df_csv2 = pd.read_csv(csv_path, delimiter=',')
    #print(df_csv2)
    df_csv = pd.concat([df_csv, df_csv2],ignore_index=True)

output_file = ref_folder_name + '.csv'
output_dir = os.path.join(preprocessed_dir, output_file)
df_csv.to_csv(output_dir, index = False, header = True)