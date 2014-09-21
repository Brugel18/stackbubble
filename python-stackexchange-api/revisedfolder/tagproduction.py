

import xml.etree.ElementTree as E
import os



dirlist = os.listdir("C:\Users\Sidharth\Documents\GitHub\DownloadsNSFW\cs.stackexchange.com\TheG20")

def properwrap(astring): #properly wraps string
	return ("<" + astring + ">")

def printthetags(theobject):
	for nodes in theobject:
		try:
			print properwrap(nodes.attrib['TagName'])
		except:
			pass


def tagparsing(theobject1, theobject2): #theobject1 is the xml tree, the object2 is the refined tag list
	TagArray = [] #array of tags
	fileArray = []
	for nodes in theobject2:
		try:
			
			TagArray.append(nodes)
		except:
			print "hi"
			pass




	for goods in TagArray:
		fileArray.append(open(goods,'w'))

		
	i = 0 #index for tagging
	k = 0
	equalizer = 0 #matching up the write value
	tempstring = "buklauu"
	subtractor = 0
	for nodes, k in zip(theobject1, range(len(theobject1))):
		i = 0
		

		while(i < len(fileArray)):
			
			try:	

				if(TagArray[i][:-5] in str(nodes.attrib['Tags'])):
					
					
					tempstring = "\"" + str(equalizer + k)+"\":{\"color\":\"Blue\",\"shape\": \"dot\",\"label\":\"Strings\", \"size\": 60, \"isExploded\":false, \"precedence\": 2," + TagArray[i] + "},"
					
					fileArray[i].write(tempstring)
			except:

				equalizer = equalizer - 1
				pass		
				
				

			
			i = i + 1
			
		equalizer = equalizer + k 
		
	i = 0
	fileArray.append(open("allthenames.json", 'w'))
	TagArray.append("allthenames.json")

	
	while(i < len(fileArray)-1): #simultaneously writes to last file arrray and closes files
		tempstring = "\"" + str(equalizer + i) + "\":{\"color\":\"Blue\",\"shape\":\"dot\",\"label\":\"Strings\", \"size\": " +  str(os.path.getsize("C:\Users\Sidharth\Documents\GitHub\DownloadsNSFW\cs.stackexchange.com\TheG20\\" + dirlist[i])) + ", \"isExploded\":false, \"precedence\": 2, + \"filename\" : \"" + TagArray[i]+ "\"},"
	
		fileArray[len(fileArray)-1].write(tempstring)
		fileArray[i].close()
		i = i + 1
	fileArray[i].close()

	""" while(i < len(fileArray)):
		fileArray[i] = open(TagArray[i], "r+")
		x = fileArray[i].read()
		print x
		print "hi"
		print x
		fileArray[i].seek(-1, 2)

		fileArray[i].truncate()
		fileArray[i].close()
		i = i + 1 """














thetree1 = E.parse('c:/users/sidharth/documents/Github/DownloadsNSFW/cs.stackexchange.com/tags.xml')
root1 = thetree1.getroot()

thetree2 = E.parse('c:/users/sidharth/documents/Github/DownloadsNSFW/cs.stackexchange.com/Posts.xml')
root2 = thetree2.getroot()



def childrenizer(Atree):    #print out data
    for children in Atree:
        print children.attrib["TagName"], " ", children.attrib["Count"]
        childrenizer(children)

tagparsing(root2, dirlist)