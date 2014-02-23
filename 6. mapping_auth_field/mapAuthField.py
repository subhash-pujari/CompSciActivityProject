from operator import itemgetter
'''
	this script maps the auth to fields they are working.

'''

fileMapAuthConf = open("mapAuthConf.txt")
fileConfField = open("confField.csv")
fileMapAuthField = open("mapAuthField.csv", "w")

confFieldDict = dict()
authFieldDictDict = dict()
authFieldDict = dict()
def main():

	for line in fileConfField:

		line = line.replace("\n", "")	
		tokens = line.split("\t")
		field = tokens[0]
		conf = tokens[1]
		confabbr = conf.split(" ")[0]
		confFieldDict[confabbr] = field

	print confFieldDict 

	for line in fileMapAuthConf:
		
		line = line.replace("\n", "")
		tokens = line.split("\t")
		auth = tokens[0]
		
		for i in range(len(tokens)):
			
			if i < 1:
				continue

			conf = tokens[i]

			if conf not in confFieldDict:
				continue

			field = confFieldDict[conf]
			
			if auth in authFieldDict:
			
				if field in authFieldDict[auth]:
					
					authFieldDict[auth][field] = 	authFieldDict[auth][field] + 1	

				else:
				
					authFieldDict[auth][field] = 1

			else:
				authFieldDict[auth] = dict()
				authFieldDict[auth][field] = 1

	for auth in authFieldDict:

		authFieldList = list()		
		for field in authFieldDict[auth]:
			authFieldList.append((field, authFieldDict[auth][field]))


		authFieldList = sorted(authFieldList, key=itemgetter(1))
		print authFieldList

		topItem = authFieldList[-1]
		fileMapAuthField.write(auth+"\t"+topItem[0]+"\n")
		
if __name__ == "__main__":
	main()
