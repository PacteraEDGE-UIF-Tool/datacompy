def match(pattern, list):
    matches = []
    m = len(list)
    n = len(pattern)

    rightMostIndexes = preprocessForBadCharacterShift(pattern)
    print("================================")
    print(rightMostIndexes)

    alignedAt = 0
    while alignedAt + (n - 1) < m:

        for indexInPattern in range(n-1, -1, -1):
            indexInlist = alignedAt + indexInPattern
            x = list[indexInlist]
            y = pattern[indexInPattern]
            print("#")
            print(x)
            print(y)
            if indexInlist >= m:
                break

            if x != y:

                r = rightMostIndexes[x]

                if x not in rightMostIndexes:
                    alignedAt = indexInlist + 1

                else:
                    shift = indexInlist - (alignedAt + r)
                    alignedAt += (shift > 0 and shift or alignedAt + 1)
                break
            elif indexInPattern == 0:
                matches.append(alignedAt)
                alignedAt += 1


    return matches

def preprocessForBadCharacterShift(pattern):
    map = dict()
    for i in range(len(pattern)-1, -1, -1):
        print(pattern[i])
        c = pattern[i]
        if c not in map:
            map[c] = i
    return map

if __name__ == "__main__":
    '''
    matches = match("ana", "bananas")
    for integer in matches:
        print ("Match at:", integer)
    print (matches == [1, 3] and "OK" or "Failed")
    '''
    matches = match(["string1", "string2", "string3"], [["sad","yes","nope"],["string1", "string2", "string3"],["no","no"]])
    for integer in matches:
        print ("list Match at:", integer)
    print (matches)