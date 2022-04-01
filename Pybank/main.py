#import modules
import os
import csv 

#import path to CSV and READ
csvpath=os.path.join('Pybank', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #working directory
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_chnage = []   
    print(f"Header: {csv_header}") 

   



