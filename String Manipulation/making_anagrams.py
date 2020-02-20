def makeAnagram(a, b):
    intersect = set(a).intersection(b)
    anagram = sum(min(a.count(letter),b.count(letter)) for letter in intersect)
    return(len(a)+len(b)-2*anagram)


a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
c = "showman"
d = "woman"
res = makeAnagram(a, b)
print(res)