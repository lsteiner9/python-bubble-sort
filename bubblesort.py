def sort(nums):
    length = len(nums)
    while True:
        count = 0
        for i in range(0, length - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count += 1
        if count == 0:
            break


def main():
    length = int(input("First enter the number of elements, then enter each "
                       "element individually:  "))
    nums = []
    for i in range(0, length):
        nums.append(int(input()))
    sort(nums)
    print(nums)


if __name__ == '__main__':
    main()
