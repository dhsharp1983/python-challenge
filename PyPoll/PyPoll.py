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
print(CandidateResults)

# Duplicate Results dictionary and use for percentage calculations
# CandidatePercentages = {}
# CandidatePercentages = CandidateResults.copy()
# print(CandidatePercentages)
# for k,v in CandidatePercentages.items():
#     print(v)
#     CandidatePercentages[v] = 'bob'
#     print(CandidatePercentages[v])

CandidatePercentages = dict((k, v / VoteCount) for k, v in CandidateResults.items())
print(CandidatePercentages)



# # Duplicate CandidateResults dictionary, and use for percentage calculations
# CandidatePercentages = CandidateResults
# for k,v in CandidatePercentages.items():
#     v = v / VoteCount

# print(CandidatePercentages["Khan"])


# # Extract Candidate names from first dictionary, create second with percentages 
# CandidatePercentages = {}
# for key,value in CandidateResults.items():
#     print(key)
#     print(value)
#     CandidatePercentages = dict([
#         (value, "bob")
# #        (key, "{:.1%}".format(value / VoteCount))
#     ])

#print(CandidateResults)
# for key,value in CandidatePercentages.items():
#     print(key)
#     print(value)

csvfile.close()
SortedCandidates = dict(sorted(CandidateResults.items(), key=lambda x: x[1], reverse=True))
SortedCandidatePercentages = dict(sorted(CandidatePercentages.items(), key=lambda x: x[1], reverse=True))
print(SortedCandidates)
print(SortedCandidatePercentages)


# # print analysis
print(f"  ")
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {VoteCount}")
print(f"-------------------------")
for candidates in SortedCandidates:
    # print(f"{candidates}: {SortedCandidates[candidates]} ({SortedCandidatePercentages[candidates]})")
    print(str(candidates) + ": " "{:.1%}".format(float(SortedCandidatePercentages[candidates])) + " (" + str(SortedCandidates[candidates]) + ")")
print(f"-------------------------")
for winner in SortedCandidates:
    print(f"Winner is: {winner}")
    break
print(f"-------------------------")
# print(f"Khan: 63.000% (2218231)")
# print(f"Correy: 20.000% (704200)")
# print(f"Li: 14.000% (492940)")
# print(f"O'Tooley: 3.000% (105630)")
# print(f"-------------------------")
# print(f"Winner: Khan")
# print(f"-------------------------")


    

# for key, value in CandidateResults.items():
#     print(f"{key} received {value} votes")



