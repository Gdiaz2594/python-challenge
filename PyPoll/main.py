
import csv
import os

election_csv = os.path.join("Resources", "election_data.csv")

#Store the content
voter = []
country = []
candidate = []

candidates = []
candidateVotes = []
candidatePercent = []
dataCandidate = ""

#Iterate through the csv file
with open(election_csv, "r", encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        voter.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

    #The total number of votes cast is the lenght of voter list
    votes_cast = len(voter)

    # A complete list of candidates who received votes
    for person in candidate:
        if person not in candidates:
            candidates.append(person)
    #The total number of votes each candidate won and the percentage of votes each candidate won
    for name in candidates:
        totalVotants = 0
        for vote in candidate:
            if name == vote:
                totalVotants += 1
        candidateVotes.append(totalVotants)
        candidatePercent.append(f"{(totalVotants*100)/votes_cast:.3f} %")

    #Write the data for each candidate
    votes = 0
    for i in range(len(candidates)):
        dataCandidate += f"{candidates[i]}: {candidatePercent[i]} ({candidateVotes[i]}) \n"
        #The winner of the election based on popular vote
        if candidateVotes[i] > votes:
            votes = candidateVotes[i]
            winner = candidates[i]

#Analysis results
analysis = f"""
Election Results
------------------------------------
Total votes: {votes_cast}
------------------------------------
{dataCandidate}------------------------------------
Winner: {winner}
------------------------------------
"""
print(analysis)

#Creation of txt file with the analysis results
output_file = os.path.join("analysis", "analysis_file.txt")

with open(output_file, "w") as textfile:
    textfile.write(analysis)
