import numpy as np

class Solution(object):
    def prod(self, numbers):
        return np.prod(numbers)

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = []
        # for index , num in enumerate(nums):
        #     product = int(self.prod(nums[:index]) * self.prod(nums[index + 1:]))
        #     result.append(product)
        # return result

        total_product = 1
        zero_element_count = 0
        has_zero = False
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                has_zero = True
                zero_element_count += 1

        result = []
        if zero_element_count > 1:
            return [0] * len(nums)
        if has_zero:
            # if zero_element_count >= len(nums) - 1 and len(nums) > 2:
            #     return [0] * len(nums)
            for num in nums:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
        else:
             for num in nums:
                result.append(total_product // num)
        return result
    
