import datetime
from collections import defaultdict

log = []
row = -1  # this will increase by 1 when a new row should be created. Never reset
firstMinCol = 2  # column with first minute

with open('input4.txt', 'r') as file:
    records = sorted(file.readlines())
    # Go through the records
    for i in range(len(records)):

        timestamp = records[i][1:17]
        date = timestamp[:10]
        hour = timestamp[11:13]
        minute = timestamp[14:16]
        message = records[i][18:]

        # Check if message represemts a new day. If so, then enter a new row and insert date and guard ID
        if '#' in message:
            # Reset sate change minutes for the day
            fallAsleepMin = None
            lastSleepMin = None
            # Add row in matrix and increase row count to update row for future messages
            log.append([0] * 62)
            row += 1
            # Add one day if guard starts just before midnight
            if hour == '00':
                log[row][0] = date
            elif hour == '23':
                log[row][0] = str(datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=1))[:10]
            # Add guard ID to row
            log[row][1] = message.split()[1]

        # Determine during which minutes the guard is awake or asleep. Awake is the first state and changes the minute alseep message occurrs
        elif 'asleep' in message:
            startSleepMin = int(minute)

        elif 'wake' in message:
            lastSleepMin = int(minute)

            for m in range(startSleepMin + firstMinCol, lastSleepMin + firstMinCol):
                log[row][m] = 1

    # print(log[0]) # 0:22 SLEEP 0:42 AWAKE 0:53 SLEEP 0:58 AWAKE

    # Add the total amount of slept minutes in logSum list

    logSum = defaultdict(lambda: 0)
    for row in range(len(log)):
        ID = log[row][1]
        logSum[ID] += int(sum(log[row][2:]))

    # print(logSum.keys())


# Function that gets the log for a certain ID from the soruceLog WITH ONLY MINUTES
def getIDlog(key, sourceLog):
    log = []
    logMinutes = []
    for row in sourceLog:
        if row[1] == key:
            log.append(row)
            logMinutes.append(row[2:])
    return logMinutes


# Finds the largest column and its index
def largestLogCol(log):
    maxSum = 0
    minute = 0
    for column in range(len(log[0])):
        s = 0
        for row in range(len(log)):
            s += log[row][column]
        if s > maxSum:
            maxSum = s
            minute = column
    return maxSum, minute


# Reserach each ID log
masterList = []
for ID in logSum.keys():
    IDlog = getIDlog(ID, log)
    masterList.append([ID, largestLogCol(IDlog)[0], largestLogCol(IDlog)[1]])

# print(masterList)

# PLOCKA UT DET ELEMENT MED STORST MITTENVARDE. MULTIPLICERA IHOP DE TVA ANDRA
maxSum = 0
for row in range(len(masterList)):
    minuteSum = masterList[row][1]
    if minuteSum > maxSum:
        maxSum = minuteSum
        maxRow = row

maxRowID = int(masterList[maxRow][0][1:])
maxRowMin = int(masterList[maxRow][2])

print('Guard ID: ' + str(maxRowID))
print('Minute: ' + str(maxRowMin))
print('ANSWER: ' + str(maxRowID * maxRowMin))
