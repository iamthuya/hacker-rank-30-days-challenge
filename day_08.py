
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phoneBook = {}
for _ in range(n):
    name, number = input().strip().split()
    phoneBook[name] = int(number)

while True:
    try :
        name = input()
        if name in phoneBook:
            print("{}={}".format(name, phoneBook[name]))
        else:
            print("Not found")
    except Exception as e:
        break
