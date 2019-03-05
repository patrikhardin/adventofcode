# There are different guards guarding at different times
# They can alter between two states

# Create a matrix where each row represents each date. Ceate one row then append with every new day
# first column (0) is the date
# second column (1) is the guard ID
# column (2) - (61) is binary. 1 if asleep 0 if awake

# pattern in data:
#   each day starts with Guard X begins shift. If the hour is 23 the day is next day. If hour is 00 then it is thw actual day. Store info in col 0 and 1
#   read each statement until first word is guard. Then alter between states 1 and 0 until 'Guard'
#   repeat
#   find row with highest sum of 1
#   multiply ID with sun.

import datetime
from collections import defaultdict

log = []
row = -1 #this will increase by 1 when a new row should be created. Never reset
firstMinCol = 2 #column with first minute

with open('input4.txt','r') as file:
    records = sorted(file.readlines())
    #Go through the records
    for i in range(len(records)):

        timestamp = records[i][1:17]
        date = timestamp[:10]
        hour = timestamp[11:13]
        minute = timestamp[14:16]
        message = records[i][18:]

        #Check if message represemts a new day. If so, then enter a new row and insert date and guard ID
        if '#' in message:
            #Reset sate change minutes for the day
            fallAsleepMin = None
            lastSleepMin = None
            # Add row in matrix and increase row count to update row for future messages
            log.append([0]*62)
            row += 1
            #Add one day if guard starts just before midnight
            if hour == '00':
                log[row][0] = date
            elif hour == '23':
                log[row][0] = str(datetime.datetime.strptime(date,'%Y-%m-%d') + datetime.timedelta(days=1))[:10]
            #Add guard ID to row
            log[row][1] = message.split()[1]

        #Determine during which minutes the guard is awake or asleep. Awake is the first state and changes the minute alseep message occurrs
        elif 'asleep' in message:
            startSleepMin = int(minute)

        elif 'wake' in message:
            lastSleepMin = int(minute)

            for m in range(startSleepMin + firstMinCol,lastSleepMin + firstMinCol):
                log[row][m] = 1

#print(log[0]) # 0:22 SLEEP 0:42 AWAKE 0:53 SLEEP 0:58 AWAKE

    #Add the total amount of slept minutes in logSum list

    logSum = defaultdict(lambda: 0)
    for row in range(len(log)):
        ID = log[row][1]
        logSum[ID] += int(sum(log[row][2:]))

    maxID = max(logSum, key=logSum.get)
    maxIDint = int(max(logSum, key=logSum.get)[1:])

#Filter rows in log where ID = maxID. Find max column and sum it up

maxLog = []
maxLogMinutes = []
for row in log:
    if row[1] == maxID:
        maxLog.append(row)
        maxLogMinutes.append(row[2:])

#Find largest col in maxLogMinutes

maxSum = 0
min = 0
for column in range(len(maxLogMinutes[0])):
    s = 0
    for row in range(len(maxLogMinutes)):
        s += maxLogMinutes[row][column]
    if s > maxSum:
        maxSum = s
        min = column

print('Guard ID: ' + maxID)
print('Minute: ' + str(min))
print('ANSWER: ' + str(maxIDint * int(min)))
