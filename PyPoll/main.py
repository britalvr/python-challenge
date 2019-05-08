# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

voter_id = []
county = []
candidate_votes = []

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:


   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')


   # Read the header row first (skip this step if there is now header)
   csv_header = next(csvreader)


   # Read each row of data after the header
   for row in csvreader:

        voter_id.append(row[0])
        county.append(row[1])
        candidate_votes.append(row[2])

total_votes = int(len(candidate_votes))
khan_votes = (candidate_votes.count("Khan"))
correy_votes = (candidate_votes.count("Correy"))
li_votes = (candidate_votes.count("Li"))
otooley_votes = (candidate_votes.count("O'Tooley"))
total_votes
with open("test.txt", "w+") as file:
        file.write("Test")
        file.write("Election Results")
        file.write("----------------------------")
        file.write("Total votes: " + str(len(voter_id)))
        file.write("----------------------------")
        file.write("Khan: " + str(int((khan_votes/total_votes)*100)) + "% (" + str(khan_votes) + ")")
        file.write("Correy: " + str(int((correy_votes/total_votes)*100)) + "% (" + str(correy_votes) + ")")
        file.write("Li: " + str(int((li_votes/total_votes)*100)) + "% (" + str(li_votes) + ")")
        file.write("O'Tooley: " + str(int((otooley_votes/total_votes)*100)) + "% (" + str(otooley_votes) + ")")
        file.write("----------------------------")
        file.write("Winner:" + "Khan" )
        file.write("-----------------------------")

