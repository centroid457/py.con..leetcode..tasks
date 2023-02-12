import re
from typing import *
import pytest


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_set: set = set()

        for num in nums:
            if len(max_set) < 3:
                max_set.add(num)
                continue

            max_set_min = min(max_set)
            if num > max_set_min and num not in max_set:
                max_set.remove(max_set_min)
                max_set.add(num)

        if len(max_set) < 3:
            return max(max_set)
        else:
            return min(max_set)



@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([[3,2,1]], 1),
        ([[3,2,]], 3),
        ([[3, 2, 2]], 3),
        ([[2, 2, 2]], 2),
        ([[2, ]], 2),

        ([[5,2,4,1,3,6,0]], 4),
        ([[1,2,2,5,3,5]], 2),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().thirdMax
    result = test_obj_link(*params)
    assert result == EXPECTED

