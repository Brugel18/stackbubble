

import xml.etree.ElementTree as E


def properwrap(astring): #properly wraps string
	return ("<" + astring + ">")

def printthetags(theobject):
	for nodes in theobject:
		try:
			print properwrap(nodes.attrib['TagName'])
		except:
			pass


def tagparsing(theobject1, theobject2): #theobject1 is the xml tree, the object2 is the tag set
	TagArray = [] #array of tags
	for nodes in theobject2:
		try:
			TagArray.append(nodes.attrib['TagName'])
		except:
			pass
	fileArray = []
	for goods in TagArray:
		fileArray.append(open(goods + '.json','w'))
	i = 0 #index for tagging
	for nodes in theobject1:
		i = 0
		while(i < len(TagArray)):
			try:
				if(TagArray[i] in nodes.attrib['Tags']):
					fileArray[i].write("{'color':getRandomColor(),'shape':'dot','label':'Strings', 'size': 60, 'isExploded':false, \"precedence\": 2," + (str(nodes.attrib) + "},")) 
				

			except:
				pass
			i = i + 1
	i = 0
	fileArray.append(open("allthenames.json", 'w'))

	
	while(i < len(fileArray)-1): #simultaneously writes to last file arrray and closes files
		fileArray[len(fileArray)-1].write("{'color':getRandomColor(),'shape':'dot','label':'Strings', 'size': 60, 'isExploded':false, \"precedence\": 2," + TagArray[i]+ "},")
		fileArray[i].close()
		i = i + 1
	fileArray[i].close()











thetree1 = E.parse('c:/users/sidharth/documents/Github/DownloadsNSFW/cs.stackexchange.com/tags.xml')
root1 = thetree1.getroot()

thetree2 = E.parse('c:/users/sidharth/documents/Github/DownloadsNSFW/cs.stackexchange.com/Posts.xml')
root2 = thetree2.getroot()



def childrenizer(Atree):    #print out data
    for children in Atree:
        print children.attrib["TagName"], " ", children.attrib["Count"]
        childrenizer(children)

tagparsing(root2, root1)