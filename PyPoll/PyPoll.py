# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# Write to screen and file

import os
import csv
import pprint

#set file path and open CSV file
filepath = os.path.join("..","Resources","Pypoll_Data.csv")
csvfile = open(filepath, "r")
ImportedCSVData = csv.reader(csvfile)

#skip header
csv_header = next(ImportedCSVData)

# define variables
UniqueCandidates = []
VoteCount = 0
VotesList = []
CandidateResults = {}

#read file 
for rows in ImportedCSVData:
    # Count the votes
    VoteCount = VoteCount + 1
    # List the unique candidates 
    if rows[2] not in UniqueCandidates:
        UniqueCandidates.append(rows[2])
    VotesList.append(rows[2])

# Calculate candidate results and place into dictionary
CandidateResults = {}
CandidateResults = dict((candidates,VotesList.count(candidates)) for candidates in set(VotesList))

# Duplicate CandidateResults dictionary, replace values with percentage figures 
CandidatePercentages = dict((k, v / VoteCount) for k, v in CandidateResults.items())

# Close CSV file
csvfile.close()

# Sort dictionaries into decending order
SortedCandidates = dict(sorted(CandidateResults.items(), key=lambda x: x[1], reverse=True))
SortedCandidatePercentages = dict(sorted(CandidatePercentages.items(), key=lambda x: x[1], reverse=True))

# # print analysis
print(f"  ")
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {VoteCount}")
print(f"-------------------------")
for candidates in SortedCandidates:
    print(str(candidates) + ": " "{:.1%}".format(float(SortedCandidatePercentages[candidates])) + " (" + str(SortedCandidates[candidates]) + ")")
print(f"-------------------------")
for winner in SortedCandidates:
    print(f"Winner is: {winner}")
    break
print(f"-------------------------")

# Print Analysis to File
# Delete previous analysis 
filepath = os.path.join("..","Analysis","PyPoll_Analysis.txt")
if os.path.exists(filepath):
    os.remove(filepath)
# Create File and write Analysis
with open(filepath,"w") as writefile:
    print(f"  ", file=writefile)
    print(f"Election Results", file=writefile)
    print(f"-------------------------", file=writefile)
    print(f"Total Votes: {VoteCount}", file=writefile)
    print(f"-------------------------", file=writefile)
    for candidates in SortedCandidates:
        print(str(candidates) + ": " "{:.1%}".format(float(SortedCandidatePercentages[candidates])) + " (" + str(SortedCandidates[candidates]) + ")", file=writefile)
    print(f"-------------------------", file=writefile)
    for winner in SortedCandidates:
        print(f"Winner is: {winner}", file=writefile)
        break
    print(f"-------------------------", file=writefile)



