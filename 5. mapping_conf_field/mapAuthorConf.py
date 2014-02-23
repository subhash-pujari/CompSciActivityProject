'''

This file is to map the author to the conferences they have published.

1. One publication should be considered as one count of conference published to.

2. Duplicates in conferences is allowed
 
'''

fileInproceedings = codecs.open('/home/subhash/Master_Project/network_data/dblp_dump_and_user_info/dblp.xml', 'r', encoding='UTF-8')
fileNameId = open("authIdNameList.txt")
fileMapAuthConf = open("mapAuthConf.txt", "w")
 
# this dict will contain author and conferences he has published to

dblpTwtAuthList = list()
authConfDict = dict()

def main():
	
	
	#populate author List
	for line in fileNameId:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		authName = tokens[1].lower()
		print "authName>>" + authName
		dblpTwtAuthList.append(authName)

	count = 0

	for line in fileInproceedings:
		line = 		
		line = line.replace("\n" , "")
		tokens = line.split("\t")
		
		if len(tokens) < 4:
			continue

		title = tokens[0]
		conf = tokens[1]
		year = tokens[2]
		
		for i in range(len(tokens)):
			
			if i < 3:
				continue
		
			authName = tokens[i]
			authName = authName.lower()

			if authName is "":
				continue
			
			if authName in dblpTwtAuthList:
				if authName in authConfDict:
					authConfDict[authName].append(conf)
				else:
					authConfDict[authName] = list() 
					authConfDict[authName].append(conf)
		count = count + 1
		print str(count)

	print "str(len(authConfDict))>>" + str(len(authConfDict))
	
	print authConfDict

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


if __name__ == "__main__":
	main()
	
