import queue


class Solution:
    # Write your code here
    def __init__(self):
        self.s = []
        self.q = queue.Queue()

    def push_character(self, a):
        self.s.append(a)

    def pop_character(self):
        return self.s.pop()

    def enqueue_character(self, a):
        self.q.put(a)

    def dequeue_character(self):
        return self.q.get()


def main():
    # read the string s
    s = input()
    # Create the Solution class object
    obj = Solution()

    l = len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.push_character(s[i])
        obj.enqueue_character(s[i])

    is_palindrome = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    '''
    for i in range(l // 2):
        if obj.pop_character() != obj.dequeue_character():
            is_palindrome = False
            break
    # finally print whether string s is palindrome or not.
    if is_palindrome:
        print("The word, " + s + ", is a palindrome.")
    else:
        print("The word, " + s + ", is not a palindrome.")


if __name__ == "__main__":
    main()
