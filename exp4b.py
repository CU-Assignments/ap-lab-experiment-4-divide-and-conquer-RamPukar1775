def beautifulArray(n):
    if n == 1:
        return [1]
    odd = [2 * x - 1 for x in beautifulArray((n + 1) // 2)]
    even = [2 * x for x in beautifulArray(n // 2)]
    return odd + even

# Example usage
print(beautifulArray(4))  # Output: [2,1,4,3] or any valid permutation
