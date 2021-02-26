# Convert From:
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado

# Convert To:
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,MM/DD/YYYY,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO

# import modules
import os
import csv

# define function to re-order birthdate
def ReOrderDate(InputDate):
    SplitDateList = InputDate.split("-")
    SplitDateList.append("/")
    DateOrder = [1,3,2,3,0]
    ReOrderedDateList = [SplitDateList[i] for i in DateOrder]
    ReOrderedDateString = ''.join([str(elem) for elem in ReOrderedDateList])
    return ReOrderedDateString

# define function to hash out the SSN
def HashOutSSN(InputSSN):
    SplitSSN = InputSSN.split("-")
    SplitSSN.append("***")
    SplitSSN.append("**")
    SplitSSN.append('-')
    SSNOrder = [3,5,4,5,2]
    ReOrderedSSNList = [SplitSSN[i] for i in SSNOrder]
    ReOrderedSSNString = ''.join([str(elem) for elem in ReOrderedSSNList])
    return ReOrderedSSNString

# define function to abbreviate state 
def AbbreviateState(LongStateString):
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
    ShortStateString = us_state_abbrev.get(LongStateString)
    return ShortStateString


#set file path and open source CSV file
filepath = os.path.join("..","Resources","PyBoss_Data.csv")
csvfile = open(filepath, "r")
ImportedCSVData = csv.reader(csvfile)


#Open WriteFile
writefilepath = os.path.join("..","Analysis","PyBoss_ReOrdered_Data.csv")
if os.path.exists(writefilepath):
    os.remove(writefilepath)
writefile = open(writefilepath, "a")

# Edit header 
for firstrow in ImportedCSVData:
    firstrow = 'Emp ID,First Name,Last Name,DOB,SSN,State'
    #print(firstrow, file=writefile)
    break

# perform data conversion task
for rows in ImportedCSVData:
    # insert extra column for firstname/lastname
    rows.insert(2, rows[1])
    # split names into list 
    FirstName = (rows[1].split())[0]
    LastName = (rows[1].split())[1]
    # apply firstname and lastname 
    rows[1] = FirstName
    rows[2] = LastName
    # call functions to edit data 
    rows[3] = ReOrderDate(rows[3])
    rows[4] = HashOutSSN(rows[4])
    rows[5] = AbbreviateState(rows[5])
    # print new csv file 
    with open(writefilepath,"a") as writefile:
        print(rows[0] + ",", rows[1] + ",", rows[2] + ",", rows[3] + ",", rows[4] + ",", rows[5]  , file=writefile)

# print to screen
print(f"Updated data has been saved to {writefilepath}")

#Close CSV files
csvfile.close()
writefile.close()