with open('input/tin6') as file:
    f = file.read().strip().split('\n')

times = list(map(int,f[0].split(':')[1].split()))
distances = list(map(int,f[1].split(':')[1].split()))


res = 1
for i in range(len(times)):
    count = 0
    for time in range(1,times[i]):
        if(time*(times[i] - time) > distances[i]):
            count += 1
    
    res *= count

print(res)