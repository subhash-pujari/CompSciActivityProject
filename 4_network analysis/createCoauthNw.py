
# main dataset
inDir1 = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

# for dblp.ids
inDir2 = "/home/subhash/Master_Project/26feb2014/user_info/"

# for user_info.txt
inDir3 = "/home/subhash/Master_Project/6th_feb_2014_data/users/"

# outDir
outDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"


def getAuthIdMapAsm():
	
	dblp_id_file = open(inDir2 + "dblp.ids")
	user_info_file = open(inDir3 + "user_info.txt")
	
	fileW = open(outDir + "authIdMapAsm.csv", "w")

	dblpSet = set()

	authDict = dict()

	for line in dblp_id_file:
		line = line.replace("\n", "")
		dblpSet.add(line)

	for line in user_info_file:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		name = tokens[2].lower()
		if tokens[0] in dblpSet:
			authDict[name] = tokens[0]

	for auth in authDict:
		_id = authDict[auth]
		fileW.write(_id + "\t" + auth + "\n")
	
	print "str(len(authDict))>>" + str(len(authDict))		
 
def getInitDblpSet():
	
	dblpSet = set()
	fileDblp = open(inDir1 + "authIdMapAsm.csv")

	for line in fileDblp:
                line = line.replace("\n", "")

                tokens = line.split("\t")
                dblpSet.add(tokens[1].lower())

        print "str(len(dblp_set))>>" + str(len(dblpSet))
	return dblpSet


def getPass(prevPassSet):
	
	neighSet = set()

	fileR = open(inDir1 + "inproceedings.tsv")

	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")

		authSet = set()
		conLastPassAuth = False

		for i in range(3, len(tokens)):
			
			name = tokens[i].lower()
			if name in prevPassSet:
				conLastPassAuth = True
				continue
				
			authSet.add(name)
				
		if conLastPassAuth:
			neighSet = neighSet.union(authSet)
			
	
	print "str(len(neighSet))>>" + str(len(neighSet))
	return neighSet

def main():
	# do the task in three pass

	# first pass get all the dblp author nodes

	dblpSet = getInitDblpSet()
	neighSet = getPass(dblpSet)
	print "str(len(neighSet))>> pass 1" + str(len(neighSet))
	prevPassSet = dblpSet.union(neighSet)
	print "total after pass>>" + str(len(prevPassSet))
	neighSet = getPass(prevPassSet)
	print "str(len(neighSet))>> pass 2" + str(len(neighSet))
	
	# second pass get all the nodes that have coauthored a paper with dblp detected authors

	# so we can have list of set as data structure
	
	# create the id name map asmelash
	#getAuthIdMapAsm()
	
if __name__ == "__main__":
	main()
