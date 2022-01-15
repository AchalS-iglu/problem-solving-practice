if __name__ == "__main__":
    n = int(input())
    stones = list(input())
    prev = None
    count = 0
    for stone in stones:
        if stone == prev:
            count += 1
        prev = stone
    print(count)