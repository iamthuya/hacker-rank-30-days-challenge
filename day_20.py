def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    # Write Your Code Here
    swap = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1

        if swap == 0:
            break

    print("Array is sorted in {} swaps.".format(swap))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


if __name__ == "__main__":
    main()
