import csv 
import os 

# Open the file, read it, identify the header and define rows 
with open ("election_data.csv") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
    data = []
    for row in csvreader:
        data.append(row)

# Create a dictionary for the candidates
candidates = {}

# Define and set total votes value
total_votes = 0

# Loop through (run through) the candidates in the file. For all candidates who have votes 
for row in data:
    candidate = row[2]
    total_votes += 1
    if candidate in candidates:
        candidates[candidate] += 1
    else:
        candidates [candidate] = 1

# # Create a Dictionary for Percents
percents = {} 
for candidate, vote in candidates.items():
     percents[candidate] = int(round((candidate/total_votes*100,0)))

winning_candidate = 0 
winner =""
for candidate, votes in candidate.items():
    if votes > winning_candidate:
        winner = candidate 
        winning_votes = votes

# print_winner = f"The Winner is {winner}!"
# print_candidates = ""
# for candidates, votes in candidates.items():
#     print_candidates = print candidates + f"{candidate}: {votes} votes"




