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
    print(f"Header: {csv_header}")
    #TOTAL VOTES
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
    #total votes
    total_votes = (len(votes))
    #print(total_votes)
    #for loop calucating number of votes per candidate
    for candidate in candidates:
        #khan
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = int(len(khan))
        #Correy
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = int(len(correy))
        #li
        elif candidate == "Li":
            li.append(candidates)
            li_votes = int(len(li))
        #O'tooley
        else:
            otooley.append(candidates)
            otooley_votes = int(len(otooley))
    
        #print(khan_votes)
        #print(correy_votes)
        #print(li_votes)
        #print(otooley_votes)
    #percentage of total votes
    P_of_votes_KHAN = str(round((khan_votes/total_votes)*100,2))
    #print("%" + (P_of_votes_KHAN))
    P_of_votes_Correy = str(round((correy_votes/total_votes)*100,2))
    #print("%" + (P_of_votes_Correy))
    P_of_votes_Li = str(round((li_votes/total_votes)*100,2))
    #print("%" + (P_of_votes_Li))
    P_of_votes_Otooley = str(round((otooley_votes/total_votes)*100,2))
    #print("%" + (P_of_votes_Otooley))

    #winner
    Winner=[khan_votes,correy_votes,li_votes,otooley_votes]
    if khan_votes > max(correy_votes,li_votes,otooley_votes):
        Winner = "Khan"
    elif correy_votes > max(khan_votes,li_votes,otooley_votes):
        Winner = "Correy"
    elif li_votes > max(khan_votes, correy_votes,otooley_votes):
        Winner = "Li"
    else: 
        Winner = "O'tooley"
#print(Winner)

#print final statements
print(f'Election Results' + '\n')
print(f'----------------------------'+'\n')
print('Total votes: ' + str(total_votes))
print(f'----------------------------'+'\n')
print(f"Khan: {P_of_votes_KHAN}% ({khan_votes})")
print(f"Correy: {P_of_votes_Correy}% ({correy_votes})")
print(f"Li: {P_of_votes_Li}% ({li_votes})")
print(f"Otooley: {P_of_votes_Otooley}% ({otooley_votes})")
print(f'----------------------------'+'\n')
print(f"Winner: {Winner}")
print(f'----------------------------'+'\n')

#creating output txt

g = open('Pypoll/Analysis/Pypoll_Result.txt', "a")
print((f'Election Results' + '\n'), file = g)
print((f'----------------------------'+'\n'), file = g)
print(('Total votes: ' + str(total_votes)), file = g)
print((f'----------------------------'+'\n'), file = g)
print((f"Khan: {P_of_votes_KHAN}% ({khan_votes})"), file = g)
print((f"Correy: {P_of_votes_Correy}% ({correy_votes})"), file = g)
print((f"Li: {P_of_votes_Li}% ({li_votes})"), file = g)
print((f"Otooley: {P_of_votes_Otooley}% ({otooley_votes})"), file = g)
print((f'----------------------------'+'\n'), file = g)
print((f"Winner: {Winner}"), file = g)
print((f'----------------------------'+'\n'), file = g)
g.close()