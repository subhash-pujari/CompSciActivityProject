'''
	This script stores the auth and conferences that he have published to. If author have published in one conference more than once then multiple occurence of the conference will be there
'''
import codecs


inDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"
outDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

def getAuthList():

	dblpTwitAuthList = list()
	fileNameId = codecs.open(inDir + "authIdNameList.txt", 'r', 'UTF-8')
	for line in fileNameId:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		authName = tokens[1].lower()
		dblpTwitAuthList.append(authName)

	print "dblpTwitAuthList len>>" + str(len(dblpTwitAuthList))
	return dblpTwitAuthList

def getAuthConfDict(dblpTwitAuthList):

	authConfDict = dict()
	inproFile = "inproceedings.tsv"
	fileInproceedings = codecs.open(inDir + inproFile, 'r', encoding='UTF-8')

	for line in fileInproceedings:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		
		# if author data missing continue
		if len(tokens) < 4:
			continue


		# first three tokens are title, conf, year
		title = tokens[0]
		conf = tokens[1]
		year = tokens[2]

		
		# go thru all the tokens
		for i in [range(3, len(tokens))][0]:
			authName = tokens[i].lower()

			if authName == "":
				continue


			# check for auth name is in the matched author set
			if authName in dblpTwitAuthList:
				# if auth conf list is initialised add the conf to his list
				if authName in authConfDict:
					authConfDict[authName].append(conf)
				# or else initialise the list
				else:
					authConfDict[authName] = list()
					authConfDict[authName].append(conf)

		print "len(authConfDict)>>" + str(len(authConfDict))
		return authConfDict

def writeAuthDictToFile(authConfDict, filename):

	fileMapAuthConf = open(filename, "w")

	for auth in authConfDict:
                
                print "auth" + auth
                line = str(auth)
                print auth
                confList = authConfDict[auth]
                print "conf List>>"
                print confList
                for conf in confList:
                        line = line +"\t"+ conf 

                line = line + "\n"
                print line
                fileMapAuthConf.write(line)
				
def main():


	filenameMapAuthConf = outDir + "mapAuthConf.txt"
	writeAuthDictToFile(getAuthConfDict(getAuthList()), filenameMapAuthConf)


if __name__ == "__main__":
	main()
	
