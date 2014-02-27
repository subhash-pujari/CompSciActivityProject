'''
This script is to map the twitter user to the DBLP users. This code has been written to map the parsed twitter user from the raw file and map them into the twitter username. We finally get a file with Twitter-id and username
'''

import codecs

inDir1 = "/home/subhash/Master_Project/6th_feb_2014_data/users/"
inDir2 = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

outDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

def getDblpAuthSet(dblpFile):

	authDblp = set()
	for line in dblpFile:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		for i in [range(3, len(tokens))][0]:
			name = tokens[i].lower()
			#print name
			authDblp.add(name.lower())

	print "str(len(authDblp)) >>" + str(len(authDblp))
	return authDblp

def getAuthIdDict(twFile):

	authDict = dict()
	for line in twFile:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		name = tokens[2].lower()
		print name
		authDict[name] = tokens[0]
		
	print "authDict len>>" + str(len(authDict))
	print authDict.keys()
	return authDict

def getSetFromDict(_dict):
	return set(_dict.keys())



def saveAuthIdDictToFile(authDict, validAuthSet):
	
	fileW = codecs.open(outDir + "authIdNameMap.tsv", "w", "UTF-8")
	for auth in authDict:
		if auth in validAuthSet:
			fileW.write(authDict[auth] + "\t" + auth + "\n")
			

def main():

	dblpFile = codecs.open(inDir2 + "inproceedings.tsv", 'r', 'UTF-8')
	twFile = codecs.open(inDir1 + "user_info.txt", 'r', 'UTF-8') 

	authDblp = getDblpAuthSet(dblpFile)
	authDict = getAuthIdDict(twFile)
	validAuthSet = authDblp.intersection(getSetFromDict(authDict))
	print "str(len(AuthSet))>>" + str(len(validAuthSet))
	saveAuthIdDictToFile(authDict, validAuthSet)

if __name__ == '__main__':
	main()
