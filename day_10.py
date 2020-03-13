def main():
    n = int(input())
    max_count = 0
    count = 0

    while n != 0:
        remainder = n % 2
        n = n // 2

        if remainder == 1:
            count += 1
            max_count = count if max_count < count else max_count
        else:
            count = 0

    print(max_count)


if __name__ == "__main__":
    main()
