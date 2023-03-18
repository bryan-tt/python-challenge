import csv
#Ballot ID,County,Candidate

# specify where to find csv file
csvfilepath = "Resources/election_data.csv"

# create variables
total_votes = 0
candidate_votes = {}
output = []
highest_vote = 0
winner = ""

# Read csv file in
with open(csvfilepath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Store header row
    csvheader = next(csvreader)

    # For loop to go through data
    for row in csvreader:
        # Count total votes
        total_votes += 1
        # Add vote count to dictionary of candidates
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
        else:
            candidate_votes[row[2]] = 1


# Add output to list
output.append(f"Election Results\n-------------------------")
output.append(f"Total Votes: {total_votes}\n-------------------------")
# Use for loop on dictionary to get candidate votes, and calculate vote percentage
for key, value in candidate_votes.items():
    output.append(f"{key}: {round((value / total_votes)*100,3)}% ({value})")
    # determine winner
    if (value > highest_vote):
        highest_vote = value
        winner = key
output.append(f"-------------------------")
output.append(f"Winner: {winner}")
output.append(f"-------------------------")

# Print to terminal
for i in output:
    print(i)

# Specify where output text file will go, and write output lines into text file
outputpath = "analysis/analysis.text"
with open(outputpath, 'w') as f:
    f.write("\n".join(output))