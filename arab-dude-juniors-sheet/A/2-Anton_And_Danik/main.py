#soez

if __name__ == "__main__":
    N = int(input())
    S = input()
    if S.count("A") > S.count("D"):
        print("Anton")
    elif S.count("A") < S.count("D"):
        print("Danik")
    else:
        print("Friendship")