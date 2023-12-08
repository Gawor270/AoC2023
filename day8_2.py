from functools import reduce
import math

with open('input/in8') as file:
    f = file.read().strip().split('\n')

instructions = list(map(int,f[0].replace("L","0").replace("R","1")))
moves = dict([[el.split('=')[0].replace(" ",""),el.split('=')[1].replace("(","").replace(")","").replace(" ","").split(',')] for el in f[2:]])
curr = list(filter(lambda x : x[-1] == "A",moves.keys()))
no_steps = [-1 for _ in range(len(curr))]
count = cnt = i = 0
while(cnt != len(curr)):
    count += 1
    for j in range(len(curr)):
        curr[j] = moves[curr[j]][instructions[i]]
        if(curr[j][-1] == "Z" and no_steps[j] == -1):
            cnt += 1
            no_steps[j] = count

    i = (i+1)%(len(instructions))

    
print(reduce(lambda x,y : int(math.lcm(x,y)),no_steps))

