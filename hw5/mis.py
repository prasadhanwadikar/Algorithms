def max_wis(a):
    dict = {} #for memorization
    return internal_max_wis(dict, a)

def internal_max_wis(dict, a):
    l = len(a)
    if a == [] or max(a) < 0:
        dict[l] = (0, [])
    else:
        if l not in dict:
            f1 = internal_max_wis(dict, a[:-1])
            f2 = internal_max_wis(dict, a[:-2])
            f2 = (f2[0] + a[l-1], f2[1] + [a[l-1]])
            dict[l] = f1 if f1[0] >= f2[0] else f2
    return dict[l]

def max_wis2(a):
    if a == [] or max(a) < 0:
        return (0, [])
    l = len(a)
    a = [0, 0] + a
    tuple_list = [(0, 0), (0, 0)] #(sum_at_my_position, include_me)
    for i in range(2, l+2):
        sum_with_me = tuple_list[i-2][0] + a[i]
        sum_till_me = tuple_list[i-1][0]
        tuple = (sum_with_me, 1) if sum_with_me > sum_till_me else (sum_till_me, 0)
        tuple_list.append(tuple)
    i = len(tuple_list)-1
    max_sum = tuple_list[i][0]
    mis = []
    while(i > 1):
       if (tuple_list[i][1] == 1):
            mis.append(a[i])
            i -= 2
       else:
            i -= 1
    return (max_sum, mis[::-1])