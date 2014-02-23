import xml.sax
import sys
import database
import codecs
import saveToRawFiles

debug = False

class DBLPContentHandler(xml.sax.ContentHandler):
	"""
		this class is Content Handler whcih gets a callback in case a particular tag is encountered in case of of parsing xml document. In case of DBLP we have added a condition 	
	"""
		
	

	def __init__(self):
		"""
		This is the init function for the SAX parser handler.
		"""
		#this list contains the current open tags. Its a stack to which push and pop the tags as they arrive
		self.elementStack = list()		

		# This is the dict element which stores the current tags and their values
		self.currentElementDict = dict()
		
		# this stores the current tag that we are considering currently
		self.currentElement = ""

		# this is string buffer to store the content for the current tag
		self.content = ""

		#this is just to get the name of the tags inside main tag its not used in the main program
#		self.mainElementDict = dict()	
		#count variable to track the current iteration. This we can use to check the program for finite iteration	
		self.count = 0

		#These tags are used for formatting like <i></i> for italic text. This can be removed as we want to get the complete text for a tag 
		self.stoptags = {"i","sup", "sub", "tt"}
		#print "hello"

		#database handler object
		self.dbHandler = database.DBHandler()
		self.rawFileHndl = saveToRawFiles.saveToRawFiles()

	def storeIntoDB(self, pubDict):
		
		"""
			store the encountered value of the publication into the database.
		"""
		if debug:
			print "database"
		
		keys = pubDict.keys()
		pubType = ""

		if "article" in keys:
			pubType = self.dbHandler.insertArticle(pubDict)
			
		if "proceedings" in keys:
			pubType = self.dbHandler.insertProceedings(pubDict)	

		if "inproceedings" in keys:
			pubType = self.rawFileHndl.saveIntoFile(pubDict)

		if "book" in keys:
			pubType = self.dbHandler.insertBook(pubDict)

		if "www" in keys:
			pubType = self.dbHandler.insertWWW(pubDict)

		if "masterthesis" in keys:
			pubType = self.datastructure.insertMasterThesis(pubDict)

		if "phdthesis" in keys:
			pubType = self.dbHandler.insertPHDThesis(pubDict)



	def startElement(self, name, attrs):

		"""
			The inherited function which is called in case a start element is encountered.
		"""

		#in case of stop tags (the one used for string formatting) return without doing anything
		if name in self.stoptags:
			return

		#nothing special needs to be done in case of start tag
		if len(self.elementStack)-1 == 0:
			if debug:
				print "start tag>>" + name
  		
		self.elementStack.append(name)
		self.currentElement = name
		
		'''
		#increment count to restrict the number of times this is called
		self.count = self.count + 1
		if self.count > 10000000:
			
			for i in self.mainElementDict.keys():
				print i				
				print self.mainElementDict[i]			
					
			sys.exit()
		'''
		
	def endElement(self, name):

		"""
			The inherited function which gets called when the end tag is encountered in an XML element.	
		"""
		
		#filter unwanted character from content
		self.content = self.content.replace("\n","")
		
		#in case of stop tags (the one used for string formatting) return without doing anything
		if name in self.stoptags:
			return
		
		
		#Pop the tag from the stack	
		self.elementStack.pop()

		#In case first element is encountered which is enclosing the article
		if len(self.elementStack)-1 == 0:

			# store the main element also to the dict
			self.currentElementDict[name] = self.content

			'''
			# take the tags in the main elements not required in main code		
			if name not in self.mainElementDict.keys():
				self.mainElementDict[name] = set(self.currentElementDict.keys())
			#take keys and union it with main element subelements			
			else:
				self.mainElementDict[name] = self.mainElementDict[name].union(set(self.currentElementDict.keys()))
			'''

			# this is a check to ensure we are gettinge extra author from the list
			'''			
			if "author" in self.currentElementDict.keys():
				if len(self.currentElementDict["author"]) > 1:
					print "more authors found"
					print self.currentElementDict["author"]
			'''

			#store the main tags into the database
			self.storeIntoDB(self.currentElementDict)

			#clear the dict for current element and get it ready for new main tag			
			self.currentElementDict.clear()
			
			
				
	
		# in case the tag is not the last element or main element
		else:		 
			#to get multiple authors
			if name == "author":

				#store the author name in existing list if it is present
				if "author" in self.currentElementDict.keys():
					author = self.content
					#author = author.decode('iso-8859-1')
					#author = author.encode('utf-8')
					authorList = self.currentElementDict[name].append(author)
					if debug:
						print "type>>" + str(type(authorList))
						print self.currentElementDict

				#create a new list for the author in case one is not present
				else:
					self.currentElementDict[name] = list()
					author = self.content
					#author = author.decode('iso-8859-1')
					#author = author.encode('utf-8')
					self.currentElementDict[name].append(author)
					# print the self and currentElementDict					
					if debug:
						print self.currentElementDict[name]
						print name
						print "list created and inserted"
						print self.currentElementDict
					
			# to get multiple editors
			elif name == "editor":

				# append to the list of editor if one is present
				if "editor" in self.currentElementDict.keys():
					self.currentElementDict[self.currentElement].append(self.content)

				# append to the list of editor if one is present				
				else:
					self.currentElementDict[self.currentElement] = list()
					self.currentElementDict[self.currentElement].append(self.content)

			# for all other tags		
			else:
				self.currentElementDict[self.currentElement] = self.content
					
				if debug:
					print "else case>>"+name
					print self.content				
			
			#clear the content to make it ready to store the content for new tag
			self.content =""
			if debug:			
				print "content_clear"
	
	def characters(self, content):
		#content = content.encode('ascii', 'ignore')
		content.replace("\n","")
		#append the content to existing tag	
		self.content = self.content + content
		if debug:		
			print self.content
		#print self.content

def main():
	t = DBLPContentHandler()	
	
	if debug:
		print "hello"
	#dblpFile = open("/home/subhash/Master_Project/network_data/dblp_dump_and_user_info/dblp.xml", "r", encoding='ISO-8859-1')
	dblpFile = codecs.open('/home/subhash/Master_Project/network_data/dblp_dump_and_user_info/dblp.xml', 'r', encoding='iso-8859-1')
	print "new codec"
	#dblpFile = open("../testXML.xml")	
	xml.sax.parse(dblpFile, t)

if __name__ == "__main__":
	main()
