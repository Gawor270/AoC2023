with open('input/in4','r') as file:
    no_cards = [1 for _ in range(214)]
    cnt = 0
    for line in file:
        split_sequence = line.split(" | ")
        split_sequence[0] = split_sequence[0].split(":")[1]
        list1 = list(map(int, split_sequence[0].split()))
        list2 = list(map(int, split_sequence[1].split()))

        winning = {key : True for key in list1}
        curr = 0
        for x in list2:
            if(x in winning): curr+=1

        for i in range(cnt+1, cnt + curr +1): no_cards[i] += no_cards[cnt]
        cnt += 1

    print(sum(no_cards))