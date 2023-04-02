# import libraries
import os
import csv
# path to the election data file
election_csv = os.path.join("election_data.csv")

# we are defining variables
total_votes = 0
candidate_votes = {}
candidate_percentages = {}

# read the csv file
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #skip header
    header = next(csv_reader)
    # loop through each row in the file
    for row in csv_reader:
        # increment the total vote count
        total_votes +=1
        # first check if the candidate is already in the dictionary, and if not, add the new one
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 0
        #increment the count of votes for candidates
        candidate_votes[row[2]] +=1
    # for each of the candidates, calculate the percentage of votes won
    for candidate, votes in candidate_votes.items():
        percentage = (votes/total_votes) * 100
        candidate_percentages[candidate] = round(percentage,2)
# determine the winner of the election
winner = max(candidate_votes, key=candidate_votes.get)

#print results
print("Election results")
print("---------------------")
print(f"Total votes: {total_votes}")
print("---------------------")

for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]}% ({votes})")
        
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')



