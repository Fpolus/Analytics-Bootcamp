# Dependencies
import csv

# Variables
vote_count = 0
candidate_votes = {}

# Read in the CSV file
with open('election_data.csv') as vote_data:
    csvreader = csv.reader(vote_data, delimiter=',')
    csv_header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        vote_count = vote_count + 1
        candidate = row[2]

        # Calculating the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# Calculating the winner
max_votes = 0
winner = None

# Loop through the data
for candidate, vote in candidate_votes.items():
    if vote > max_votes:
        max_votes = vote
        winner = candidate

# Printing the results
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_count))
print("-------------------------")

# Loop through the data
for candidate, votes in candidate_votes.items():
    percent_vote = (votes / vote_count) * 100
    print(candidate + ": " + "{:.3f}%".format(percent_vote) + " (" + str(votes) + ")")

# Printing the results  
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Exporting the results to a text file
with open('Analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(vote_count) + "\n")
    text.write("---------------------------------------\n")
    
    # Loop through the data
    for candidate, votes in candidate_votes.items():
        percent_vote = (votes / vote_count) * 100
        text.write(candidate + ": " + "{:.3f}%".format(percent_vote) + " (" + str(votes) + ")\n")
        
    # Printing the results
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")


