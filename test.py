import xml.etree.ElementTree as xml

pitfalls = ["long", "difficult", "hard", "understand", "formidable", "challenging", "troublesome", "confused", "test", "tried"]
beginner = ["beginner", "elementry", "sorry", "new", "first", "time", "never", "hw", "easy"]

def scorer(weights, child):
    score = 0
    try:
        score += weights[0]*float(child.attrib['ViewCount'])
    except:
        pass
    try:
        score += weights[1]*float(child.attrib['Counts'])
    except:
        pass
    try:
        score += weights[2]*float(child.attrib['Score'])
    except:
        pass
    try:
        for word in pitfalls:
            if word in [x.lower for x in child.attrib['Body'].split()]:
                score += weights[3]
    except:
        pass
    try:
        for word in beginner:
            if word in [x.lower for x in child.attrib['Body']]:
                score += weights[4]
    except:
        pass
    try:
        user = child.attrib['OwnerUserId']
        for x in userRoot:
            if x.attrib['Id'] == user:
                score += weights[5]*float(x.attrib['Reputation'])
    except:
        pass
    return score

def scorer_difficult_problems(child):
    weights = [50, 10, 10, 200, -100, 1]
    return scorer(weights, child)

def scorer_common_pitfall(child):
    weights = [100, 50, 50, 100, 200, -1]
    return scorer(weights, child)

users = xml.parse('../stackdata/cs.stackexchange.com/Users.xml')
userRoot = users.getroot()



tree = xml.parse('../stackdata/cs.stackexchange.com/Posts.xml')
root = tree.getroot()
mostviews = 0
keyword = "turing"
ranks = dict()
for child in root:
    try:
        if(keyword in [x.lower() for x in child.attrib['Body'].split()]):
            ranks[child] = scorer_difficult_problems(child)
    except:
        pass
r = sorted(ranks.iteritems(), key=lambda (k, v): -v )
r = [child[0].attrib  for child in r[:10]]

for x in r:
    print x
