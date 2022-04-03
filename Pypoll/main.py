#import modules
import os
import csv

#import path to csv and read
csvpath = os.path.join('Pypoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #working directory
    csv_header = next(csvreader)
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    #TOTAL VOTES
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
    #total votes
    total_votes = (len(votes))
    print(total_votes)
    #for loop calucating number of votes per candidate
    for candidate in candidates:
        #khan
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        #Correy
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        #li
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        #O'tooley
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)