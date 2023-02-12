import re
from typing import *
import pytest


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:0>32b}"[::-1], 2)


@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([0b00000010100101000001111010011100], 0b00111001011110000010100101000000),
        ([0b11111111111111111111111111111101], 0b10111111111111111111111111111111),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().reverseBits
    result = test_obj_link(*params)
    assert result == EXPECTED

