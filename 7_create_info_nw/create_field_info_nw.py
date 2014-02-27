
from operator import itemgetter
import codecs

inDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"
outDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

def getAuthFieldDict():
	authFieldDict  = dict()
	

	fileR = codecs.open(inDir + "mapAuthField.csv", "r", "UTF-8")

	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		name = tokens[0]
		field = tokens[1]
		authFieldDict[name] = field

	print "len authFieldDict>>" + str(len(authFieldDict))
	return authFieldDict

def getIdAuthDict():
	
	idAuthDict = dict()

	fileR = open(inDir + "authIdMapAsm.csv")
	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		
		name = tokens[1]
		_id = tokens[0]

		idAuthDict[_id] = name
	
	print "len idAuthDuct>> " + str(len(idAuthDict))
	return idAuthDict

def getFieldFieldMap(fileName, authFieldDict, idAuthDict):
	
	fileR = open(fileName)
	fieldFieldDict = dict()
	
	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split(";")
		user1 = idAuthDict[tokens[0]]
		user2 = idAuthDict[tokens[1]]
		if user1 in authFieldDict and user2 in authFieldDict:
			
			field1 = authFieldDict[user1]
			field2 = authFieldDict[user2]
			
			if field2 not in fieldFieldDict:
				fieldFieldDict[field2] = dict()
				fieldFieldDict[field2][field1] = 1

			else:
				if field1 not in fieldFieldDict[field2]:
					fieldFieldDict[field2][field1] = 1
				else:
					fieldFieldDict[field2][field1] = fieldFieldDict[field2][field1] + 1
			
	
	return fieldFieldDict

def saveFieldFieldDict(fieldFieldDict, fileName):
	

	topFieldItemDict = dict()

	#find the field in each field
	for field in fieldFieldDict:

		if field not in fieldFieldDict:
			continue

		fieldCount = fieldFieldDict[field]

		fieldList = list()

		for field1 in fieldCount:
			if field == field1:
				continue

			fieldList.append((field1, fieldCount[field1]))

		#sort this list
		fieldList = sorted(fieldList, key=itemgetter(1))
	
		topItemList = list()

		for i in range(1, 6):
			topItemList.append(fieldList[-1 * i])

		topFieldItemDict[field] = topItemList

	arcs = 0

	for field in topFieldItemDict:
		arcs = arcs + len(topFieldItemDict[field]) 

	print "arcs>>" + str(arcs)

	fileW  = open(fileName, "w")

	fields = topFieldItemDict.keys()

	fileW.write("*Vertices "+ str(len(fields)) + "\n")

	fieldIdMap = dict()
	count = 1

	for field in fields:
		fieldIdMap[field] = count
		totalCount = 0
		for item in topFieldItemDict[field]:
			totalCount = totalCount + item[1]

		fileW.write(str(count)+ " " +'\"'+field +"\"" + " "+ str(totalCount) +  "\n")
		count = count + 1

	fileW.write("*Arcs "+ str(arcs) + "\n")

	for field in topFieldItemDict:
		
		listItems = topFieldItemDict[field]
		for item in listItems:
			line = str(fieldIdMap[field]) + " " + str(fieldIdMap[item[0]]) + " " + str(item[1])			
			fileW.write(line + "\n")

def main():

	fileNameList = ["filt_user1_mentions_user2.csv", "filt_user1_follows_user2.csv", "filt_user1_retweets_user2.csv"]

	outFilenameList = list()

	for fileName in fileNameList:
		
		filename = fileName[11:fileName.find("_user2")]		
		print "fileName>>" + filename
		fieldFieldDict =  getFieldFieldMap(inDir + fileName, getAuthFieldDict(), getIdAuthDict())
		saveFieldFieldDict(fieldFieldDict, outDir + filename + ".net")
			
if __name__ == "__main__":
	main()
