dataDir = "/home/subhash/Master_Project/6th_feb_2014_data/users/network_info/"
dataDirUsrInfo = "/home/subhash/Master_Project/6th_feb_2014_data/users/"
filtAuthFilename = "authIdNameList.txt"


folFileName = "user1_follows_user2.txt"
retFileName = "user1_retweets_user2.txt"
menFileName = "user1_mentions_user2.txt"

filtFolFileName = "filt_user1_follows_user2.txt"
#filtRetFileName = "filt_user1_retweet_user2.csv"
#filtMenFileName = "filt_user1_mention_user2.csv"
def main():
	folFile = dataDir + folFileName
	retFile = dataDir + retFileName
	menFile = dataDir + menFileName

		
	'''code to filter the data for the follow n/w'''
	authList = list()
	fileR = open(dataDirUsrInfo + "dblp_ids.txt")
	for line in fileR:
		line = line.replace("\n","")
		#line = line.split("\t")
		authList.append(line)

	fileR = open(folFile)
	fileW = open(filtFolFileName, "w")

	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		if len(tokens) >= 2:
			name1 = tokens[0]
			name2 = tokens[1]
			if name2 in authList and name1 in authList:
				print line
				line = line.replace("\t", ";")
				fileW.write(line)


if __name__ == "__main__":
	main()
