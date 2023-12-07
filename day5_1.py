with open('input/in5') as file:
    f = file.read().strip().split('\n\n')

seeds = list(map(int, f[0].split()[1:]))
mapping = [[list(map(int, line.split())) for line in f[i].split('\n')[1:]] for i in range(1, 8)]

res = 1e9
for seed in seeds:
    next = seed
    for i in range(7):
        curr = next
        for d,s,l in mapping[i]:
            if(s <= curr and curr < s + l): 
                next = d + curr - s
    
    res = min(res, next)

print(res)