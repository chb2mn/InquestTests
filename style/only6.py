


def only6(nums):
    return [x for x in nums if x % 6 == 0 and x > 0]

if __name__ == '__main__':
    nums = range(100)
    only6_list = only6(nums)
    print only6_list
