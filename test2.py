import xml.etree.ElementTree as xml
from sklearn import svm
import numpy as np

pitfalls = ["long", "difficult", "hard", "understand", "formidable", "challenging", "troublesome", "confused", "test", "tried"]
beginner = ["beginner", "elementry", "sorry", "new", "first", "time", "never", "hw", "easy"]

def getFeatures(child, userRoot):
    try:
        features = list()
        x = child.attrib.get('ViewCount')
        x = 0 if x is None else float(x)
        features.append(x)

        x = child.attrib.get('Counts')
        x = 0 if x is None else float(x)
        features.append(x)

        x = child.attrib.get('Score')
        x = 0 if x is None else float(x)
        features.append(x)
        pit = 0
        beg = 0
        if 'Body' in child.attrib:
            for word in pitfalls:
                if word in [x.lower for x in child.attrib.get('Body').split()]:
                    pit += 1

            for word in beginner:
                if word in [x.lower for x in child.attrib.get('Body')]:
                    beg += 1
        features.append(float(pit))
        features.append(float(beg))

        user = child.attrib.get('OwnerUserId')
        rep = 0
        if user is not None:
            for x in userRoot:
                if x.attrib.get('Id') == user and 'Reputation' in x.attrib:
                    rep += float(x.attrib['Reputation'])
        features.append(float(rep))
        features =  np.asarray(features)
        return features
    except:
        print "error"

def getTrainingSample(root, userRoot, filename):
    f = open(filename)
    classifies = list()
    features = list()
    for line in f:
        line = line.split()
        identifier = line[0]
        classifies.append(int(line[1]))
        for child in root:
            if child.attrib.get('Id') == identifier:
                features.append(getFeatures(child, userRoot))
    features = np.asarray(features)
    print features.shape
    return [classifies, features]



def learn(x):
    clf = svm.SVC()
    clf.fit(x[1], x[0])
    return clf

def main():
    users = xml.parse('../stackdata/cs.stackexchange.com/Users.xml')
    userRoot = users.getroot()

    tree = xml.parse('../stackdata/cs.stackexchange.com/Posts.xml')
    root = tree.getroot()

    samples = getTrainingSample(root, userRoot, "testdata.txt")
    print samples
    clf = learn(samples);
    print clf
    keyword = "regular"
    toRank = list()
    posts = list()
    for child in root:
        try:
            if child is not None:
                if(keyword in [x.lower() for x in child.attrib['Body'].split()]):
                    toRank.append(getFeatures(child, userRoot))
                    posts.append(child)
        except:
            pass
    ranks = clf.decision_function(toRank)
    final = [ (x,y) for x,y in zip(posts, ranks)]
    asdf = sorted(final, key = lambda (x,y): y)[:10]
    for fdsa,i in zip(asdf, range(len(asdf))):
        if i > 10:
            break
        print fdsa[0].attrib
main()
