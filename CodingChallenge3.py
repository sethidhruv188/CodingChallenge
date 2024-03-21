def is_subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    if dp[n][target]:
        subset = []
        i, j = n, target
        while i > 0 and j > 0:
            if dp[i][j] != dp[i - 1][j]:
                subset.append(nums[i - 1])
                j -= nums[i - 1]
            i -= 1
        return True, subset[::-1]
    else:
        return False, []


# Example usage:
nums = [1, 3, 5, 0, 11, 17, 9, 5]
target = 10
exists, subset = is_subset_sum(nums, target)
if exists:
    print("Such a subset exists:", subset)
else:
    print("No subset exists.")
