def reversePairs(nums):
    def merge_sort(start, end):
        if start >= end:
            return 0
        
        mid = (start + end) // 2
        count = merge_sort(start, mid) + merge_sort(mid + 1, end)
        
        # Count reverse pairs
        j = mid + 1
        for i in range(start, mid + 1):
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))
        
        # Merge step (standard merge sort merge)
        temp = []
        i, j = start, mid + 1
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= end:
            temp.append(nums[j])
            j += 1
        
        # Copy sorted values back
        for i in range(len(temp)):
            nums[start + i] = temp[i]
        
        return count
    
    return merge_sort(0, len(nums) - 1)

# Example usage
nums = [1, 3, 2, 3, 1]
print(reversePairs(nums))  # Output: 2
