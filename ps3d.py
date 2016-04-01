def subStringMatchExactlyOneSub(target,key):
    Answers = []
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        for matchFiltered in filtered:
            if key[miss] != target[matchFiltered + len(key1)]:
                Answers.append(matchFiltered)
    print("possible matches for exactly one element of", key, "incorrectly matched", target, "start at:")
    print(tuple(Answers))
    return tuple(Answers)
    
def subStringMatchExact(target,key):
    pos = []
    for i in range(0, len(target)):
        if target[i:i+len(key)] == key:
            pos.append(i)
    return tuple(pos)

def constrainedMatchPair(firstMatch,secondMatch,length):
    n = []
    for i in firstMatch:
        for j in secondMatch:
            if i + length +1 == j:
                n.append(i)
    return tuple(n)
    
#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

subStringMatchExactlyOneSub(target1, key10)