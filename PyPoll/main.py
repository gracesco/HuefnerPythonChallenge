import csv 
import os 

# Create a function that will open the file, read it, identify the header and define rows. 
def read_election_data(path):
    with open ("election_data.csv") as csv_file:
        csvreader = csv.reader(csv_file, delimiter=",")
        header = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
    return data

# Create a function to count the votes for candidates
def candidate_votes(data):
    # Create a dictionary for the candidates 
    candidates = {}
    # Define and set total votes value
    total_votes = 0 
    # Loop through the candidates in the file to determine the amount of each candidate has.
    for row in data:
        candidate = row[2]
        total_votes += 1
        # If the candidate has multiple votes then count those up, otherwise candidate only has one vote
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates [candidate] = 1
    return [candidates, total_votes]

# Create a function to determine the results and declare a winner
def final_results(candidates,total_votes):
    winning_votes = 0 
    # Define how the winner will be displayed in the terminal: as a sentence
    winner =""
    # Loop through the candidates to determine a winner 
    for candidate, votes in candidates.items():
        # If the votes are calculated as the most, that candidate is the winner
        if votes > winning_votes:
            winner = candidate 
            winning_votes = votes
    # Print the below sentence for the winner        
    announce_winner = f"The winner is {winner} with {winning_votes} votes!"
    # Define how candidates will be displayed in terminal: as a list with votes and percent
    candidate_result = ""
    for candidate, votes in candidates.items():
        candidate_result = candidate_result + f"{candidate}: {votes} votes ({int(round((votes/total_votes)*100,2))}%)\n"
    # Print the results with Election, Total Votes, Winner, and status of other candidates
    results = f"\nElection results:\nTotal Votes: {total_votes}\n{announce_winner}\n{candidate_result}"
    return results    

# Create a function to do collectively run the functions above and print results
def run_script(path):
    election_data = read_election_data(path)
    candidates, total_votes = candidate_votes(election_data)
    results = final_results(candidates,total_votes)
    print(results)
    save_final = input("Do you want to save the final results? (y/n)\n ")
    if save_final =="y":
        with open ("output_file.txt","w") as doc:
            doc.write(results)

run_script("election_data.csv")




