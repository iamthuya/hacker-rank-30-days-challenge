def hour_glass_sum(arr, i, j):
    line_1 = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
    line_2 = arr[i][j]
    line_3 = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]

    return line_1 + line_2 + line_3


def main():
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    largest = float('-Inf')
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            value = hour_glass_sum(arr, i, j)
            largest = value if value > largest else largest

    print(largest)


if __name__ == "__main__":
    main()