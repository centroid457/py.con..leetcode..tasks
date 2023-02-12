import re
from typing import *
import pytest


class Solution:
    def PascalTriangle(self, numRows: int) -> List[List[int]]:
        rows = []
        row_prev = []

        for row_index in range(numRows):
            row = [1]
            row_index_center = (row_index+2)//2 -1

            for element_index in range(1, row_index+1):
                if element_index == row_index_center and not row_index%2:
                    row.append(row_prev[element_index] * 2)
                    row.extend(row[0:-1][::-1])
                    break
                elif element_index <= row_index_center:
                    row.append(row_prev[element_index - 1] + row_prev[element_index])
                    continue

                row.extend(row[::-1])
                break

            row_prev = row
            rows.append(row)

        return rows


@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([1], [[1]]),
        ([2], [[1],[1,1]]),
        ([3], [[1],[1,1],[1,2,1]]),
        ([4], [[1],[1,1],[1,2,1],[1,3,3,1]]),
        ([5], [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().PascalTriangle
    result = test_obj_link(*params)
    assert result == EXPECTED
