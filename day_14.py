import itertools


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximum_difference = None

    # Add your code here
    def compute_difference(self):
        self.maximum_difference = max([abs(i - j) for (i, j) in itertools.product(self.__elements, self.__elements)])


def main():
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.compute_difference()

    print(d.maximum_difference)


if __name__ == "__main__":
    main()
