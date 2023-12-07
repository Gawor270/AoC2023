from collections import Counter

with open('input/in7') as file:
    f = file.read().strip().split('\n')


mapping = {'A':'Z','K':'Y','Q':'X','J':'W','T':'V'}
for i in range(8):
    mapping[chr(ord('9')-i)] = chr(ord('9')-i)

def transform1(s):
    cnt = Counter(s)
    return sorted(cnt.values(), reverse=True)

def transform2(s):
    res = ""
    for i in range(len(s)):
        res = res + mapping[s[i]]
    
    return res

cards = [[el.split(' ')[0],int(el.split(' ')[1])] for el in f]
cards.sort(key = lambda x :[transform1(x[0]),transform2(x[0])])
print(sum([(i+1)*cards[i][1] for i in range(len(cards))]))