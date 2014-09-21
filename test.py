import xml.etree.ElementTree as xml

pitfalls = ["long", "difficult", "hard", "understand", "formidable", "challenging", "troublesome", "confused", "test", "tried"]
beginner = ["new", "first", "time", "never", "hw"]

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
    return score

def scorer_difficult_problems(child):
    weights = [10, 1, 100, 10, 100]
    return scorer(weights, child)

def scorer_common_pitfall(child):
    weights = [100, 10, 100, 10, 100]
    return scorer(weights, child)

tree = xml.parse('data/Posts.xml')
root = tree.getroot()
mostviews = 0
keyword = "regular"
ranks = dict()
for child in root:
    try:
        if(keyword in [x.lower() for x in child.attrib['Body'].split()]):
            ranks[child] = scorer_common_pitfall(child)
    except:
        pass
r = sorted(ranks.iteritems(), key=lambda (k, v): -v )
r = [child[0].attrib  for child in r[:10]]
for x in r:
    print x
