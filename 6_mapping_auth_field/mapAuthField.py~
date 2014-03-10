from operator import itemgetter
import codecs
'''
	this script maps the auth to fields they are working.

'''

inDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

def getConfFieldDict():
	
	confFieldDict = dict()

	fileConfField = codecs.open(inDir + "confField.csv", "r", "UTF-8")
	
	for line in fileConfField:

                line = line.replace("\n", "")   
                tokens = line.split("\t")
                field = tokens[0]
                conf = tokens[1]
                confabbr = conf.split(" ")[0]
                confFieldDict[confabbr.lower()] = field
	print "confFieldDict>>" + str(len(confFieldDict))
	return confFieldDict

def getAuthFieldDict(confFieldDict):

	fileMapAuthConf = codecs.open(inDir + "mapAuthConf.txt", 'r', 'UTF-8')
	authFieldDict = dict()

	for line in fileMapAuthConf:

                line = line.replace("\n", "")
                tokens = line.split("\t")
                auth = tokens[0]
	
                for i in range(1, len(tokens)):

                        conf = tokens[i].lower()

                        if conf not in confFieldDict:
				continue

			field = confFieldDict[conf]
			print field
                        if auth in authFieldDict:

                                if field in authFieldDict[auth]:
					authFieldDict[auth][field] =    authFieldDict[auth][field] + 1
				else:
					authFieldDict[auth][field] = 1
			else:
				authFieldDict[auth] = dict()
				authFieldDict[auth][field] = 1

	print "authFieldDict>>" + str(len(authFieldDict))	
	return authFieldDict

def saveToFile(authFieldDict):
	

	fileMapAuthField = codecs.open(inDir + "mapAuthField.csv", "w", "UTF-8")
	for auth in authFieldDict:

                authFieldList = list()          
                for field in authFieldDict[auth]:
                        authFieldList.append((field, authFieldDict[auth][field]))


                authFieldList = sorted(authFieldList, key=itemgetter(1))
                print authFieldList

                topItem = authFieldList[-1]
                fileMapAuthField.write(auth+"\t"+topItem[0]+"\n")


def main():
	
	saveToFile(getAuthFieldDict(getConfFieldDict()))	
				
if __name__ == "__main__":
	main()
