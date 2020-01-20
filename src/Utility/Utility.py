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
