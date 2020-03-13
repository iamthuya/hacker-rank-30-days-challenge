def space_print(s):
    return "".join([s[i] for i in range(len(s)) if i % 2 == 0]) + " " + "".join(
        [s[i] for i in range(len(s)) if i % 2 != 0])


def main():
    n = int(input())
    for _ in range(n):
        print(space_print(input()))


if __name__ == "__main__":
    main()
