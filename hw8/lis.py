def lis(s):
    if s == "": return ""
    lis = []
    for i, c in enumerate(s):
        lis.append((1, c))
        for j in range(i):
            if lis[j][0] + 1 > lis[i][0] and c > lis[j][1][-1]:
                lis[i] = (lis[j][0] + 1, lis[j][1] + c)
    return sorted(lis)[-1][1]

if __name__=='__main__':
    print(lis("aebbcg"))
    print(lis("zyx"))