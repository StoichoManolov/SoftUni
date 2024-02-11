from typing import List


def numbers(args: List[int]):
    positives = sum(num for num in args if num > 0)
    negatives = sum(num for num in args if num < 0)

    print(negatives)
    print(positives)

    if abs(negatives) > positives:
        print(f'The negatives are stronger than the positives')
    else:
        print(f'The positives are stronger than the negatives')


nums = [int(x) for x in input().split()]

numbers(nums)








