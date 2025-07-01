# isomorphic strings
class Solution(object):
    def isIsomorphic(self, s, t):
        return encode(s) == encode(t)
def encode(s):
    mapping = {}
    pattern = []
    counter = 0
    for ch in s:
        if ch not in mapping:
            mapping[ch] = counter
            counter += 1
        pattern.append(mapping[ch])
    return pattern
