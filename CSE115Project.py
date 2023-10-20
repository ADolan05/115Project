
data = [ {'Title': 'SOLE PARK', 'Category': 'SCULPTURE', 'Type': 'RELIEF',
'Medium': 'STONE', 'Frame': 'false', 'Photo URL Link': 'UNKNOWN', 'Artist':
'UNKNOWN', 'Street Address': 'BUSTI AVE & NIAGARA ST', 'City': 'BUFFALO',
'Zipcode': '14213', 'State': 'NY'},
{'Title': 'BUFFALO STREET MAP', 'Category': 'GRAPHIC ARTS', 'Type': 'MAP',
'Medium': 'PARCHMENT', 'Frame': 'true', 'Photo URL Link': 'UNKNOWN',
'Artist': 'SMITH BROTHERS COMPANY', 'Street Address': '65 NIAGARA SQUARE',
'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'WAR MEMORIAL STADIUM RENDERING', 'Category': 'GRAPHIC ARTS',
'Type': 'DRAWING', 'Medium': 'PAPER', 'Frame': 'false', 'Photo URL Link':
'UNKNOWN', 'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE',
'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'MAYOR HIRAM BARTON', 'Category': 'PAINTINGS', 'Type': 'PORTRAIT',
'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/HIRAM%20BARTON.HTML', 'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARASQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'MAYOR ELI COOK', 'Category': 'GRAPHIC ARTS', 'Type': 'PORTRAIT',
'Medium': 'PASTEL ON PAPER', 'Frame': 'true', 'Photo URL Link':
'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/ELI%20COOK.HTML', 'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE',
'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'MAYOR ANTHONY MASIELLO', 'Category': 'PAINTINGS', 'Type':
'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
'UNKNOWN', 'Artist': 'NATHAN NAETZKER', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
{'Title': 'MAYOR CHANDLER J WELLS', 'Category': 'PAINTINGS', 'Type':
'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/CHANDLER%20WELLS.HTML', 'Artist': 'ALVAH BRADISH', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'} ]



#define getValuesForKey
#Input: key, a string that is a key for records, and records is list of dictionaries
#returns: a list of values in records that have the key that is the same as the parameter key
#getValuesForKey("Artist", data) should return a list of all artist in data
def getValuesForKey(key,records):
    out = []
    for myDict in records:
        #loop through the list of dictionaries
        for k in myDict.keys():
            #loop through keys in dictionary
            if k == key:
                out.append(myDict[k])
    return out

#define countMatchesByKey
#Input: 3 parameters, key: a string, value: a value, and records: a list of dictionaries
#Retruns: the number of records whose key pair matches the parameters key and pair
# countMatchesByKey("Artist","UNKNOWN",data) should return 4
def countMatchesByKey(key, value, records):
    match = 0
    for myDict in records:
        for k in myDict.keys():
            if k == key and myDict[k] == value:
                match = match + 1
    return match

#define countMatchesByKeys
#Input: 5 parameters: key1, value1, key2, value2, records (Same concept as countMatchesByKey)
#Returns: number of records who have key pairs that match for key1:value1 and key2:Value2
def countMatchesByKeys(key1, value1, key2, value2, records):
    match = 0
    for myDict in records:
        pair1 = 0
        pair2 = 0
        for k in myDict.keys():
            if k == key1 and myDict[k]== value1: 
                pair1 = 1
        for i in myDict.keys():
            if i == key2 and myDict[i]== value2:
                pair2 = 1
        if pair1 == 1 and pair2 == 1:
            match = match + 1
    return match
#define filterByKey
#Input: 3 parameters: key, value, records
#returns: a list of dictionaries where each of the dictionaries have the key pair
#that matches key and value
def filterByKey(key, value, records):
    myList = []
    for myDict in records:
        for k in myDict.keys():
            if  k == key and myDict[k] == value:
                myList.append(myDict)
    return myList
#define computeFrequency
#Input: 2 paramaters: key, records
#returns: a dictionary where each pair is the value associated with key: the #
#of times the value is in records
def computeFrequency(key, records):
    newDict = {}
    for myDict in records:
        if key in myDict.keys():
            value = myDict[key]
            newDict[value] = countMatchesByKey(key,value,records)
    return newDict
