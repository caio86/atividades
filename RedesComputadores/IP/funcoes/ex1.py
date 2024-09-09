def menor(*nums):

    if len(nums) < 1:
        raise Exception("not enough arguments")

    menor = nums[0]
    for i in range(2, len(nums)):
        if nums[i] < menor:
            menor = nums[i]

    return menor


def main():
    print(menor(1, 2, 3))
    print(menor(4, 20, -1000))
    # print(menor())


main()
