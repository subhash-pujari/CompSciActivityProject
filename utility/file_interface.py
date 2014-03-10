import imp

'''
	This class is an interface to the file system and provides data structure to rest of the API
'''

class FileInterface:

	def __init__(self):
		self.root_dir = "../../dataset/"

		self._type = ['follow', 'retweet', 'mention']
		# data file
		self.datafiles = {self._type[0]:'filt_user1_follows_user2_data.csv' , self._type[1]:'filt_user1_retweets_user2_data.csv', self._type[2]: 'filt_user1_mentions_user2_data.csv'}
		self.modIndex = {self._type[0]:13, self._type[1]:11, self._type[2]:13}
	
	def getIdNameDict(self):
		
		idNameDict = dict()
		filename = self.root_dir + "authIdMapAsm.csv"
		fileR = open(filename)

		for line in fileR:
			line = line.replace('\n', '')
			tokens = line.split("\t")
			_id = tokens[0]	
			name = tokens[1]
			idNameDict[_id] = name

		print str(len(idNameDict))
		return idNameDict

	def getNameIdDict(self):
		nameIdDict = dict()

		filename = self.root_dir + "authIdMapAsm.csv"
		fileR = open(filename)
		for line in fileR:
			
			line = line.replace("\n", "")
			tokens = line.split("\t")
			name = tokens[1]	
			_id = tokens[0]

			nameIdDict[name] = _id	
		
		print len(nameIdDict)	
		return nameIdDict

	def getCommIdDict(self, _type):
		commIdDict = dict()
		filtCommIdDict = dict()
		
		filename = self.datafiles[_type]
		modIndex = self.modIndex[_type]

		fileR = open(self.root_dir + filename)
		for line in fileR:
			line = line.replace("\n", "")
			tokens = line.split(" ")
			_id = tokens[0]
			comm = tokens[modIndex]
			if comm not in commIdDict:
				commIdDict[comm] = set()
				commIdDict[comm].add(_id)

			else:
				commIdDict[comm].add(_id)

		for comm in commIdDict:
			if len(commIdDict[comm]) > 5:
				filtCommIdDict[comm] = commIdDict[comm] 
		print len(filtCommIdDict)
		return filtCommIdDict

	def getIdFieldDict(self):
		
		idFieldDict = dict()
		nameIdDict = self.getNameIdDict()

		fileR = open(self.root_dir + 'mapAuthField.csv')
		for line in fileR:
			line = line.replace("\n", "")
			tokens = line.split("\t")
			name = tokens[0]
			field  = tokens[1]
			
			if name in nameIdDict:
				_id = nameIdDict[name]
				#print _id
				idFieldDict[nameIdDict[name]] = field
		
		idNameDict = self.getIdNameDict()	
		print len(idFieldDict)
		return idFieldDict

	
		

def main():
	fi = FileInterface()
	fi.getIdNameDict()
	fi.getCommIdDict('follow')
	fi.getNameIdDict()
	fi.getIdFieldDict()

if __name__ == '__main__':
	main()

