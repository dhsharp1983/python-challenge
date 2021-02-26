#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

#set file path and open CSV file
filepath = os.path.join("..","Resources","PyBank_Data.csv")
csvfile = open(filepath, "r")
ImportedCSVData = csv.reader(csvfile)

#skip header
csv_header = next(ImportedCSVData)

#define some empty variables
MonthCount = 0
TotalProfit = 0
ProfitList = []
MonthList = []
MaxProfitMonth = ""
MinProfitMonth = ""

ProfitDeltaList = []

#start loop, add month counter, add total profit
#Create ProfitList and MonthList for analysis calculation 
for rows in ImportedCSVData:
    MonthCount = MonthCount + 1
    TotalProfit = TotalProfit + int(rows[1])
    ProfitList.append(int(rows[1]))
    MonthList.append(rows[0])

# calculate ProfitDelta
FirstRun = True
for entry in range(len(ProfitList)):
    if FirstRun == False:
        ProfitDeltaList.append(ProfitList[entry] - ProfitList[entry - 1])
    FirstRun = False
ProfitDelta = sum(ProfitDeltaList) / len(ProfitDeltaList)
print(ProfitDelta)

#Calculate Average Change
AverageChange = TotalProfit / MonthCount

#Calculate Min/Max Profits
MaxProfit = max(ProfitList)
MinProfit = min(ProfitList)

#Format Currency output
FormattedTotalProfit = '{:,.2f}'.format(TotalProfit)
FormattedAverageChange = '{:,.2f}'.format(AverageChange)
FormattedMaxProfit = '{:,.2f}'.format(MaxProfit)
FormattedMinProfit = '{:,.2f}'.format(MinProfit)
FormattedProfitDelta = '{:,.2f}'.format(ProfitDelta)

#Find relative Min and Max Months
MinProfitMonthIndex = ProfitList.index(MinProfit)
MinProfitMonth = MonthList[MinProfitMonthIndex]
MaxProfitMonthIndex = ProfitList.index(MaxProfit)
MaxProfitMonth = MonthList[MaxProfitMonthIndex]

# Print Analysis to Screen
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {MonthCount}")
print(f"Total: ${FormattedTotalProfit}")
print(f"Average  Change: ${FormattedProfitDelta}")
print(f"Greatest Increase in Profits: ${FormattedMaxProfit} in {MaxProfitMonth}")
print(f"Greatest Decrease in Profits: ${FormattedMinProfit} in {MinProfitMonth}")

# Print Analysis to File
# Delete previous analysis 
filepath = os.path.join("..","Analysis","PyBank_Analysis.txt")
if os.path.exists(filepath):
    os.remove(filepath)
# Create File and write Analysis
with open(filepath,"w") as writefile:
    print("Financial Analysis", file=writefile)
    print("----------------------------", file=writefile)
    print(f"Total Months: {MonthCount}", file=writefile)
    print(f"Total: ${FormattedTotalProfit}", file=writefile)
    print(f"Average  Change: ${FormattedProfitDelta}", file=writefile)
    print(f"Greatest Increase in Profits: ${FormattedMaxProfit} in {MaxProfitMonth}", file=writefile)
    print(f"Greatest Decrease in Profits: ${FormattedMinProfit} in {MinProfitMonth}", file=writefile)

#Close CSV file
csvfile.close()
