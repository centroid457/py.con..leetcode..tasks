import re
from typing import *
import pytest


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        result1_list = []

        num1_prev = None
        for num1_index, num1 in enumerate(nums[:-2:]):
            if num1 == num1_prev:
                result1_list.append(result1_list[-1])
                continue
            num1_prev = num1

            result2_list = []
            num2_prev = None
            for num2_index, num2 in enumerate(nums[num1_index + 1:-1:]):
                if num2 == num1:
                    continue
                if num2 == num2_prev:
                    result1_list.append(result2_list[-1])
                    continue
                num2_prev = num2

                part3 = nums[num2_index + 1::]
                result3 = len(part3) - part3.count(num1) - part3.count(num2)
                if result3 < 0:
                    result3 = 0

                result2_list.append(result3)

            result1_list.append(sum(result2_list))
        return sum(result1_list)


@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([[4,4,2,4,3]], 3),
        ([[1,1,1,1,1]], 0),

        ([[1]], 0),
        ([[1,1]], 0),
        ([[1, 1, 1]], 0),
        ([[1, 1, 3]], 0),
        ([[1, 2, 3]], 1),
        ([[1, 2, 3, 3]], 2),

        ([[1,3,1,2,4]], 7),

    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().unequalTriplets
    result = test_obj_link(*params)
    assert result == EXPECTED
