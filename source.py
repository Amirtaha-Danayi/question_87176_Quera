def game(number):
    list = []
    for i in str(number):
        list.append(i)
    sort_list = sorted(list)
    return int(sort_list[1]) - int(sort_list[0])