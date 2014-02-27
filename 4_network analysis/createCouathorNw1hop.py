import codecs

inDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

outDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"


# create set of all the identified user
def getAuthSet():

	authSet = set()
	fileR = codecs.open(inDir + "coAuthor_1.tsv", 'r', 'UTF-8')
	for line in fileR:
		line = line.replace("\n", "")
		authSet.add(line)
	print "len(authSet)>>" + str(len(authSet))
	return authSet
			

# create a id for all the authors which are identified
def getNodeIdDict(authSet):
	
	count = 0
	authIdDict = dict()
	for auth in authSet:
		if auth not in authIdDict:
			count = count + 1
			authIdDict[auth] = count 
	print "len(authIdDict)>>" + str(len(authIdDict))
	return authIdDict

#create nw for the identified users with their ids
def getCoAuthorNw(authIdDict):
	

	fileW = open(outDir + "coAuthorIdNw.csv", "w")

	fileInProc = codecs.open(inDir + "inproceedings.tsv", 'r', 'UTF-8')

	for line in fileInProc:
		
		coAuthSet = list()

		line = line.replace("\n", "")

		tokens = line.split("\t")

		for i in range(3, len(tokens)):
			auth = tokens[i].lower()
			if auth in authIdDict:
				coAuthSet.append(authIdDict[auth])

		if len(coAuthSet) > 1:
			for j in range(len(coAuthSet)):
				for k in range(j+1,len(coAuthSet)):
					fileW.write(str(coAuthSet[j]) + ";" + str(coAuthSet[k]) + "\n")

def saveAuthIdDict(authIdDict):

	fileW =codecs.open(outDir + "coAuthNameIdMap.csv", "w", "UTF-8")
	for auth in authIdDict:
		fileW.write(auth + "\t" + str(authIdDict[auth]) + "\n")

	fileW.close()

def main():
	authSet = getAuthSet()
	authIdDict = getNodeIdDict(authSet)
	saveAuthIdDict(authIdDict)
	getCoAuthorNw(authIdDict)

if __name__ == "__main__":
	main()


