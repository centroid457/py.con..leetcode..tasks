import re
from typing import *
import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        if n > 2:
            return 2+self.climbStairs(n - 2)
        else:
            return n



@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([1], 1),
        ([2], 2),
        ([3], 3),
        ([4], 5),
        ([5], 8),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().climbStairs
    result = test_obj_link(*params)
    assert result == EXPECTED
