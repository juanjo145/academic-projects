from sys import stdin

def create_kupellakes_bst(nums):
    def build_bst(left, right):
        if left > right:
            return ""
        root_idx = left
        min_diff = float("inf")
        max_left_sum = float("-inf")
        for i in range(left, right+1):
            if i != right and nums[i] == nums[i+1]:
                continue
            if i == left:
                left_sum = 0
            else:
                left_sum = sum(nums[left:i])
            right_sum = sum(nums[i:right+1])
            diff = abs(left_sum - right_sum)
            if diff < min_diff:
                root_idx = i
                min_diff = diff
                max_left_sum = left_sum
            elif diff == min_diff and left_sum > max_left_sum:
                root_idx = i
                max_left_sum = left_sum
        if left == right:
            return str(nums[left])
        left_subtree = build_bst(left, root_idx-1)
        right_subtree = build_bst(root_idx+1, right)
        return f"{nums[root_idx]}({left_subtree},{right_subtree})" if left_subtree and right_subtree else f"{nums[root_idx]}{left_subtree}{right_subtree}"
    return build_bst(0, len(nums)-1)

def main():
    cases = int(stdin.readline())
    for case in range(1, cases+1):
        secuencia = int(stdin.readline())
        num = list(map(int, stdin.readline().split()))

        bst_representation = create_kupellakes_bst(num)
        print(f"Case #{case}: {bst_representation}")

main()
