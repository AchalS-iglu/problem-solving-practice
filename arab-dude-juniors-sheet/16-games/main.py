if __name__ == "__main__":
    n = int(input())
    home = []
    guest = []
    count = 0
    for i in range(n):
        x = input().split(" ")
        home.append(x[0])
        guest.append(x[1])
    for j in home:
        count += guest.count(j)
    print(count)