import random
import string
import re
from datetime import date, timedelta
import calendar

class Utility:
    @staticmethod
    def convertFieldValueToLowerCase(dict, key):
        modifiedField = dict[key].lower()
        dict[key] = modifiedField
        return dict

    @staticmethod
    def appendNewFieldToDict(dict, key, value):
        dict[key] = value
        return dict

    @staticmethod
    def checkExemptPaths(pathAsString, pathsToExemptList):
        pathToCheck = pathAsString
        if pathAsString.endswith('/') == True: 
            pathToCheck = pathAsString[:-1] # Remove the trailing backslash
        
        # Convert the string to an array and check if the last item is in the exempt list
        if pathToCheck.split('/')[-1] in pathsToExemptList:
            return True
        else:
            return False
    
    @staticmethod
    def randomString(stringLength):
        """Generate a random string with the combination of lowercase and uppercase letters """

        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

    @staticmethod
    def computeNextCycleDate(cycleDuration, startDate):
        # \\d+(d|w|m) => 1d, 1w, 2m
        data = re.search(r"^\d+",cycleDuration).group()
        data = int(data)
        span = cycleDuration[-1]
        startDateList = [int(x) for x in startDate.split('-')]
        startDate = date(startDateList[0], startDateList[1], startDateList[2])
                
        if span == 'd':
            extraDays = data
        elif span == 'w':
            extraDays = 7 * data
        elif span == 'm':
            extraDays = calendar.monthrange(startDate.year, startDate.month)[1]
        return startDate + timedelta(days=extraDays)