with open('input/in4','r') as file:
    res = 0
    for line in file:
        line = line[10:]
        split_sequence = line.split(" | ")
        list1 = list(map(int, split_sequence[0].split()))
        list2 = list(map(int, split_sequence[1].split()))

        winning = {key : True for key in list1}
        curr = 0
        for x in list2:
            if(x in winning): curr+=1

        if(curr): res += 2**(curr-1)

    print(res)