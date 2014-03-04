from operator import itemgetter
import codecs
import imp 

inDir = "../../../dataset/"

def getIdAuthDict():
	
	idAuthDict = dict()
	
	fileR = open(inDir + "authIdMapAsm.csv")
	for line in fileR:
		line = line.replace("\n", "")
		tokens = line.split("\t")
		
		name = tokens[1].lower()
		_id = tokens[0]
		idAuthDict[_id] = name

	return idAuthDict

def main():

	
	types = {'follow','retweet', 'mention'}
	file_interface = imp.load_source("module.name", "../utility/file_interface.py")
	fi = file_interface.FileInterface()
	hubAuthListDict = dict()

	for _type in types:
		hubAuthListDict[_type] = fi.getHubAuthList(_type)
		
	commonSet = set()
	hubSetDict = dict()
	hubListDict = dict()
	# first check for hubs
	for _type in types:
		hubAuthList = hubAuthListDict[_type] 
		hubAuthList = sorted(hubAuthList, key = itemgetter(1))
		
		topSet = set()
		topList = list()
		for i in range(1,51):
			topSet.add(hubAuthList[i*-1][0])
			topList.append(hubAuthList[i*-1][0])

		print str(len(topSet))
		if len(commonSet) == 0:
			print "commonSet init"
			commonSet = topSet
		else:
			commonSet = commonSet.intersection(topSet)
		
		print str(len(commonSet))
		hubSetDict[_type] = topSet
		hubListDict[_type] = topList
	
	idAuthDict = getIdAuthDict()		

	for _id in commonSet:
		line = idAuthDict[_id]

		for _type in types:
			
			line = line + "\t" + str(hubListDict[_type].index(_id)+1)
	
		print line
		
if __name__ == "__main__":
	main()
