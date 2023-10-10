numbers = input().split(", ")

def ispalindrome(number):

    for i in number:
        if i == i[::-1]:
            print(f'True')
        else:
            print(f'False')

ispalindrome(numbers)