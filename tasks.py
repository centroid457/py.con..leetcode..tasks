import re
from typing import *
import pytest


class Solution:
    def countDigits(self, num: int) -> int:
        num_str = str(num)
        deviders = set(map(int, num_str))
        result = 0
        for devider in list(deviders):
            if not num%devider:
                result += num_str.count(str(devider))

        return result


@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([7], 1),
        ([121], 2),
        ([1248], 4),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().countDigits
    result = test_obj_link(*params)
    assert result == EXPECTED
