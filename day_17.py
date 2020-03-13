class Calculator(object):
    @staticmethod
    def power(n, p):
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")
        else:
            return n ** p


def main():
    my_calculator = Calculator()
    T = int(input())
    for i in range(T):
        n, p = map(int, input().split())
        try:
            ans = my_calculator.power(n, p)
            print(ans)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

