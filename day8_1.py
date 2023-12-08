with open('input/in8') as file:
    f = file.read().strip().split('\n')

instructions = f[0]
moves = dict([[el.split('=')[0].replace(" ",""),el.split('=')[1].replace("(","").replace(")","").replace(" ","").split(',')] for el in f[2:]])
curr = "AAA"
count = i = 0
while(curr != "ZZZ"):
    if(instructions[i] == 'L'): curr = moves[curr][0]
    else: curr = moves[curr][1]
    i = (i+1)%len(instructions)
    count += 1

print(count)

