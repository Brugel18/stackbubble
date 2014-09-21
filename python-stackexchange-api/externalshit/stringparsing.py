
import xml.etree.ElementTree as E




thetree = E.parse('Posts.xml')
root = thetree.getroot()



def childrenizer(Atree):    #print out data
    for children in Atree:
        print children.attrib
        childrenizer(children)

childrenizer(root)


