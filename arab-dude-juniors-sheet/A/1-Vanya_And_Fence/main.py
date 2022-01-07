if __name__ == '__main__':
    l = input()
    ls = l.split(" ")
    nfriends = int(ls[0])
    hfence = int(ls[1])
    hfriends = (input()).split(" ")
    hfriends = map(int, hfriends)
    length = 0
    for h in hfriends:
        if h > hfence:
            length += 2
        else:
            length += 1
    print(length)
    