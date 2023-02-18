import re
from typing import *
import pytest


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        result = 0
        while grid[0]:
            max_element = 0
            for row in grid:
                element = row.pop()
                if max_element < element:
                    max_element = element
            result += max_element
        return result


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
