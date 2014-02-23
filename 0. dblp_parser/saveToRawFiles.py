
import codecs

class saveToRawFiles():
	
	def __init__(self):
		self.file = codecs.open("inproceedings.tsv","w")
		print "init"

	
	def saveIntoFile(self, tagDict):
		print "save into file"				
		keys = tagDict.keys()
		if "inproceedings" in keys:
			self.saveInProceeding(tagDict)		
		

	def saveInProceeding(self, tagDict):

		keys = tagDict.keys()
		author = str()
		if 'author' in keys:
			authorList = tagDict['author']
			if len(authorList) > 1:
				print 'more than 1 author len>>' + str(len(authorList))
				print authorList		
			if authorList is not None:
				for i in authorList:
					author = author + i + "\t"
					print author

			

		conf = tagDict['booktitle']

		title = tagDict['title']

		year = tagDict['year']


		line = title + '\t' + conf +'\t'+ year + '\t' + author +'\n'
		print line
		line = line.encode("utf-8")		
		
		self.file.write(line)		

