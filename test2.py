import xml.etree.ElementTree as xml
from sklearn import svm

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
    return [classifies, features]



def learn(x):
    clf = svm.SVC()
    clf.fit([[1,2,3],[1,2,2]], [0,1])
    return clf


def scorer(weights, features):
    score = 0
    for x,y in zip(weights, features):
        score += x*y
    return score

def scorer_difficult_problems(features):
#todo learn weights
    weights = [50, 10, 10, 200, -100, 1]
    return scorer(weights, features)

def scorer_common_pitfall(features):
#todo learn weights
    weights = [100, 50, 50, 100, 200, -1]
    return scorer(weights, features)



def main():
    users = xml.parse('../stackdata/cs.stackexchange.com/Users.xml')
    userRoot = users.getroot()

    tree = xml.parse('../stackdata/cs.stackexchange.com/Posts.xml')
    root = tree.getroot()
    keyword = "turing"
    ranks = dict()
    for child in root:
        try:
            if(keyword in [x.lower() for x in child.attrib['Body'].split()]):
                ranks[child] = scorer_difficult_problems( [getFeatures(child, userRoot)])
        except:
            pass
    r = sorted(ranks.iteritems(), key=lambda (k, v): -v )
    r = [child[0].attrib  for child in r[:10]]

    for x in r:
        print x


def main2():
    users = xml.parse('../stackdata/cs.stackexchange.com/Users.xml')
    userRoot = users.getroot()

    tree = xml.parse('../stackdata/cs.stackexchange.com/Posts.xml')
    root = tree.getroot()

    samples = getTrainingSample(root, userRoot, "testdata.txt")
    print samples
    clf = learn(samples);
    print clf


    keyword = "language"
    ranks = dict()
    for child in root:
        try:
            print clf.predict([getFeatures(child, userRoot)])
        except:
            pass
    print ranks
main2()
