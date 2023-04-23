def is_samePatterns(colors, patterns):
    if len(colors) != len(patterns):
       return False
    sdict = {}
    pset = set()
    sset = set()
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        print(pset)
        print(sset)
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []
            print("->",sdict)
        keys = sdict[patterns[i]]
        print("Keys:",keys)
        keys.append(colors[i])
        sdict[patterns[i]] = keys
        print("=>",sdict)
    print(sdict,pset,sset)
    if len(pset) != len(sset):
       return False
    print(sdict.values())
    #for values in sdict.values():
    #    for i in range(len(values) - 1):
    #        if values[i] != values[i+1]:
    #           return False
    return True
print(is_samePatterns(["red",
"green",
"green"], ["a",
"b",
"b"]))
print(is_samePatterns(["red",
"green",
"greenn"], ["a",
"b",
"b"]))


def samePatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    sdict = {}
    for i in range(len(patterns)):
        if patterns[i] not in sdict:
            sdict[patterns[i]] = colors[i]
        elif sdict[patterns[i]] != colors[i]:
            return False
    return True

# Example usage
color1 = ["red", "green", "green"]
patterns1 = ["a", "b", "b"]
print(samePatterns(color1, patterns1))  # Output: True

color2 = ["red", "green", "greenn"]
patterns2 = ["a", "b", "b"]
print(samePatterns(color2, patterns2))  # Output: False















    
