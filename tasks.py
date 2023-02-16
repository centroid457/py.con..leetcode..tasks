import re
from typing import *
import pytest


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for num in range(1, n+1):
            part = ""
            if not num%3:
                part += "Fizz"
            if not num%5:
                part += "Buzz"

            part = part or str(num)

            result.append(part)

        return result

@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([3], ["1","2","Fizz"]),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().fizzBuzz
    result = test_obj_link(*params)
    assert result == EXPECTED
