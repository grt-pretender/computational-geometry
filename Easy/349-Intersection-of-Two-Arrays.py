# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:

	# storing unique common elements
    visited, res = {}, []

    for k in nums1:
    	visited[k] = k
    
    for c in nums2:
        if c in visited:
            res.append(c)
            visited.pop(c)
    return res

nums1 = [1,2,2,1]
nums2 = [2,2]
ans = intersection(nums1, nums2)
print(ans)
