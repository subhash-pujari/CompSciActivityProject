from operator import itemgetter

class Community:
	
	def __init__(self, fieldDict):
		self.fieldDict = fieldDict
		self.fieldMap = FieldMap()
		self.topFieldNum = 3	
	def getTop3Field(self):

		fieldList = list()
		
		for field in self.fieldDict:
			fieldList.append((self.fieldMap.getFieldAcronym(field), self.fieldDict[field]))
		fieldList = sorted(fieldList, key=itemgetter(1))
		print fieldList
		if len(fieldList) > self.topFieldNum:
			topFieldList = list()
			for i in range(1, self.topFieldNum+1):
				topFieldList.append(fieldList[-1*i])
			
			return topFieldList
		else:	
			return fieldList

class FieldMap:
	
	def __init__(self):
		self.acronym = {'ComputerArchitecture':'CA', 'SoftwareEngineering':'SE', 'ComputerGraphics':'CG', 'SecurityAndPrivacy':'SNP', 'DataManagement':'DM',  'ConcurrentDistributedAndParallelComputing':'CDP', 'ComputationalBiology':'CB', 'ComputerNetworkingAndNetworkedSystems':'CN' , 'AlgorithmsAndTheory':'ATH', 'ProgrammingLanguages':'PL', 'Education':'ED', 'OperatingSystems':'OS', 'ArtificialIntelligence':'AI' , 'HumanComputerInteraction':'HCI'}

	def getFieldAcronym(self, fieldName):
		
		if fieldName in self.acronym:

			return self.acronym[fieldName]
		else: 
			print "notFound>>" +fieldName
			return None

	def getFieldList(self):
		
		return self.acronym.keys()

def main():
	fm = FieldMap()
	print fm.getFieldAcronym('SoftwareEngineering')
	fieldDict = {'AlgorithmsAndTheory':2}
	cm = Community(fieldDict)
	print cm.getTop3Field()

if __name__ == "__main__":
	main()	
