import re
from typing import *
import pytest


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n%3 == 0:
            n = n/3

        return n == 1


@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([-3], False),
        ([0], False),
        ([1], True),
        ([2], False),
        ([3], True),
        ([8], False),
        ([9], True),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().isPowerOfThree
    result = test_obj_link(*params)
    assert result == EXPECTED
