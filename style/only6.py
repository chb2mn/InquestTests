


def only6(nums):
    for i in nums:
        if i % 6 == 0 and i > 0:
           print i


if __name__ == '__main__':
    nums = range(100)
    only6(nums)
