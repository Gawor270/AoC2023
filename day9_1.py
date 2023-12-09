with open('input/in9') as file:
    f = file.read().strip().split('\n')

def process(l):
    diff = [l[i+1] - l[i] for i in range(len(l)-1)]
    return l[-1] if all(value == 0 for value in l) else l[-1] + process(diff)
    
oasis = [list(map(int,el.split(' '))) for el in f]
print(sum([process(o) for o in oasis]))