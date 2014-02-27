
#inputDir
inDir = "/home/subhash/Master_Project/26feb2014/user_info/"

#output Dir
outDir = "/home/subhash/Dropbox/master_major_project/python_script/dataset/"

#list of filenames
fileNameList = ["user1_follows_user2", "user1_retweets_user2", "user1_mentions_user2"]

dblp_ids = "dblp.ids"

def main():
	
	authList = list()

	fileR = open(inDir + dblp_ids)
	# initialise the authlist dblp
	for line in fileR:
		line = line.replace("\n","")
		#line = line.split("\t")
		authList.append(line)

	for fileName in fileNameList:
		print "currently doing >>" + fileName
		fileR = open(inDir + fileName)
		fileW = open(outDir + "filt_"+ fileName + ".tsv", "w")
		for line in fileR:
			line = line.replace("\n", "")
			tokens = line.split("\t")

			if len(tokens) >= 2:
				id1 = tokens[0]
				id2 = tokens[1]
				if id2 in authList and id1 in authList:
					line = line.replace("\t", ";")
					line = line + "\n"
					fileW.write(line)
		
if __name__ == "__main__":
	main()
