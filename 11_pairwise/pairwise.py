import codecs

inDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

totalIdSet = set()

def getAuthNameIdDict():
	filename = inDir + "authIdMapAsm.csv"

	fileR = codecs.open(filename, 'r', 'UTF-8')

	authIdDict = dict()
	idAuthDict = dict()
	
	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")

		name = tokens[1]
		_id = tokens[0]

		authIdDict[name] = _id
		idAuthDict[_id] = name

	print "len authIdDict >> idAuthDict >> " + str(len(authIdDict)) + ">> " + str(len(idAuthDict))

	return(authIdDict, idAuthDict)

def getPairwise(filename, idAuthDict):

	authAuthCnt = dict()

	fileR = open(filename)

	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split(";")
		
		id1 = tokens[0]
		id2 = tokens[1]

		if id2 in idAuthDict:
			
			if id2 not in authAuthCnt:
				authAuthCnt[id2] = dict()
				authAuthCnt[id2][id1] = 1

			else:
				if id1 not in authAuthCnt[id2]:
					authAuthCnt[id2][id1] = 1
				else:
					authAuthCnt[id2][id1] = authAuthCnt[id2][id1] + 1
					#print "again came"

		totalIdSet.add(id1)
		totalIdSet.add(id2)

	print "len authAuthCnt>>" + str(len(authAuthCnt))

	return authAuthCnt
			 
def getPairWiseCoAuth(authIdDict):
	
	fileR = codecs.open(inDir + "coauthor.csv", 'r', 'UTF-8')
	coAuthorDict = dict()

	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split(";")
			
		name1 = tokens[0].lower()
		name2 = tokens[1].lower()

		if name1 in authIdDict and name2 in authIdDict:
			
			id1 = authIdDict[name1]
			id2 = authIdDict[name2]

			#print id1
			#print id2
	
			#print coAuthorDict

			if id1 not in coAuthorDict:
				coAuthorDict[id1] = dict()
				coAuthorDict[id1][id2] = 1
			else:
				if id2 not in coAuthorDict[id1]:
					coAuthorDict[id1][id2] = 1
				else:
					#print "again came"
					coAuthorDict[id1][id2] = coAuthorDict[id1][id2] + 1
		
			totalIdSet.add(id1)
			totalIdSet.add(id2)	 
	
	print "len coAuthCnt >> " + str(len(coAuthorDict))
	return coAuthorDict


def main():
	print "hello"
	dicts = getAuthNameIdDict()
	authIdDict = dicts[0]
	idAuthDict = dicts[1]
	menAuthAuthCnt = getPairwise(inDir + "filt_user1_mentions_user2.csv" , dicts[1])
	retAuthAuthCnt = getPairwise(inDir + "filt_user1_retweets_user2.csv" , dicts[1])
	coAuthorDict = getPairWiseCoAuth(dicts[0])

	#print menAuthAuthCnt
	#print retAuthAuthCnt
	#print coAuthorDict

	print "len totalIdSet >>" + str(len(totalIdSet))
	
	fileW = codecs.open(inDir + "pairwise.tsv", "w", "UTF-8")
	fileW.write("user1" + "\t" + "user2" + "\t" + "men" + "\t" + "ret" + "\t" + "coAuth" + "\n")
	for id1 in totalIdSet:
		for id2 in totalIdSet:
		
			men = 0
			ret = 0
			coAuth = 0

			if id1 in menAuthAuthCnt:
				if id2 in menAuthAuthCnt[id1]:
					men = menAuthAuthCnt[id1][id2]
					
			if id1 in retAuthAuthCnt:
				if id2 in retAuthAuthCnt[id1]:
					ret = retAuthAuthCnt[id1][id2]

			if id1 in coAuthorDict:
				if id2 in coAuthorDict[id1]:
					coAuth = coAuth + coAuthorDict[id1][id2]

			if id2 in coAuthorDict:
				if id1 in coAuthorDict[id2]:
					coAuth = coAuth + coAuthorDict[id2][id1]					
					

			if men != 0 or ret != 0 or coAuth != 0:
				line = idAuthDict[id1] + "\t" + idAuthDict[id2] + "\t" + str(men) + "\t" + str(ret) + "\t" + str(coAuth) + "\n"
				fileW.write(line)
				print line

if __name__ == "__main__":
	main()
