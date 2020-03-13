def main():
    s = input().strip()
    try:
        print(int(s))
    except Exception as e:
        print("Bad String")


if __name__ == "__main__":
    main()
