import imp
from operator import itemgetter

class CommFieldDist:
		
	def __init__(self):
		file_interface = imp.load_source('module.name', '../utility/file_interface.py')
		fi = file_interface.FileInterface()
		
		self.idNameDict = fi.getIdNameDict()
		self.idFieldDict = fi.getIdFieldDict()
		self.commIdDict = fi.getCommIdDict('follow')
		
	def getCommFieldDict(self):
		
		commFieldDict = dict()
		for comm in self.commIdDict:
			commFieldDict[comm] = dict()
			
			idSet = self.commIdDict[comm]
			for _id in idSet:
				if _id in self.idFieldDict:
					
					field = self.idFieldDict[_id]
					if field not in commFieldDict[comm]:
						commFieldDict[comm][field] = 1
					else:
						commFieldDict[comm][field] = commFieldDict[comm][field] + 1
					
		return commFieldDict	
	
				

def main():
	print "hello"
	commDict =  CommFieldDist().getCommFieldDict()
	datastruct = imp.load_source("module.name", "../utility/datastruct.py")
	fieldMap = datastruct.FieldMap()
	fieldList = fieldMap.getFieldList()
	print fieldList
	fileW = open("../../dataset/" + "commFieldDist.csv", "w")
	line = 'field_name'
	for field in fieldList:
		line = line + " "+fieldMap.getFieldAcronym(field)
	
	line = line + "\n"
	fileW.write(line)

	commCountList = list()
 
	for comm in commDict:
		community = datastruct.Community(commDict[comm])
		topFieldList =  community.getTop3Field()
		commName = ''
		for field in topFieldList:
			if commName == '':
				commName = field[0]
			else:
				commName = commName + "+"+field[0]
		
		line = commName
		count = 0
		for field in fieldList:
			if field in community.fieldDict:
				countStr = community.fieldDict[field]
				count = count + community.fieldDict[field]
				
			else:
				count = count + 0
				countStr = 0
			
			line = line + " " + str(countStr)
		
		commCountList.append((line, count))
	commCountList = sorted(commCountList, key=itemgetter(1))
	for _id in range(1, len(commCountList)+1):
		fileW.write(commCountList[_id * -1][0] + "\n")
				

if __name__ == "__main__":
	main()
