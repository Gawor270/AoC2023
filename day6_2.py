import math
with open('input/in6') as file:
    f = file.read().strip().split('\n')

time = int(''.join(f[0].split(':')[1].split()))
distance = int(''.join(f[1].split(':')[1].split()))

if(time*time - 4*distance >0):
    delta = math.sqrt(time*time - 4*distance)
    l = math.ceil((time-delta)/2)
    u = math.floor((time+delta)/2)
    print(u - l +1)