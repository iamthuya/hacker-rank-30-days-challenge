import os


def factorial(n):
    if n == 1:
        return n

    return n * factorial(n - 1)


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()


if __name__ == "__main__":
    main()
