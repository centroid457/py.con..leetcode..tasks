import re
from typing import *
import pytest


class Solution:
    def hammingWeight(self, n: int) -> int:
        return list(f"{n:b}").count("1")



@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([1], 1),
        ([0b00000000000000000000000000001011], 3),
        ([0b00000000000000000000000010000000], 1),
        ([0b11111111111111111111111111111101], 31),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().hammingWeight
    result = test_obj_link(*params)
    assert result == EXPECTED

