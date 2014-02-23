
from operator import itemgetter


fieldAuthIdDict = dict()

def initFieldAuthDict():
	fileR = open("authIdNameList.txt")
	nameIdDict = dict()
	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		_id = tokens[0]
		name = tokens[1]
		nameIdDict[name] = _id		

	print "nameIdDict>>" + str(len(nameIdDict))

	fileR = open("mapAuthField.csv")
	fieldAuthDict = dict()
	for line in fileR:
		line = line.replace("\n","")
		tokens = line.split("\t")
	
		name = tokens[0]
		field = tokens[1]

		if field in fieldAuthDict:
			fieldAuthDict[field].append(name)	
		else:
			fieldAuthDict[field] = list()
		
	cnt = 0

	for field in fieldAuthDict:
		print field + str(len(fieldAuthDict[field]))
		cnt = cnt + len(fieldAuthDict[field])

	print "number of authors in field>>" + str(cnt)

	#convert name into id field
	for field in fieldAuthDict:
		fieldAuthIdDict[field] = list()
		nameList = fieldAuthDict[field]
		for name in nameList:
			fieldAuthIdDict[field].append(nameIdDict[name])
	
	print "\nid count>> \n"
	for field in fieldAuthIdDict:
		print field + "  >>  "+ str(len(fieldAuthIdDict[field]))

def getField(user):
	#print len(fieldAuthIdDict)
	for field in fieldAuthIdDict:
		#print field	
		fieldList = fieldAuthIdDict[field]
		if user in fieldList:
			return field

def getFieldsUser(user1, user2):
	print user1 + " >> "+ user2
	return (getField(user1), getField(user2))


def main():

	#init
	initFieldAuthDict()
	
	#print "init>>" + str(len(fieldAuthIdDict))
	fieldFieldMapDict  = dict()

	#create a field to field map
	fileR = open("filt_user1_mention_user2.csv")

	
	for line in fileR:
		print line
		tokens = line.split(";")
		user1 = tokens[0]
		user2 = tokens[1]
		user2 = user2.replace("\n", "")
		fieldFlow = getFieldsUser(user1, user2)
		if fieldFlow[0] is None or fieldFlow[1] is None:
			continue
	
		if fieldFlow[0] not in fieldFieldMapDict:	
			fieldFieldMapDict[fieldFlow[0]] = dict()
			if fieldFlow[1] not in fieldFieldMapDict[fieldFlow[0]]:
				fieldFieldMapDict[fieldFlow[0]][fieldFlow[1]] = 1
			else:
				fieldFieldMapDict[fieldFlow[0]][fieldFlow[1]] = fieldFieldMapDict[fieldFlow[0]][fieldFlow[1]] + 1
		else:
			if fieldFlow[1] not in fieldFieldMapDict[fieldFlow[0]]:
				fieldFieldMapDict[fieldFlow[0]][fieldFlow[1]] = 1
			else:
				fieldFieldMapDict[fieldFlow[0]][fieldFlow[1]] = fieldFieldMapDict[fieldFlow[0]][fieldFlow[1]] + 1

	print fieldFieldMapDict

	keys = fieldFieldMapDict.keys()
	fileW = open("mention.net", "w")

	fileW.write("*Vertices "+str(len(fieldDict))+ "\n")
	for index in range(len(keys)):
		field = keys[index]
		fieldDict = fieldFieldMapDict[field]
		count = 0
		for field1 in fieldDict:
			count = count + fieldDict[field1]
		if field is None:
			continue

 		line = str(index+1) +' "'+field+'" '+ str(count) + "\n"
		fileW.write(line)
	
	

	tupleFinalList = list()

	for index in range(len(keys)):
		field = keys[index]
		fieldDict = fieldFieldMapDict[field]
		
		#for each field define a tuple list
		tupleFieldFieldList  = list()				
		for field1 in fieldDict:
			if field1 is None:
				continue
			tup = (field)			
			indexField1 = keys.index(field1)
			#line = str(index+1) + " " + str(indexField1+1) + " " + str(fieldDict[field1]) + "\n"
			#fileW.write(line)
			tupleFieldFieldList.append((index+1, indexField1+1, fieldDict[field1]))

		tupleFieldFieldList = sorted(tupleFieldFieldList, key=itemgetter(2))

		for i in range(5):
			tupleFinalList.append(tupleFieldFieldList[-1*(i+1)])

	fileW.write("*Arcs "+ str(len(tupleFinalList))+ "\n")
	for item in tupleFinalList:
		fileW.write(item[0] + " " +item[1] + " " + str(item[2]) + "\n")
		
			
if __name__ == "__main__":
	main()
