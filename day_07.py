def main():
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    [print(i, end=" ") for i in arr]


if __name__ == "__main__":
    main()
