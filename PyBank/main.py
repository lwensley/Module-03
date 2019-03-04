# Import code
import os
import csv

# Define lists
dateslist          = []
netprofitlist      = []
changeinprofitlist = []

# Define path
PyBank_csv_path = os.path.join(".", "budget_data.csv")

# Define Functions

# Average Function
def avg(list):
    length = len(list)
    total = sum(list)
    return total / length

# Open and read csv
with open(PyBank_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read through rows
    for row in csvreader:
        
        # Add each date to 'dateslist' list
        dateslist.append(row[0])
        
        # Add each amount to 'netprofitlist' list
        netprofitlist.append(int(row[1]))

# Add changes in net profit/loss to 'changeinprofitlist' list

# Loop through one less time than the 'netprofitlist' list length
for i in range(len(netprofitlist)-1):
    
    # add change in profit to profit list
    changeinprofitlist.append(netprofitlist[i+1]-netprofitlist[i])

# Using the max and min values from the 'changeinprofitslist' list, 
# determine their index (ie location in the list), and define as variables
maxindex = int(changeinprofitlist.index(max(changeinprofitlist)))
minindex = int(changeinprofitlist.index(min(changeinprofitlist)))
    
# Pull min and max dates from the 'datelist' list using the minindex and maxindex variables
mindate = dateslist[minindex+1]
maxdate = dateslist[maxindex+1]


#Print results
print('Financial Analysis')
print("-" * 20)
print(f'Total Months: {len(dateslist)}')
print(f'Total Profit(loss): ${sum(netprofitlist)}')
print(f'Average Change: ${round(avg(changeinprofitlist),2)}')
print(f'Greatest Increase in Profits: {maxdate} (${max(changeinprofitlist)})')
print(f'Greatest Decrease in Profits: {mindate} (${min(changeinprofitlist)})')
 
# Write CSV
output_path = os.path.join(".", "PyBankResults.csv")
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write rows
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["-" * 20])
    csvwriter.writerow(['Total Months', len(dateslist)])
    csvwriter.writerow(['Total Profit(loss)', sum(netprofitlist)])                
    csvwriter.writerow(['Average Change', round(avg(changeinprofitlist),2)])
    csvwriter.writerow(['Greatest Increase in Profits', maxdate, max(changeinprofitlist)])
    csvwriter.writerow(['Greatest Decrease in Profits', mindate, min(changeinprofitlist)])

print("-" * 20)
print(f'CSV file saved here {output_path}')