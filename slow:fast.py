nums = [1, 1, 1, 1, 2, 2, 2.3, 3, 4, 3, 4, 5, 6, 5, 5, 5, 6]
'''        
slowRunner = 0
for fastRunner in range(len(nums)):
        if slowRunner == something slowy:
                slowRunner += 1
'''
j = 0
for i in range(1, len(nums)):
        # if current element is not duplicate, 
        # slow runner grows one step and copys the current value
        if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

print(nums)