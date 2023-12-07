from collections import Counter

with open('input/in7') as file:
    f = file.read().strip().split('\n')

mapping = {'A':'Z','K':'Y','Q':'X','T':'V'}
for i in range(8):
    mapping[chr(ord('9')-i)] = chr(ord('9')-i)
mapping['J'] = '/'

def transform1(s):
    cnt = Counter(s)
    if(len(cnt) == 1 and 'J' in cnt):
        return [5]
    
    if('J' in cnt):
        val  = cnt['J']
        del cnt['J']
        cnt[max(cnt, key = cnt.get)] += val
        
    return sorted(cnt.values(), reverse=True)

def transform2(s):
    res = ""
    for i in range(len(s)):
        res = res + mapping[s[i]]
    
    return res

cards = [[el.split(' ')[0],int(el.split(' ')[1])] for el in f]
cards.sort(key = lambda x :(transform1(x[0]),transform2(x[0])))
print(sum([(i+1)*cards[i][1] for i in range(len(cards))]))