if __name__ == "__main__":
    usernameUniqueChars = set(list(input()))
    if len(usernameUniqueChars) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")