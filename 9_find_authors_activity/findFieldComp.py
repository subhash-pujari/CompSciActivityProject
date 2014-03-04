import imp
from operator import itemgetter

'''
	This script is to find field composition in top authors
'''

def main():
	
	file_interface = imp.load_source("module.name", "../utility/file_interface.py")
	fi = file_interface.FileInterface()
	idNameDict = fi.getIdNameDict()
	nameIdDict = fi.getNameIdDict()
	nameFieldDict = fi.getNameFieldDict()
	
	types = ['mention']
	
	fieldCount = dict()
	count = 0
	for _type in types:
		hubList = fi.getHubAuthList(_type)
		hubList = sorted(hubList, key=itemgetter(2))
		for i in range(1,201):
			_tuple = hubList[-1*i]
			_id = _tuple[0]
			name = idNameDict[_id]
			if name in nameFieldDict:
				count = count + 1
				field = nameFieldDict[name]
				if field not in fieldCount:
					fieldCount[field] = 1
				else:
					fieldCount[field] = fieldCount[field] + 1
			
	for field in fieldCount:
		
		print count
		print fieldCount[field]
		per = float(fieldCount[field]) / float(count) * 100
		line = field + "\t" + str(per)+"%" + "\n"
		print line

if __name__ == "__main__":
	main()
