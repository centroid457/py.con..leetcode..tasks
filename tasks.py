import re
from typing import *
import pytest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""

        num1_rev = num1[::-1]
        num2_rev = num2[::-1]

        add_over = 0
        while num1_rev or num2_rev or add_over:
            try:
                n1 = int(num1_rev[0])
            except:
                n1 = 0
            try:
                n2 = int(num2_rev[0])
            except:
                n2 = 0

            num1_rev = num1_rev[1::]
            num2_rev = num2_rev[1::]

            result_i = n1 + n2 + add_over
            add_over = 1 if result_i > 9 else 0
            result = str(result_i%10) + result

        while result[0] == "0" and len(result)>1:
            result = result[1::]
        return result

@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        (["0", "0"], "0"),
        (["0", "1"], "1"),
        (["1", "2"], "3"),
        (["11", "123"], "134"),
    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().addStrings
    result = test_obj_link(*params)
    assert result == EXPECTED
