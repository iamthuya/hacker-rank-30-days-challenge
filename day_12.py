class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def print_person(self):
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id_number)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, first_name, last_name, id_number, scores):
        super().__init__(first_name, last_name, id_number)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        score = sum(self.scores) / len(self.scores)
        if 90 <= score <= 100:
            return "O"
        elif 80 <= score < 90:
            return "E"
        elif 70 <= score < 80:
            return "A"
        elif 55 <= score < 70:
            return "P"
        elif 40 <= score < 55:
            return "D"
        else:
            return "T"


def main():
    line = input().split()
    first_name = line[0]
    last_name = line[1]
    id_number = line[2]
    num_scores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(first_name, last_name, id_number, scores)
    s.printPerson()
    print("Grade:", s.calculate())


if __name__ == "__main__":
    main()
