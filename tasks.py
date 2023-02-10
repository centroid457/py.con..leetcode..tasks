import re
from typing import *
import pytest

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ord_A = ord("A") - 1
        base = 26

        result = ""
        while columnNumber:
            value = columnNumber % base
            value = value or base
            result = chr(value + ord_A) + result

            if columnNumber == base:
                break
            columnNumber = (columnNumber - 1)//base

        return result



@pytest.mark.parametrize(
    argnames="params,EXPECTED",
    argvalues=[
        ([1], "A"),
        ([7], "G"),
        ([26], "Z"),
        ([27], "AA"),
        ([28], "AB"),
        ([676], "YZ"),
        ([701], "ZY"),
        ([17576], "YYZ"),

    ]
)
def test__solution(params,EXPECTED):
    test_obj_link = Solution().convertToTitle
    result = test_obj_link(*params)
    assert result == EXPECTED

