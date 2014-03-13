from operator import itemgetter
import file_interface

inDir = "/home/subhash/Dropbox/master_major_project/dataset/"

class CommBasedRoles:
		
	
	def __init__(self):
		print "hello"
		self.fieldFile = open(inDir + 'fieldRole.csv')
		self.commFile = open(inDir + 'commRole.csv')
		self.commList = self.initCommList()
		self.fieldList = self.initFieldList()
		self.file_interface = file_interface.FileInterface()
		self.idNameDict = self.file_interface.getIdNameDict()

	def initFieldList(self):
		fieldList = list()
		fieldFile = open(inDir + 'fieldRole.csv')
				
		for line in fieldFile:
			line = line.replace("\n", "")
			tokens = line.split("\t")
			_id = tokens[0]
			deg = tokens[1]
			comm = tokens[2]
			fieldList.append((_id, float(deg), float(comm)))
		
		print "len field List>>" + str(len(fieldList))
		return fieldList

	def initCommList(self):
		commList = list()
		commFile = open(inDir + 'commRole.csv')
		for line in commFile:
			line = line.replace("\n", "")
			tokens = line.split("\t")
			_id = tokens[0]
			deg = tokens[1]
			comm = tokens[2]
			commList.append((_id, float(deg), float(comm)))

		print "len comm List>>" + str(len(commList))
		return commList
		
	def getAmbassador(self, count, _type):
		print "get Ambassador"	
		degThres = 0.1
		commThres = 0.5
		filtList = list()
		topList = list()
		if _type == 'field':
			roleList = self.fieldList
	
		elif _type == 'comm':
			roleList = self.commList		
				
		for _tuple in roleList:
			if _tuple[1] > degThres and _tuple[2] > commThres:
				filtList.append(_tuple)

		print str(len(filtList))

		filtList = sorted(filtList, key=itemgetter(1))
		#print self.idNameDict[filtList[-1][0]]		
		
		for i in range(1, count+1):
			topList.append(self.idNameDict[filtList[-1*i][0]])

		return topList

		
			
	def getBridge(self, count, _type):
		degThres = 0.1
		commThres = 0.5
		filtList = list()
		topList = list()
		if _type == 'field':
			roleList = self.fieldList
		
		elif _type == 'comm':
			roleList = self.commList

		for _tuple in roleList:
			if _tuple[1] <= degThres and _tuple[2] > commThres:
				filtList.append(_tuple)

		print str(len(filtList))
		filtList = sorted(filtList, key=itemgetter(1))

		for i  in range(1, count + 1):
			topList.append(self.idNameDict[filtList[i][0]])
		return topList

	def getBigFish(self, count, _type):
		degThres = 0.1
		commThres = 0.5
	
		filtList = list()
		topList = list()
		if _type == 'field':
			roleList = self.fieldList

		elif _type== 'comm' :
			roleList = self.commList

		for _tuple in roleList:
			if _tuple[1] > degThres and _tuple[2] < commThres:
				filtList.append(_tuple)

		print str(len(filtList))

		filtList = sorted(filtList, key = itemgetter(1))

		for i in range(1, count + 1):
			topList.append(self.idNameDict[filtList[-1*i][0]])
		
		return topList		
	


def main():
	cbr = CommBasedRoles()
	fileW = open(inDir + 'commBasedRoles.tex', "w")
	types = ['field', 'comm']

	count = 10
	fileW.write("\\begin{table} \centering \\begin{tabular}{c|c|c}   \hline \n")
 	for _type in types:
		amb = cbr.getAmbassador(count, _type)
		bri = cbr.getBridge(count, _type)
		bf = cbr.getBigFish(count, _type)
		for i in range(count):
			fileW.write(amb[i] +" & "+ bri[i] + " & " + bf[i] + " \\\\" +"\n")
		fileW.write('\hline' + '\n')
	fileW.write("\end{tabular} \end{table}")
	print cbr.getAmbassador(10, 'comm')
	print cbr.getBridge(10, 'comm')
	print cbr.getBigFish(10, 'comm')
	print "hello"

if __name__ == "__main__":
	main()
