# Import code
import os
import csv

# Define lists
candidatelist     = []
voterpercentlist  = []
votercountlist    = []

# Define path
PyPoll_csv_path = os.path.join(".", "election_data.csv")

# Define Functions
# Define percent calculation
def percent(votes):
    totalvotes = sum(votercountlist)
    return format(votes / totalvotes * 100, '.3f')
    
# Open and read csv
with open(PyPoll_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read through rows
    for row in csvreader:
        
        # Add each unique candidate to 'candidatelist' list, and create index on votercountlist
        if row[2] not in candidatelist:
            candidatelist.append(row[2])
            votercountlist.append(int(0))
            voterpercentlist.append(float(0))
        
        # Add each vote to respective votecount in 'votecountlist' list
        if row[2] in candidatelist:
            i = candidatelist.index(row[2])
            votercountlist[i] = votercountlist[i] +1

# calculate percent votes and add to 'voterpercentlist' list
for x in range(len(voterpercentlist)):
    voterpercentlist[x] = percent(votercountlist[x])

# calculate index of winner based on max value in 'voterpercentlist' list
winnerindex = int(voterpercentlist.index(max(voterpercentlist)))
    
# print results
print('Election Results')
print("-" * 20)
print(f"Total Votes: {sum(votercountlist)}")
print("-" * 20)

for y in range(len(candidatelist)):
    print(f'{candidatelist[y]}: {voterpercentlist[y]}% ({votercountlist[y]})')

print("-" * 20)
print(f"Winner: {candidatelist[winnerindex]}")

# Write CSV
output_path = os.path.join(".", "PyPollResults.csv")
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write rows
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(["-" * 20])
    csvwriter.writerow(['Total Votes',sum(votercountlist)])
    csvwriter.writerow(["-" * 20])
    for y in range(len(candidatelist)):
        csvwriter.writerow([candidatelist[y], str(voterpercentlist[y]) + "%", "(" + str(votercountlist[y]) + ")"])           
    csvwriter.writerow(["-" * 20])
    csvwriter.writerow(['Winner', candidatelist[winnerindex]])

# Print output location
print("-" * 20)
print(f'CSV file saved here {output_path}')