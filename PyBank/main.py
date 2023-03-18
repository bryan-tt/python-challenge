import csv

# File path for the csv file
csvpath = "Resources/budget_data.csv"

# Variables to store data
total_months = 0
net_total = 0
profit_loss = []
date = []
pl_diff = []
output = []


# read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store the header row
    csvheader = next(csvreader)

    for row in csvreader:
        # Count total months included in dataset
        total_months += 1
        # Net total amount of Profit/Losses over the period
        net_total += int(row[1])
        # Add all dates into list
        date.append(row[0])
        # Add all profit and losses into a list
        profit_loss.append(int(row[1]))

# Create list with changes in PL
for i in range(len(profit_loss)-1):
    pl_diff.append(profit_loss[i+1] - profit_loss[i])

# Find average of change in PL
avg = round((float(sum(pl_diff))/len(pl_diff)),2)

# Find greatest increase in PL and date
greatest_increase = max(pl_diff)
greatest_increase_date = date[pl_diff.index(greatest_increase)+1]

# Find the greatest decrease in PL, and date
greatest_decrease = min(pl_diff)
greatest_decrease_date = date[pl_diff.index(greatest_decrease)+1]

# Add analysis output to list
output.append(f"Financial Analysis\n----------------------------")
output.append(f"Total Months: {total_months}")
output.append(f"Total: ${net_total}")
output.append(f"Average change: ${avg}")
output.append(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
output.append(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# print analysis to terminal
for i in output:
    print(i)

# write analysis to text file
output_path = "analysis/analysis.txt"
with open(output_path, 'w') as f:
    f.write('\n'.join(output))