with open('input/in5') as file:
    f = file.read().strip().split('\n\n')

seeds = list(map(int, f[0].split()[1:]))
mapping = [[list(map(int, line.split())) for line in f[i].split('\n')[1:]] for i in range(1, 8)]
ranges = [[seeds[i], seeds[i] + seeds[i+1]] for i in range(0,len(seeds),2)]

for map in mapping: map.sort(key=lambda item: item[1])

def rec(rang, depth = 0):
    if(depth == 7):
        return rang[0]
    
    last = 0
    val = 1e9
    for map in mapping[depth]:
        l = max(last,rang[0])
        u = min(map[1],rang[1])
        if(l < u):
            val = min(val,rec([l,u],depth+1))

        l = max(rang[0],map[1])
        u = min(rang[1],map[1] + map[2])
        if(l < u):
            diff = map[0] - map[1]
            val = min(val, rec([l+diff,u + diff],depth+1))
        
        last = u
    
    l = max(last,rang[0])
    u = rang[1]
    if(l < u): 
        val = min(val, rec([l,u],depth+1))
    
    return val

res = 1e9
for rang in ranges:
    res = min(res,rec(rang))

print(res)

    
    
    

    