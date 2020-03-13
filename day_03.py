def main():
    n = int(input())
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 6:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")


if __name__ == "__main__":
    main()
