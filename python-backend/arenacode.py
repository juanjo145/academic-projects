from sys import stdin

def create_kupellakes_bst(nums):
    if not nums:
        return ''
    if len(nums) == 1:
        return str(nums[0])
    left_sum = nums[0]
    right_sum = sum(nums[1:])
    min_diff = abs(left_sum - right_sum)
    min_diff_idx = 0
    for i in range(1, len(nums)):
        left_sum += nums[i]
        right_sum -= nums[i]
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff
            min_diff_idx = i
        elif diff == min_diff and left_sum > sum(nums[:min_diff_idx+1]):
            min_diff_idx = i
    left_subtree = create_kupellakes_bst(nums[1:min_diff_idx+1])
    right_subtree = create_kupellakes_bst(nums[min_diff_idx+1:])
    if left_subtree and right_subtree:
        return f"{nums[min_diff_idx]}({left_subtree},{right_subtree})"
    elif left_subtree:
        return f"{nums[min_diff_idx]}({left_subtree})"
    else:
        return f"{nums[min_diff_idx]}({right_subtree})"

def main():
    cases = int(stdin.readline())
    for case in range(1, cases+1):
        secuencia = int(stdin.readline())
        num = list(map(int, stdin.readline().split()))

        bst_representation = create_kupellakes_bst(num)
        print(f"Case #{case}: {bst_representation}")

main()