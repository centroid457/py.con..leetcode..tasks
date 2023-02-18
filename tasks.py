import re
from typing import *
import pytest


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        return sum(map(max, zip(*grid)))


@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([[[1,2,4],[3,3,1]]], 8),
        ([[[10]]], 10),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().deleteGreatestValue
    result = test_obj_link(*params)
    assert result == EXPECTED
