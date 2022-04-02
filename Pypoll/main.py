#import modules
import os
import csv

#import path to csv and read
csvpath = os.path.join('Pypoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)
    #working directory
