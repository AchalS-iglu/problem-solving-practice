if __name__ == "__main__":
    n = int(input())
    count = 0
    for i in range(n):
        prblms = input().split(" ")
        if prblms.count("1") >= 2:
            count += 1
    print(count)