def k_elements_max_product(nums: list[int], k: int) -> int:
    window_product = 1
    for i in range(k):
        window_product *= nums[i]

    max_product = window_product

    for r in range(k, len(nums)):
        l = r - k
        window_product = 1
        for i in range(l, r):
            window_product *= nums[i]
        max_product = max(max_product, window_product)

    return max_product

print(k_elements_max_product([3, 0, 5, 9, 4, 1], 3))
