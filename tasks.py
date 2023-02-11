import re
from typing import *
import pytest


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = None
        finish = None

        def result_append():
            if start == finish:
                result.append(f"{start}")
            else:
                result.append(f"{start}->{finish}")

        for num in nums:
            # INIT range
            if start is None:
                start = num
                finish = num
                continue

            # WORK
            if num > (finish + 1):
                result_append()
                start = num

            finish = num

        if start is not None:
            result_append()

        return result


@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([[0,1,2,4,5,7]], ["0->2","4->5","7"]),
        ([[0,2,3,4,6,8,9]], ["0","2->4","6","8->9"]),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().summaryRanges
    result = test_obj_link(*params)
    assert result == EXPECTED

